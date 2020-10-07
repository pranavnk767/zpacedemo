from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
    url(r'^get_reviews',views.get_reviews,name='get_reviews'),
    url(r'^register',views.saveRegister,name='register'),
    url(r'^login',views.authenticate_user,name='login'),
    url(r'^get_adv',views.get_adv,name='get_adv'),
    url(r'^get_category',views.get_category,name='get_category'),

]