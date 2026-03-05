from django.shortcuts import render
from .models import Announcements
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from .forms import AnnouncementForm
from django.urls import reverse_lazy
class AnnouncementListView(ListView):
    model = Announcements
    template_name = 'Announcements/announcement_list.html'
    context_object_name = 'Announcements'
    
class AnnouncementDeteilView(DetailView):
    model = Announcements
    template_name = 'Announcements/announcement_detail.html'
    context_object_name = 'Announcement'
    
class AnnouncementCreateView(CreateView):
    model = Announcements
    template_name = 'Announcements/create_announcement.html'
    form_class = AnnouncementForm
    success_url = reverse_lazy("Announcement_List")
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class AnnouncementDeleteView(DeleteView):
    model = Announcements
    template_name = 'Announcements/delete_announcement.html'
    success_url = reverse_lazy("Announcement_List")
    
class AnnouncementUpdateView(UpdateView):
    model = Announcements
    template_name = 'Announcements/update_announcement.html'
    form_class = AnnouncementForm
    success_url = reverse_lazy("Announcement_List")