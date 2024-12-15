from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # ////////////////////ADMIN/////////////////////////
    path('addremoveclub/',addremoveclub.as_view(),name='addremoveclub'),
    path('addremovecollege/',addremovecollege.as_view(),name='addremovecollege'),
    path('collegeedit/<int:id>/',collegeedit.as_view(),name='collegeedit'),
    path('collegedelete/<int:id>/',Deletecollegetable.as_view(),name='collegedelete'),
    path('addremoveschool/',addremoveschool.as_view(),name='addremoveschool'),
    path('schooledit/<int:id>/',schooledit.as_view(),name='schooledit'),
    path('schooldelete/<int:id>/',Deleteschooltable.as_view(),name='schooldelete'),
    #//////////club///////////////
    path('clubedit/<int:id>/',clubedit.as_view(),name='clubedit'),
    path('clubhomepage/',clubhomepage.as_view(),name='clubhomepage'),
    path('clubregister/',register.as_view(),name='clubregister'),
    path('clubdelete/<int:id>/',Deleteclubtable.as_view(),name='clubdelete'),
    path('',login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('notification/',notification.as_view(),name='notification'),
    path('schooledit/',schooledit.as_view(),name='schooledit'),
    path('servicesbyclub/',servicesbyclub.as_view(),name='servicesbyclub'),
    path('viewservices/',viewservices.as_view(),name='viewservices'),
    path('viewactivities/',viewactivities.as_view(),name='viewactivities'),
    path('viewcomplaints/',viewcomplaints.as_view(),name='viewcomplaints'),
    path('viewuser/',View_user.as_view(),name='viewuser'),
    path('viewnotification/',View_notification.as_view(),name='viewnotification'),
    path('homepage/',homepage.as_view(),name='homepage'),
    path('rejectservices/<int:id>',rejectservices.as_view(),name='rejectservices'),
    path('acceptservices/<int:id>',acceptservices.as_view(),name='acceptservices'),

    


#//////////////CLUB///////////////

   path('viewfeedback/',viewfeedback.as_view(),name='viewfeedback'),
   path('viewreply/',viewreply.as_view(),name='viewreply'),
   path('viewinstruction/',viewinstruction.as_view(),name='viewinstruction'),


#////////////////////EVENT////////////

    path('feedback/',feedback.as_view(),name='feedback'),
    path('information/',information.as_view(),name='information'),
    
    path('register/',register.as_view(),name='register'),
]

