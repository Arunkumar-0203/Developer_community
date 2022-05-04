from django.urls import path

from jobs.com_views import IndexView, PostJobView, Vacancy, ViewApplication, Confirm, ViewVacancyApp, \
    ConfirmVacancy, ViewWorkStatus, ViewEmployees, ComplaintViews,DownloadFile, give_link

urlpatterns = [

    path('',IndexView.as_view()),
    path('add_complaint',ComplaintViews.as_view()),
    path('post_job',PostJobView.as_view()),
    path('add_vacancy',Vacancy.as_view()),
    path('view_appoint',ViewApplication.as_view()),
    path('confirm',Confirm.as_view()),
    path('confirm_vacancy',ConfirmVacancy.as_view()),
    path('vacanncy_apponit',ViewVacancyApp.as_view()),
    path('view_work_status',ViewWorkStatus.as_view()),
    path('view_emplyees',ViewEmployees.as_view()),
    path('download',DownloadFile.as_view()),
    path('give_link',give_link.as_view()),


]
def urls():
    return urlpatterns,'company','company'