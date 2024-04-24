from django.urls import path
from . import views
urlpatterns=[
    path('',views.test),
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('add',views.add),
    path('insert',views.insert),
    path('ins',views.ins),
    path('student',views.insert_2),
    path('ins2',views.ins2),
    path('show',views.show),
    path('show2',views.show2),
    path('del/<int:id>',views.dele), #dynamic url
    path('edit/<int:id>',views.edit),
    path('upd/<int:id>',views.upd),
    path('edit2/<int:id>', views.edit2),
    path('upd2/<int:id>', views.upd2),
    path('upload',views.upload),
    path('upld',views.upld),
    path('fpic',views.fpic),
    path('login',views.login),
    path('log',views.log),

]