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
    path('adhome/',views.adhome,name='adhome'),
    path('aduser/',views.aduser,name='aduser'),
    path('adfeedback/',views.adfeedback,name='adfeedback'),
    path('feedremove/<int:id>/',views.feedremove,name='feedremove'),
    path('useremove/<int:id>/',views.useremove,name='useremove'),
    path('adlog/',views.adlog,name='adlog'),
    path('info/',views.info,name='info'),
    path('adinfo/',views.adinfo,name='info'),
    path('inforemove/<int:id>/',views.inforemove,name='inforemove'),
    path('docreg/',views.docreg,name='docreg'),
    path('doclog/',views.doclog,name='doclog'),
    path('dochome/',views.dochome,name='dochome'),
    path('doclist/',views.doclist,name='doclist'),
    path('dlist/',views.dlist,name='dlist'),
    path('ddelete/<int:id>/',views.ddelete,name='ddelete'),
    path('appointment/<int:id>/',views.appointment,name='appointment'),
    path('appsuccess/',views.appsuccess,name='appsuccess'),
    path('drpatient/',views.drpatient,name='drpatient'),
    path('docpro/',views.docpro,name='docpro'),
    path('docupd/',views.docupd,name='docupd'),
    path('doc/',views.pro_update,name='doc_update'),
    path('accept/<int:id>',views.accept, name='accept'),
    path('search/',views.search,name='search'),
    path('output/',views.output,name='output'),
    # path('result/',views.result,name='result'),


]
