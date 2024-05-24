migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

admin:
	python manage.py createsuperuser

app:
	django-admin startapp $(word 2, $(MAKECMDGOALS))
	echo -e "from django.urls import path\n\n\
	from .views import *\n\n\n\
	urlpatterns = [\n\
	\tpath('', home, name='home'),\n\
	]" > $(word 2, $(MAKECMDGOALS))/urls.py
	sed -i "/^INSTALLED_APPS\s*=/,/^\s*\]/ s/^\(\s*\]\s*\)$$/    '$(word 2, $(MAKECMDGOALS))',\n\1/" ecommerce/settings.py
	sed -i "/^urlpatterns\s*=/,/^\s*\]/ s/^\(\s*\]\s*\)$$/	path('', include('$(word 2, $(MAKECMDGOALS)).urls')),\n\1/" ecommerce/urls.py

up:
	python manage.py runserver

shell:
	python manage.py shell