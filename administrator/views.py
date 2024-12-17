from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from administrator.form import *
from .models import *

# Create your views here.

# //////////////////////////////// ADMIN ////////////////////////////////////
class login(View):
    def get(self,request):
        return render(request,'administrator/login.html')
    def post(self,request):
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)

        login_obj = LoginTable.objects.get(username=username,password=password)

        if login_obj.usertype=="admin":
            return HttpResponse('''<script>alert("welcome to admin home");window.location="/homepage/"</script>''')
        elif login_obj.usertype=="clubs":
            return HttpResponse('''<script>alert("welcome to clubs home");window.location="/clubhomepage/"</script>''')
        
class Logout(View):
     def get(self,request):
         return HttpResponse('''<script>alert("Logout Successfully");window.location="/"</script>''')
        

class homepage(View):
    def get(self,request):
        return render(request,'administrator/homepage.html') 
      

class addremoveclub(View):
    def get(self,request):
        obj=clubtable.objects.all()
        print(obj)
        return render(request,'administrator/addremoveclub.html',{'val':obj})
    def post(self,request):
        form=clubform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("ADDED");window.location="/addremoveclub/"</script>''')    
        return HttpResponse('''<script>alert("FAILED");window.location="/addremoveclub/"</script>''')
    
class clubedit(View):
    def get(self,request,id):
        obj=clubtable.objects.get(id=id)
        return render(request,'administrator/clubedit.html',{'val':obj})
    def post(self,request,id):
        obj = clubtable.objects.get(id=id)
        print("obj")
        form = Updateclubform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("UPDATED");window.location="/addremoveclub/"</script>''')
    
class Deleteclubtable(View):
    def get(self,request,id):
        obj=clubtable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("DELETED");window.location="/addremoveclub"</script>''')     

class clubhomepage(View):
    def get(self,request):
        return render(request,'clubs/clubhomepage.html') 

                                       
        
class sendnotification(View):
    def get(self,request):
        obj=User.objects.all()
        abc=event.objects.all()
        return render(request, 'administrator/sendnotification.html', {'val': obj, 'val2': abc})
    def post(self,request):
        form=notificationform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("ADDED");window.location="/viewnotification/"</script>''')

 
class View_notification(View):
    def get(self, request):
        obj = notificationtable.objects.all()
        return render(request, 'event/notificationtable.html',{'obj':obj})


class servicesbyclub(View):
    def get(self,request):
        obj = servicetable.objects.all()
        return render(request,'administrator/servicesbyclub.html',{'obj':obj})

class viewservices(View):
    def get(self,request):
        obj = servicetable.objects.filter(status='Accepted')
        return render(request, 'administrator/viewservices.html',{'obj':obj})
class acceptservices(View):
    def get(self,request,id):
        obj = servicetable.objects.get(id=id)
        obj.status = 'Accepted'
        obj.save()
        return redirect('servicesbyclub')
    
class rejectservices(View):
    def get(self,request,id):
        obj = servicetable.objects.get(id=id)
        obj.status = 'Rejected'
        obj.save()
        return redirect('servicesbyclub')
        
class viewactivities(View):
    def get(self,request):
        obj = activities.objects.all()
        return render(request,'administrator/viewactivities.html', {'val':obj})
class viewcomplaints(View):
    def get(self,request):
        obj = complaints.objects.all()
        return render(request,'administrator/viewcomplaints.html',{'val':obj})
    

class View_user(View):
    def get(self, request):
        obj = User.objects.all()
        return render(request, 'administrator/viewuser.html', {'val':obj})
    def post(self, request):
        name=request.POST('name')
        obj1=User.objects.filter(name=name)
        print(obj1)
        return render(request,'administrator/viewuser.html', {'val1':obj1})

# ////////////////////////// club//////////////
class clubhomepage(View):
    def get(self,request):
        return render(request,'clubs/clubhomepage.html') 
    
class clublogin(View):
    def get(self,request):
        return render(request,'clubs/clublogin.html')
    
class sendrequest(View):
    def get(self,request):
        return render(request,'clubs/sendrequest.html') 
    

class sendcomplaints(View):
    def get(self,request):
        return render(request,'clubs/sendcomplaints.html') 
    
    
      
class studentregister(View):
    def get(self,request):
        return render(request,'clubs/studentregister.html')
    def post(self,request):
        form=ClubRegistrartionForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            obj = LoginTable()
            obj.username=request.POST['username']
            obj.password=request.POST['password']
            obj.type = "pending"
            obj.save()
            f.LOGIN_ID=obj
            f.save()
            return HttpResponse('''<script>alert("ADDED");window.location="/"</script>''')

    
class viewnotificasion(View):
    def get(self,request):
        return render(request,'clubs/viewnotification.html')
    
class viewfeedback(View):
    def get(self,request):
        return render(request,'clubs/viewfeedback.html')
    
class Status(View):
     def get(self,request):
        return render(request,'clubs/addinstructions.html')


#////////////////CLUB COORDINATOR/////////////
class addmanagemembers(View):
    def get(self,request):
        return render(request,'Club coordinator/addmanagemembers.html')
    
class addevent(View):
    def get(self,request):
        return render(request,'Club coordinator/addevent.html')
    
class addinstructions(View):
    def get(self,request):
        return render(request,'Club coordinator/addinstructions.html')
    
class coordinatorregister(View):
    def get(self,request):
        return render(request,'Club coordinator/coordinatorregister.html')

class information(View):
    def get(self,request):
        return render(request,'Club coordinator/information.html')
    
class notificationtable(View):
    def get(self,request):
        return render(request,'Club coordinator/notificationtable.html')
    
class sendnotification(View):
    def get(self,request):
        return render(request,'Club coordinator/sendnotification.html')
    
class viewcomplaints(View):
    def get(self,request):
        return render(request,'Club coordinator/viewcomplaints.html')



class viewfeedback(View):
    def get(self,request):
        return render(request,'Club coordinator/viewfeedback.html')
    
class viewrequest(View):
    def get(self,request):
        return render(request,'Club coordinator/viewrequest.html')


    





