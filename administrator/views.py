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

class addremovecollege(View):
    def get(self,request):
        obj=collegetable.objects.all()
        print(obj)
        return render(request,'administrator/addremovecollege.html',{'val':obj})
    def post(self,request):
        form=collegeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("ADDED");window.location="/addremovecollege/"</script>''')    
        return HttpResponse('''<script>alert("FAILED");window.location="/addremovecollege/"</script>''')
    
class collegeedit(View):
    def get(self,request,id):
        obj=collegetable.objects.get(id=id)
        return render(request,'administrator/collegeedit.html',{'val':obj})
    def post(self,request,id):
        obj = collegetable.objects.get(id=id)
        print("obj")
        form = Updatecollegeform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("UPDATED");window.location="/addremovecollege/"</script>''')
    
class Deletecollegetable(View):
    def get(self,request,id):
        obj=collegetable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("DELETED");window.location="/addremovecollege"</script>''')      
                                       
        
 
class addremoveschool(View):
   def get(self,request): 
        obj=schooltable.objects.all()
        print(obj)
        return render(request,'administrator/addremoveschool.html',{'val':obj})
   def post(self,request):
        form=schoolform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("ADDED");window.location="/addremoveschool/"</script>''')    
        return HttpResponse('''<script>alert("FAILED");window.location="/addremoveschool/"</script>''')

class schooledit(View):
    def get(self,request,id):
        obj=schooltable.objects.get(id=id)
        return render(request,'administrator/schooledit.html',{'val':obj})
    def post(self,request,id):
        obj = schooltable.objects.get(id=id)
        print(obj)
        form = Updateschoolform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("UPDATED");window.location="/addremoveschool/"</script>''')
    
class Deleteschooltable(View):
    def get(self,request,id):
        obj=schooltable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("DELETED");window.location="/addremoveschool"</script>''')      
                                       
        
class notification(View):
    def get(self,request):
        obj=User.objects.all()
        abc=event.objects.all()
        return render(request, 'administrator/notification.html', {'val': obj, 'val2': abc})
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
class viewfeedback(View):
     def get(self,request):
        obj = feedback.objects.all()
        return render(request,'administrator/viewfeedback.html',{'val':obj})

# ////////////////////////// club//////////////
class register(View):
    def get(self,request):
        return render(request,'clubs/register.html')
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


class viewinstruction(View):
    def get(self,request):
        return render(request,'clubs/addinstructions.html')
class viewreply(View):
    def get(self,request):
        return render(request,'clubs/viewreply.html')
class viewfeedback(View):
    def get(self,request):
        return render(request,'clubs/viewfeedback.html')

#////////////////EVENT/////////////
class feedback(View):
    def get(self,request):
        return render(request,'event/feedback.html')
class information(View):
    def get(self,request):
        return render(request,'event/information.html')


    





