from django.urls import path
from .views import home_view, services_view, blog_view, contact_view, about_view, success_stories_view

urlpatterns = [
    path('', home_view, name='home'),
    path('sobre-nosotros/', about_view, name='about'),
    path('servicios/', services_view, name='services'),
    path('casos-de-exito/', success_stories_view, name='success_stories'),
    path('blog/', blog_view, name='blog'),
    path('contacto/', contact_view, name='contact'),
]
