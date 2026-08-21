from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        include("Care360_homepage_be.urls")
    ),

    path(
        "medicines/",
        include("medicines.urls")
    ),

    path(
        "emergency/",
        include("emergency.urls")
    ),

    path(
    "safety-care/",
    include("safetycare.urls")
),

]
