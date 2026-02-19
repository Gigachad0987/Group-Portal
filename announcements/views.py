from django.shortcuts import render
from .models import Announcements
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
class AnnouncementListView(ListView):
    model = Announcements
    template_name = 'announcement_list.html'
    
class AnnouncementDeteilView(DetailView):
    model = Announcements
    template_name = 'announcement_detail.html'
    context_object_name = 'Announcements'
    
class AnnouncementCreateView(CreateView):
    model = Announcements
    template_name = 'create_announcement.html'
    
class AnnouncementDeleteView(DeleteView):
    model = Announcements
    template_name = 'delete_announcement.html'
    
class AnnouncementUpdateView(UpdateView):
    model = Announcements
    template_name = 'update_announcement.html'