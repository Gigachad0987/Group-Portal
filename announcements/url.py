from django.urls import path
from announcements import views
urlpatterns = [
    path("announcement_detail/", views.AnnouncementDeteilView.as_view(), name = ("Announement_Details")),
    path("announcement_list/", views.AnnouncementListView.as_view(), name = ("Announement_List")),
    path("create_announcement/", views.AnnouncementCreateView.as_view(), name = ("Announement_Create")),
    path("delete_announcement/", views.AnnouncementDeleteView.as_view(), name = ("Announement_Delete")),
    path("update_announcement/", views.AnnouncementUpdateView.as_view(), name = ("Announement_Update")),
]