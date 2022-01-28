from django.urls import URLPattern, path

from . import views

#UrlConf
urlpatterns = [
#    path('playground/hello', views.say_hello)
    path('hello/', views.say_hello)
]