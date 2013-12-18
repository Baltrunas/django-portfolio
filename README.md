django-portfolio
================
Portfolio is well-suited for designers, programmers, photographers. The ability to create pages with a list of customers and their feedback. Create categories for projects, which provides a great opportunity to structure a portfolio. For each project, you can add multiple images. Each image can contain a title and a description.


# Required
* Django 1.5+
* sorl.thumbnail
* jQuery 2.0+


# Install
* Add to INSTALLED_APPS 'portfolio'
* Add to urls.py  url(r'^', include('portfolio.urls')),
* manage.py syncdb
* manage.py collectstatic


# ToDo
Models:
	Category
		? sites
	Project
	ScreenShot
		? Метод для обрамления скриншота как окна
		? типы\виды файлов для изображения
	Client
	Review

Pages:
	~ Клиенты
		http://mediatemple.net/company/clients/
		http://www.carbonneutral.com/our-clients/
		Client Since: 2007
	~ Клиент подробно

	- Отзывы
	- Отзыв

	~ Все категории
		Ограничить количество выводимых проектов
	~ Категория
		? Шаблон для категории
	~ Проект
		? Шаблон для проекта
	- Скриншот
		? Шаблон для изображения
		- Нормальные сноски

Views:
	? screenshot

Admin:

URLs:
	? screenshot

Tests:
