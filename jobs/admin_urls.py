from django.urls import path

from jobs.admin_views import IndexView,ApproveView, RejectView, NewCompanyView, NewUserView, CompanyView, UsersView,ComplaintView


urlpatterns = [

    path('',IndexView.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('appr_company',NewCompanyView.as_view()),
    path('appr_user',NewUserView.as_view()),
    path('company_view',CompanyView.as_view()),
    path('user_view',UsersView.as_view()),
    path('view_complaints',ComplaintView.as_view()),



]
def urls():
      return urlpatterns,'admin','admin'
