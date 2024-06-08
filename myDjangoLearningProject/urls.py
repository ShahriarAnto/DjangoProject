"""
URL configuration for myDjangoLearningProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myDjangoLearningProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage , name = 'home'),
    path('about-us/' , views.aboutUs , name = 'about'),
    path('another-page/' , views.anotherFunction),
    path('another-page-view/' , views.anotherPageFunction , name = "another-page"),
    path('course/<courseId>' , views.courseDetails),
    path('user-form-get' , views.userFormGet , name = 'getUserForm'),
    path('user-form-post' , views.userFormPost , name = 'postUserForm'),
    path('submitForm' , views.submitForm , name = 'submitForm'),
    path('calculator' , views.calculatorProject , name = 'calculator'),
    path('evenOdd' , views.evenOdd , name = 'evenOdd'),
    path('markSheet/' , views.markSheet , name = 'markSheet'),
    path('newsDetails/<news_id>' , views.newsDetails , name = 'newsDetails'),
    path('serviceDetails/<service_slug>' , views.serviceDetails , name = 'serviceDetails'),

]
