from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.emergency,
        name="emergency"
    ),

    path(
        "add-contact/",
        views.add_emergency_contact,
        name="add_emergency_contact"
    ),

]