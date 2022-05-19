from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import TemplateView, View

from Developer_community import settings
from jobs.download import download
from jobs.models import Complaint, PostJob, AddVacancy, ViewAppont, ApplyVacancy, AddWorkStatus, usereegistration


class IndexView(TemplateView):
    template_name = 'company/com_index.html'

# class ComplaintView(TemplateView):
#     template_name = 'company/add_complaint.html'
#     def post(self,request,*args,**kwargs):
#         user = User.objects.get(id=self.request.user.id)
#         complaint = Complaint()
#         complaint.user = user
#         complaint.complaint = request.POST['complaints']
#         complaint.save()
#         return redirect('/company/add_complaints')

class PostJobView(TemplateView):
    template_name = 'company/post_job.html'
    def post(self, request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)

        email = request.POST['email']
        jobtitle = request.POST['jobtiltle']
        date = request.POST['Date']
        money = request.POST['money']
        language = request.POST['language']
        time = request.POST['time']
        jobdesc = request.POST['jobdesc']
        jobtype = request.FILES['image']
        companyname = request.POST['companyname']
        contact = request.POST['contact']
        address = request.POST['address']

        pro = PostJob()
        pro.user = user
        pro.email = email
        pro.jobtitle = jobtitle
        pro.jobdesc = jobdesc
        pro.date = date
        pro.language = language
        pro.time = time
        pro.money = money
        pro.images = jobtype
        pro.companyname = companyname
        pro.status = 'new'
        pro.contact = contact
        pro.address = address
        pro.save()
        return redirect('/company/post_job')

class ComplaintViews(TemplateView):
    template_name = 'company/add_complaints.html'
    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        complaints = Complaint()
        complaints.user = user
        complaints.complaint = request.POST['complaint']
        complaints.save()
        return redirect('/company/add_complaint')



class Vacancy(TemplateView):
    template_name = 'company/add_vacancy.html'
    def post(self, request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)

        jobtype = request.POST['jobtype']
        date = request.POST['date']
        Quali = request.POST['quali']
        salary = request.POST['salary']
        jobdesc = request.POST['desc']

        add = AddVacancy()
        add.user = user
        add.jobtype = jobtype
        add.deadline = date
        add.salary = salary
        add.qualification = Quali
        add.jobdesc = jobdesc
        add.status = 'new'
        add.save()
        return redirect('/company/add_vacancy')

class ViewApplication(TemplateView):
    template_name = 'company/view_appoint.html'

    def get_context_data(self, **kwargs):
        context = super(ViewApplication,self).get_context_data(**kwargs)
        # id = self.request.GET['id']
        print(self.request.user.id)
        user = User.objects.get(pk=self.request.user.id)
        companayappont = ViewAppont.objects.filter(job__user=user,status='apply')
        context['companayappont'] =  companayappont
        return context


class ViewVacancyApp(TemplateView):
    template_name = 'company/vacanncy_apponit.html'

    def get_context_data(self, **kwargs):
        context = super(ViewVacancyApp,self).get_context_data(**kwargs)
        # id = self.request.GET['id']
        user = User.objects.get(pk=self.request.user.id)
        appont = ApplyVacancy.objects.filter(vacancy__user=user,status='apply')
        context['appont'] =  appont
        return context


class Confirm(View):

    def get(self, request, *args, **kwargs):
        id = self.request.GET['id']
        # user = User.objects.get(pk=self.request.user.id)
        appo = ViewAppont.objects.get(pk=id)
        appo.status = 'Confirm'
        appo.save()

        # post = ViewAppont.objects.get(job=id)
        jobs = PostJob.objects.get(pk=appo.job.id)
        jobs.status = 'Confirm'
        jobs.save()
        return  redirect('/company/view_appoint')

class ConfirmVacancy(View):

    def get(self, request, *args, **kwargs):
        id = self.request.GET['id']
        print(id)
        # user = User.objects.get(pk=self.request.user.id)
        appo = ApplyVacancy.objects.get(id=id)
        appo.status = 'confirm'
        appo.save()
        cv_doc=appo.user.cv_doc
        # post = ViewAppont.objects.get(job=id)
        vacan = AddVacancy.objects.get(pk=appo.vacancy.id)
        vacan.status = 'confirm'
        vacan.save()
        email = EmailMessage(
        'your appointed',
        'join with in 3 days',
        settings.EMAIL_HOST_USER,
        [appo.user.user.email],
         )
        email.fail_silently = False
        email.send()
        return redirect(request.META['HTTP_REFERER'])


class ViewWorkStatus(TemplateView):
     template_name = 'company/view_workstatus.html'

     def get_context_data(self, **kwargs):
        context = super(ViewWorkStatus,self).get_context_data(**kwargs)
        # id = self.request.GET['id']
        user = User.objects.get(pk=self.request.user.id)
        appont = AddWorkStatus.objects.filter(status='Completed',jobs__user=user)
        context['appont'] =  appont
        return context

class ViewEmployees(TemplateView):
     template_name = 'company/view_emplyees.html'

     def get_context_data(self, **kwargs):
        context = super(ViewEmployees,self).get_context_data(**kwargs)
        # id = self.request.GET['id']
        user = User.objects.get(pk=self.request.user.id)
        u=AddVacancy.objects.filter(user_id=user.id)
        appont = ApplyVacancy.objects.filter(status='Confirm',company_id=user.id)
        print("55555555555",appont)
        context['appont'] =  appont
        return context

class DownloadFile(View):
    def dispatch(self, request, *args, **kwargs):
        path = request.GET['path']
        download(request,path)
        return redirect('/company/view_work_status')



class give_link(TemplateView):
    template_name = 'company/give_link.html'
    def post(self, request,*args,**kwargs):
        id = self.request.GET['id']
        user = User.objects.get(pk=self.request.user.id)
        appont = ApplyVacancy.objects.filter(vacancy__user=user,status='apply')
        ApplyVacancys =ApplyVacancy.objects.get(id=id)
        date =request.POST['date']
        time=request.POST['time']
        link=request.POST['link']
        ApplyVacancys.date=date
        ApplyVacancys.time=time
        ApplyVacancys.link=link
        ApplyVacancys.save()
        messages ="Link uploaded successfully"
        return render(request,'company/vacanncy_apponit.html',{'messages':messages,'appont':appont})