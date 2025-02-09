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

        login_obj = LoginTable.objects.get(username=username,password=password,status='accept')

        if login_obj.usertype=="admin":
            return HttpResponse('''<script>alert("welcome to admin home");window.location="/homepage/"</script>''')
        elif login_obj.usertype=="clubs":
            return HttpResponse('''<script>alert("welcome to clubs home");window.location="/clubhomepage/"</script>''')
        
class Logout(View):
     def get(self,request):
         return HttpResponse('''<script>alert("Logout Successfully");window.location="/"</script>''')
class viewevent(View):
    def get(self, request):
        obj = eventtable.objects.all()
        return render(request, 'administrator/viewevent.html',{'obj':obj})

class viewstudents(View):
    def get(self,request):
        obj = studentstable.objects.filter(status='Accepted')
        return render(request, 'administrator/viewstudents.html',{'obj':obj})        
class viewcomplaints(View):
    def get(self,request):
        obj = complaints.objects.all()
        return render(request,'administrator/viewcomplaints.html',{'val':obj})
class sendreply(View):
    def get(self,request):
        return render(request,'administrator/sentreply.html') 
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
class acceptevent(View):
    def get(self,request,id):
        obj = User.objects.get(id=id)
        c=EventTable.objects.get(id=obj.id)
        c.status = 'accept'
        c.save()
        return redirect('viewevent')
    
class rejectevent(View):
    def get(self,request,id):
        obj = User.objects.get(id=id)
        c=EventTable.objects.get(id=obj.id)
        c.status = 'reject'
        c.save()
        return redirect('viewevent')
class viewfeedback(View):
    def get(self,request):
        return render(request,'administrator/viewfeedback.html')
    
class homepage(View):
    def get(self,request):
        return render(request,'administrator/homepage.html') 
      
# ////////////////////////// clubcoordinator//////////////
class eventregister(View):
    def get(self,request):
        return render(request,'clubcoordinator/eventregister.html')
    def post(self,request):
        form=EventRegisterForm(request.POST)
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
class sendcomplaints(View):
    def get(self,request):
        return render(request,'clubcoordinator/sendcomplaints.html') 
class viewreply(View):
    def get(self,request):
        return render(request,'clubs/viewreply.html')

class addormanageevent(View):
    def get(self,request,id):
        obj=eventtable.objects.get(id=id)
        return render(request,'clubcoordinator/addormanageevent.html',{'val':obj})
    def post(self,request,id):
        obj = eventtable.objects.get(id=id)
        print("obj")
        form = Updateeventform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("UPDATED");window.location="/addormanageevent/"</script>''')
    
class Deleteeventtable(View):
    def get(self,request,id):
        obj=clubtable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("DELETED");window.location="/addormanageevent/"</script>''')     

class addormanageinstruction(View):
    def get(self,request,id):
        obj=instructiontable.objects.get(id=id)
        return render(request,'clubcoordinator/addormanageinstruction.html',{'val':obj})
    def post(self,request,id):
        obj = instructiontable.objects.get(id=id)
        print("obj")
        form = Updateinstructionform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("UPDATED");window.location="/addormanageinstruction/"</script>''')
    
class Deleteinstruction(View):
    def get(self,request,id):
        obj=instructiontable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("DELETED");window.location="/addormanageinstruction/"</script>''')   
class Deleteinstruction(View):
    def get(self,request,id):
        obj = User.objects.get(id=id)
        c=LoginTable.objects.get(id=obj.id)
        c.status = 'accept'
        c.save()
        return redirect('addormanageinstruction')
class acceptstudent(View):
    def get(self,request,id):
        obj = User.objects.get(id=id)
        c=LoginTable.objects.get(id=obj.id)
        c.status = 'accept'
        c.save()
        return redirect('viewstudent')
    
class rejectstudent(View):
    def get(self,request,id):
        obj = User.objects.get(id=id)
        c=LoginTable.objects.get(id=obj.id)
        c.status = 'reject'
        c.save()
        return redirect('viewstudent')
class addgallery(View):
    def get(self,request,id):
        obj=gallerytable.objects.get(id=id)
        return render(request,'clubcoordinator/addgallery.html',{'val':obj})
    def post(self,request,id):
        obj = gallerytable.objects.get(id=id)
        print("obj")
        form = Updategalleryform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("UPDATED");window.location="/addgallery/"</script>''')
class Deletegallerytable(View):
    def get(self,request,id):
        obj=gallerytable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("DELETED");window.location="/addgallery/"</script>''')    
class Studentsofevent(View):
    def get(self,request):
        return render(request,'Club coordinator/listofevent.html')
class Listofstudent(View):
    def get(self,request):
        return render(request,'Club coordinator/listofstudent.html')


    





