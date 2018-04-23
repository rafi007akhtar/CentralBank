from django.conf.urls import url
from . import views

app_name = "admins"

urlpatterns = [
    url(r"^$", views.index, name = "admin_index"),
]
