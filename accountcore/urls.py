from django.urls import path
from . import views
urlpatterns = [
    path("", views.GroupProfilrView.as_view(), name="GroupProfile"),
    path("profile/", views.UserProfileView.as_view(), name="UserProfile"),
    path("profileedit/", views.UserProfileUpdate.as_view(), name="ProfileEdit"),
    path("register/", views.UserRegister.as_view(), name="UserRegister"),
]