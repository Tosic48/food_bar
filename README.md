<h1>Сайт для продажи тортиков</h1>
<p>Это проект Django, предназначенный для помощи в продаже тортов. Здесь вы найдете отзывы на главной странице, навигацию в шапке, под блоком с отзывами можно оставить свой, страница с меню и возможностью заказать торт через форму.</p>
<h2>Установка и запуск</h2>
<p>Склонируйте репозиторий с помощью команды:</p>
<pre><code>git clone https://github.com/Tosic48/food_bar.git</code></pre>
<p>Установите необходимые пакеты:</p>
<pre><code>pip install -r requirements.txt</code></pre>
<p>Создайте базу данных и примените миграции:</p>
<pre><code>python manage.py makemigrations<br>python manage.py migrate</code></pre>
<p>Создайте суперпользователя:</p>
<pre><code>python manage.py createsuperuser</code></pre>
<p>Запустите сервер:</p>
<pre><code>python manage.py runserver</code></pre>
<p>Откройте браузер и перейдите по адресу <a href="http://localhost:8000/">http://localhost:8000/</a></p>
<h2>Функционал</h2>
<h3>Главная страница</h3>
<p>На главной странице вверху навигация по сайту, предварительное меню, карусель из отзывов и саму форму с возможностью оставить отзыв.</p>
<h3>О нас</h3>
<p>История о главной героине и ее становлении.</p>
<h3>Меню</h3>
<p>Реализовано меню с подгрузкой информации из БД и ниже есть форма оформления заказа (отправляет email с информацией из формы).</p>
<h3>Регистрация</h3>
<p>Добавлена возможность регистрации для пользователей.</p>
<h3>Контакты</h3>
<p>Если у вас возникли какие-либо вопросы или предложения, свяжитесь с нами по адресу: antonsuhodolski@tut.by
</p>
