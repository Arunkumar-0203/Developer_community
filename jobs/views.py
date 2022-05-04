from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from jobs.models import usereegistration, UserType, companyegistration


class IndexView(TemplateView):
    template_name = 'index.html'

class UserReg(TemplateView):
    template_name = 'user_register.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        pin = request.POST['pin']
        address = request.POST['address']
        cv_docs= request.FILES['aaa']
        print(cv_docs)
        G = FileSystemStorage()
        CV = G.save(cv_docs.name, cv_docs)
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = usereegistration()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.pet = pin
             reg.cv_doc =CV
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "user"
             usertype.save()
             return redirect('user_register')
        except:
             messages = "Register Successfully"
             return render(request,'user_register.html',{'messages':messages})


class CompanyReg(TemplateView):
    template_name = 'company_register.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        pin = request.POST['pin']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = companyegistration()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.pet = pin
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "company"
             usertype.save()
             return redirect('company_register')
        except:
             messages = "Register Successfully"
             return render(request,'company_register.html',{'messages':messages})


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return redirect('/company')
            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})
