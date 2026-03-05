from django.urls import path
from announcements import views
urlpatterns = [
    path("announcement_detail/<int:pk>", views.AnnouncementDeteilView.as_view(), name = ("Announcement_Details")),
    path("announcement_list/", views.AnnouncementListView.as_view(), name = ("Announcement_List")),
    path("create_announcement/", views.AnnouncementCreateView.as_view(), name = ("Announcement_Create")),
    path("delete_announcement/<int:pk>", views.AnnouncementDeleteView.as_view(), name = ("Announcement_Delete")),
    path("update_announcement/<int:pk>", views.AnnouncementUpdateView.as_view(), name = ("Announcement_Update")),
]