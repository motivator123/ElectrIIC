from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('register', views.registration, name = 'register'),
    path('faq', views.faq, name = 'faq'),
    path('communication', views.communication, name = 'communication'),
    path('about', views.about, name = 'about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)