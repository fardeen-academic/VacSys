from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse

from .models import Member
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, MemberUpdateForm


class LandingPageView(generic.TemplateView):
    template_name = 'vaccine/vaccine.html'


class MemberListView(LoginRequiredMixin, generic.ListView):
    template_name = "vaccine/dashboard.html"
    queryset = Member.objects.all()
    context_object_name = 'members'


class FirstDoseView(LoginRequiredMixin, generic.ListView):
    template_name = "vaccine/dashboard.html"
    queryset = Member.objects.filter(first_dose_done='False')
    context_object_name = 'members'


class SecondDoseView(LoginRequiredMixin, generic.ListView):
    template_name = "vaccine/dashboard.html"
    queryset = Member.objects.filter(first_dose_done='True', second_dose_done='False')
    context_object_name = 'members'


class DoseDoneView(LoginRequiredMixin, generic.ListView):
    template_name = "vaccine/dashboard.html"
    queryset = Member.objects.members = Member.objects.filter(first_dose_done='True', second_dose_done='True')
    context_object_name = 'members'


class MemberDetailView(LoginRequiredMixin, generic.UpdateView):
    template_name = "vaccine/member_details.html"
    form_class = MemberUpdateForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Member.objects.filter()

    def get_success_url(self):
        return reverse("vaccine:dashboard")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this lead")
        return super(MemberDetailView, self).form_valid(form)


class MemberDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'vaccine/delete.html'
    queryset = Member.objects.all()

    def get_success_url(self):
        return reverse('vaccine:dashboard')


class HomePage(generic.CreateView):
    template_name = 'vaccine/vaccine.html'
    form_class = RegisterForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Member.objects.filter()

    def get_success_url(self):
        return reverse("vaccine:index")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully registered for vaccine.")
        return super(HomePage, self).form_valid(form)


class CheckDate(generic.TemplateView):
    template_name = "vaccine/checkdate.html"


class DateDetails(generic.DetailView):
    queryset = Member.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Member.objects.filter()
    template_name = "vaccine/detailview.html"


class Verify(generic.DetailView):
    queryset = Member.objects.all()
    template_name = "vaccine/verify.html"



'''
def dashboard(request):
    members = Member.objects.all()
    context = {
        "members": members
    }
    return render(request, "vaccine/dashboard.html", context)


def member_details(request, pk):
    member = Member.objects.get(nid=pk)
    context = {
        "member": member
    }
    return render(request, "vaccine/member_details.html", context)


def first_dose(request):
    members = Member.objects.filter(first_dose_done='False')
    context = {
        "members": members
    }
    return render(request, "vaccine/first_dose.html", context)


def second_dose(request):
    members = Member.objects.filter(first_dose_done='True', second_dose_done='False')
    for member in members:
        if member.first_dose_done == "False" or member.second_dose_done == "True":
            members.delete()
    context = {
        "members": members
    }
    return render(request, "vaccine/second_dose.html", context)


def complete_dose(request):
    members = Member.objects.members = Member.objects.filter(first_dose_done='True', second_dose_done='True')
    context = {
        "members": members
    }
    return render(request, "vaccine/complete_dose.html", context)

'''