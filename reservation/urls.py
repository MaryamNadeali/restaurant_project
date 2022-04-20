from django.urls import path
from . import views
import reservation

app_name = "reservation"

urlpatterns = [
    path("",views.reserve,name="book"),
]
