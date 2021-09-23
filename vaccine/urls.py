from django.urls import path

from .views import MemberListView, MemberDetailView, MemberDeleteView, FirstDoseView, SecondDoseView, DoseDoneView, LandingPageView, HomePage, DateDetails, Verify, CheckDate
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'vaccine'


urlpatterns = [

    path('', HomePage.as_view(), name='index'),
    path('check-date', CheckDate.as_view(), name='check-dates'),
    path('check-date/<pk>', DateDetails.as_view(), name='date-details'),

    path('verify', Verify.as_view(), name='verify'),
    path('login', LoginView.as_view(), name='login'),
    path('dashboard/logout', LogoutView.as_view(), name='logout'),

    path('dashboard/', MemberListView.as_view(), name='dashboard'),
    path('dashboard/first_dose', FirstDoseView.as_view(), name='first-dose'),
    path('dashboard/second_dose', SecondDoseView.as_view(), name='second-dose'),
    path('dashboard/complete_dose', DoseDoneView.as_view(), name='complete_dose'),
    path('dashboard/member/<pk>', MemberDetailView.as_view(), name='member-details'),
    path('dashboard/member/<pk>/delete', MemberDeleteView.as_view(), name='member-delete'),

]

urlpatterns += staticfiles_urlpatterns()
