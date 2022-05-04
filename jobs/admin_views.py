from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView, View

# from jobs.models import
from jobs.models import companyegistration, usereegistration, Complaint, ViewAppont


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):


        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})
        # if user.is_staff == 1:
        #     return HttpResponseRedirect("newhostels",{'message':"Hostel Approved"})
        # else:
        #     return HttpResponseRedirect("newusers",{'message':"Hostel Approved"})


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})
        # if user.is_staff=='1':
        #     return HttpResponseRedirect("newhostels",{'message':"Hostel Approved"})
        # else:
        #     return HttpResponseRedirect("newusers",{'message':"Hostel Approved"})


class NewCompanyView(TemplateView):
    template_name = 'admin/appr_company.html'

    def get_context_data(self, **kwargs):
        context = super(NewCompanyView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        company = companyegistration.objects.filter(user__last_name='0',user__is_staff='0')
        # context['users'] = user
        context['company'] =  company
        return context

class NewUserView(TemplateView):
    template_name = 'admin/appr_user.html'

    def get_context_data(self, **kwargs):
        context = super(NewUserView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # users = User()
        user = usereegistration.objects.filter(user__last_name='0',user__is_staff='0')
        # context['users'] = user
        context['user'] =  user
        return context


class UsersView(TemplateView):
    template_name = 'admin/user_view.html'

    def get_context_data(self, **kwargs):
        context = super(UsersView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        users = usereegistration.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        # context['users'] = user
        context['user'] =  users
        return context

class CompanyView(TemplateView):
    template_name = 'admin/company_view.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        company = companyegistration.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        # context['users'] = user
        context['company'] =  company
        return context


class ComplaintView(TemplateView):
    template_name = 'admin/view_complaints.html'

    def get_context_data(self, **kwargs):
        context = super(ComplaintView,self).get_context_data(**kwargs)
        complaint = Complaint.objects.all()
        context['complaint'] =  complaint
        return context


