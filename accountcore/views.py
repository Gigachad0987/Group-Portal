from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView
from .models import UserProfile, GroupProfile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
class GroupProfilrView(DetailView):
    model = GroupProfile
    template_name = "accountscore/GroupProfile.html"
    context_object_name = "GroupProfile"
    def get_object(self):
        return GroupProfile.objects.first()
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context
    
class UserProfileView(DetailView):
    model = UserProfile
    template_name = "accountscore/UserProfile.html"
    context_object_name = "UserProfile"
    def get_object(self):
        return self.request.user.profile
    
class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ["avatar", "bio"]
    template_name = "accountscore/ProfileEdit.html"
    success_url = reverse_lazy("UserProfile")
    def get_object(self):
        return self.request.user.profile
    
class UserRegister(CreateView):
    model = User
    template_name = "accountscore/register.html"
    form_class = UserRegisterform
    succsess_url = reverse_lazy("UserProfile")