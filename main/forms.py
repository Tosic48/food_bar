import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from config import PASSWORD
from main.models import Review


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password (again)',
                                widget=forms.PasswordInput,
                                help_text='Введите тот же самый пароль еще раз для проверки')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'The entered passwords do not match', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'details', 'customers', 'photo']


def send_email(name, email, phone, date_time, choice):
    sender_email = "nikmarooo@mail.ru"  # Адрес электронной почты отправителя
    sender_password = PASSWORD  # Пароль электронной почты отправителя
    recipient_email = "nikmarooo@mail.ru"  # Адрес электронной почты получателя

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "New order"

    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nDate and time: {date_time}\nChoice: {choice}"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


def send_email2(name, email, phone, text):
    sender_email = "nikmarooo@mail.ru"  # Адрес электронной почты отправителя
    sender_password = PASSWORD  # Пароль электронной почты отправителя
    recipient_email = "nikmarooo@mail.ru"  # Адрес электронной почты получателя

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Contact me"

    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nText: {text}"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.mail.ru", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
