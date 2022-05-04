from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Developer_community import settings
from jobs.user_views import IndexView, ComplaintView, JobView, JobDetailsView, Vacancy, Appointment, VacancyDetails,AddWorkStatus, \
     ApplyVacancys, AddWorkStatusView, DownloadFile, user_profile, interview

urlpatterns = [

    path('',IndexView.as_view()),
    path('add_complaint',ComplaintView.as_view()),
    path('view_jobs',JobView.as_view()),
    path('job_details',JobDetailsView.as_view()),
    path('view_vacancy',Vacancy.as_view()),
    path('vacancy_details',VacancyDetails.as_view()),
    path('job_detail',Appointment.as_view()),
    path('add_workstatus',AddWorkStatusView.as_view()),
    path('vacancy_detail',ApplyVacancys.as_view()),
    path('download',DownloadFile.as_view()),
    path('user_profile',user_profile.as_view()),
    path('interview',interview.as_view()),



]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
def urls():
    return urlpatterns,'user','user'