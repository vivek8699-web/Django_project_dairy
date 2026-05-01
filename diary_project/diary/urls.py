from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("add-entry/", views.add_entry_view, name="add_entry"),
    path("delete-entry/<int:entry_id>/", views.delete_entry_view, name="delete_entry"),
    path("edit-entry/<int:entry_id>/", views.edit_entry_view, name="edit_entry"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)