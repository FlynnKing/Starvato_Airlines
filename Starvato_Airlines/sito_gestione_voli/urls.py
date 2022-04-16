from django.urls import path
from . import views



urlpatterns = [
         path('', views.home, name = 'home'),
         path('pannello_amministratore', views.admin_panel, name = 'contattaci')
]
