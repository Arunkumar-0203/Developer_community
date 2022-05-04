from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import TemplateView, View

from jobs.download import download
from jobs.models import Complaint, PostJob, AddVacancy, ViewAppont, AddWorkStatus, ApplyVacancy, usereegistration


class IndexView(TemplateView):
    template_name = 'user/user_index.html'


class ComplaintView(TemplateView):
    template_name = 'user/add_complaint.html'
    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        complaint = Complaint()
        complaint.user = user
        complaint.complaint = request.POST['complaint']
        complaint.save()
        return redirect('/user/add_complaint')

class JobView(TemplateView):
    template_name = 'user/view_jobs.html'

    def get_context_data(self, **kwargs):
        context = super(JobView,self).get_context_data(**kwargs)
        post = PostJob.objects.filter(status='new')
        context['post'] =  post
        return context

class JobDetailsView(TemplateView):
    template_name = 'user/job_details.html'
    def get_context_data(self, **kwargs):
        context = super(JobDetailsView,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        details = PostJob.objects.get(pk=id)
        context['details'] =  details
        return context

class Vacancy(TemplateView):
    template_name = 'user/view_vacancy.html'

    def get_context_data(self, **kwargs):
        context = super(Vacancy,self).get_context_data(**kwargs)
        vacancy = AddVacancy.objects.filter(status='new')
        context['vacancy'] =  vacancy
        return context

class VacancyDetails(TemplateView):
    template_name = 'user/vacancy_details.html'
    def get_context_data(self, **kwargs):
        context = super(VacancyDetails,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        detail = AddVacancy.objects.get(pk=id)
        context['detail'] =  detail
        return context



class Appointment(TemplateView):
    template_name = 'user/job_details.html'
    def get_context_data(self, **kwargs):
        context = super(Appointment,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        user = User.objects.get(pk=self.request.user.id)
        job = PostJob.objects.get(pk=id)
        appl = ViewAppont()
        appl.job = job
        appl.user = user
        appl.status = 'apply'
        appl.save()
        return context


class AddWorkStatusView(TemplateView):
    template_name = 'user/add_workstatus.html'
    def post(self, request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        id = request.POST['jobs']
        job = PostJob.objects.get(pk=id)
        workdesc = request.POST['workdesc']
        ima = request.FILES['image']
        image = request.FILES['images']
        ad = AddWorkStatus()
        ad.users = user
        ad.status = 'Completed'
        ad.statusdesc = workdesc
        ad.jobs = job
        ad.image = ima
        ad.images = image
        ad.save()
        return redirect('/user/add_workstatus')
    def get_context_data(self, **kwargs):

        context = super(AddWorkStatusView,self).get_context_data(**kwargs)
        user = User.objects.get(id=self.request.user.id)
        pjob = ViewAppont.objects.filter(status='Confirm',user=user)
        context['pjob'] =  pjob
        return context


class ApplyVacancys(TemplateView):
    template_name = 'user/job_details.html'
    def get_context_data(self, **kwargs):
        context = super(ApplyVacancys,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        usereg =usereegistration.objects.get(user_id=self.request.user.id)
        user = User.objects.get(pk=self.request.user.id)
        vecan = AddVacancy.objects.get(pk=id)
        appl = ApplyVacancy()
        appl.vacancy = vecan
        appl.user_id = usereg.id
        appl.status = 'apply'
        appl.save()
        return context

class DownloadFile(View):
    def dispatch(self, request, *args, **kwargs):
        path = request.GET['path']
        download(request,path)
        return redirect('/user/job_detail')


class user_profile(TemplateView):
    template_name = 'user/edit_user_profile.html'
    def get_context_data(self, **kwargs):
        context = super(user_profile,self).get_context_data(**kwargs)
        id=self.request.user.id
        profile =usereegistration.objects.get(user_id=id)
        context['profile'] =  profile
        return context
    def post(self, request,*args,**kwargs):
        id=self.request.user.id
        user =User.objects.get(id=id)
        profile =usereegistration.objects.get(user_id=id)
        fullname = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        profile.address = address
        profile.contact = contact
        user.first_name=fullname
        user.email=email
        user.save()
        profile.save()
        messages = "update Successfully"
        return render(request,'user/user_index.html',{'messages':messages})

class interview(TemplateView):
    template_name ='user/interview.html'
    def get_context_data(self, **kwargs):
        context = super(interview,self).get_context_data(**kwargs)
        id=self.request.user.id
        user =usereegistration.objects.get(user_id=id)
        intervi =ApplyVacancy.objects.filter(user_id=user.id,status='apply')
        context['intervi'] =  intervi
        return context