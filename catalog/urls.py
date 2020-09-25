from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
    url(r'^get_reviews',views.get_reviews,name='get_reviews'),
    url(r'^register',views.saveRegister,name='register'),

]