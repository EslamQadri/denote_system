from django.urls import path
from . import views 

urlpatterns=[
path('',views.home_page,name ='home'),
path('contact_us',views.contact_us_page,name ='contact_us'),
path('donores',views.donores_page,name ='donores'),
path('Registration',views.Registration_page,name ='Registration'),
path('Registration_ajax',views.Registration_ajax,name ='Registration_ajax'),


]