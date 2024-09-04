"""
URL configuration for diabetes project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('updatepro/',views.updatepro,name='updatepro'),
    path('pro/',views.pro_update,name='pro_update'),
    path('feedbacks/',views.feedbacks,name='feedbacks'),
    path('home/',views.home,name='home'),
    path('aduser/',views.aduser,name='aduser'),
    path('adfeedback/',views.adfeedback,name='adfeedback'),
    path('feedremove/<int:id>/',views.feedremove,name='feedremove'),
    path('useremove/<int:id>/',views.useremove,name='useremove'),
    path('adlog/',views.adlog,name='adlog'),
    path('contact/',views.contact,name='contact')

]
