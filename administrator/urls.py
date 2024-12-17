from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # ////////////////////ADMIN/////////////////////////
    path('addremoveclub/',addremoveclub.as_view(),name='addremoveclub'),
    path('clubedit/',clubedit.as_view(),name='clubedit'),
    path('homepage/',homepage.as_view(),name='homepage'),
    path('login/',login.as_view(),name='login'),
    path('sendnotification/',sendnotification.as_view(),name='sendnotification'),
    path('servicesbyclub/',servicesbyclub.as_view(),name='servicesbyclub'),
    path('viewactivities/',viewactivities.as_view(),name='viewactivities'),
    path('viewcomplaints/',viewcomplaints.as_view(),name='viewcomplaints'),
    path('viewservices/',viewservices.as_view(),name='viewservices'),
    path('viewuser/',View_user.as_view(),name='viewuser'),
    


#//////////////CLUB///////////////
   path('clubhomepage/',clubhomepage.as_view(),name='clubhomepage'),
   path('clublogin/',clublogin.as_view(),name='clublogin'),
   path('studentregister/',studentregister.as_view(),name='studentregister'),
   path('sendcomplaints/',sendcomplaints.as_view(),name='sendcomplaints'),
   path('sendrequest/',sendrequest.as_view(),name='sendrequest'),
   path('viewfeedback/',viewfeedback.as_view(),name='viewfeedback'),
   path('viewnotification/',View_notification.as_view(),name='viewnotification'),
   path('Status/',Status.as_view(),name='status'),


#////////////////////CLUB COORDINATOR////////////

    path('add&managemembers/',addmanagemembers.as_view(),name='add&managemembers'),
    path('addevent/',addevent.as_view(),name='addevent'),
    path('addinstructions/',addinstructions.as_view(),name='addinstructions'), 
    path('coordinatorregister/',coordinatorregister.as_view(),name='coordinatorregister'),
    path('infromation/',information.as_view(),name='information'),
    path('notificationtable/',notificationtable.as_view(),name='notificationtable'),
    path('sendnotification/',sendnotification.as_view(),name='sendnotification'),
    path('viewcomplaints/',viewcomplaints.as_view(),name='viewcomplaints'),
    path('viewfeedback/',viewfeedback.as_view(),name='viewfeedback'),
    path('viewrequest/',viewrequest.as_view(),name='viewrequest'),
]