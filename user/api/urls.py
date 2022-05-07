from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user import views
from user.views import EmployerOnlyView, JobseekerOnlyView, JobseekerSignupView, EmployerSignupView, CustomAuthToken, LogoutView, JobseekerOnlyView, EmployerOnlyView, AdvertisementsView, JobseekersView, JobView

urlpatterns = [
    path('register/jobseeker/', JobseekerSignupView.as_view()),
    path('register/employer/', EmployerSignupView.as_view()),
    path('login/', CustomAuthToken.as_view(), name="auth_token"),
    path('logout/', LogoutView.as_view(), name="logout_view"),
    path('jobseeker/dashboard/', JobseekerOnlyView.as_view(), name="jobseeker_dashboard"),
    path('employer/dashboard/', EmployerOnlyView.as_view(), name="employer_dashboard"),
    path('add/', AdvertisementsView.as_view()),
    path('view/jobseekers', JobseekersView.as_view()),
    path('new/jobs',JobView.as_view()),
    # path('search/jobseekers', views.search_jobseeker(), name='search_jobseeker')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)