from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('login', views.Login.as_view(), name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('faq', views.faq, name = 'faq'),
    path('communication', views.communication, name = 'communication'),
    path('about', views.about, name = 'about'),
    path('catalog', include('shop.urls',  namespace = 'shop'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)