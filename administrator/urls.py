from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # ////////////////////ADMIN/////////////////////////
    path('login/',login.as_view(),name='login'),
    path('login/',Logout.as_view(),name='login'),
    path('viewevent/',viewevent.as_view(),name='viewevent'),
    path('viewstudent/',viewstudents.as_view(),name='viewstudents'),
    path('viewcomplaints/',viewcomplaints.as_view(),name='viewcomplaints'),
    path('sendreply/',sendreply.as_view(),name='sendreply'),
    path('sendnotification/',sendnotification.as_view(),name='sendnotification'),
    path('acceptevent/',acceptevent.as_view(),name='acceptevent'),
    path('rejectevent/',rejectevent.as_view(),name='rejectevent'),
    path('viewfeedback/',viewfeedback.as_view(),name='viewfeedback'),
    path('homepage/',homepage.as_view(),name='homepage'),
    
    


#////////////////////CLUB COORDINATOR////////////

    path('eventregister/',eventregister.as_view(),name='eventregister'),
    path('sendcomplaints/',sendcomplaints.as_view(),name='sendcomplaints'),
    path('viewreply/',viewreply.as_view(),name='viewreply'),
    path('addormanageevent/',addormanageevent.as_view(),name='addormanageevent'),
    path('Deleteeventtable/',Deleteeventtable.as_view(),name='Deleteeventtable'),
    path('addormanageinstruction/',addormanageinstruction.as_view(),name='addormanageinstruction'),
    path('Deleteinstruction/',Deleteinstruction.as_view(),name='Deleteinstruction'),
    path('acceptstudent/',acceptstudent.as_view(),name='acorrejstudent'),
    path('rejectstudentt/',rejectstudent.as_view(),name='acorrejstudent'),
    path('addgallery/',addgallery.as_view(),name='addgallery'),
    path('Deletegallery/',Deletegallerytable.as_view(),name='addgallery'),
    path('Studentsofevent/',Studentsofevent.as_view(),name='listofevent'),
    path('Listofstudent/',Listofstudent.as_view(),name='Listofstudent'),

    ]