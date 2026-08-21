from django.shortcuts import render, redirect
from .models import EmergencyContact

def emergency(request):

    contacts = EmergencyContact.objects.all().order_by("-id")

    print("EMERGENCY CONTACT COUNT:", contacts.count())
    print("EMERGENCY CONTACTS:", list(
        contacts.values("name", "relationship", "phone")
    ))

    return render(
        request,
        "emergency.html",
        {
            "emergency_contacts": contacts
        }
    )


def add_emergency_contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        relationship = request.POST.get("relationship")
        phone = request.POST.get("phone")

        if name and relationship and phone:

            EmergencyContact.objects.create(
                name=name,
                relationship=relationship,
                phone=phone
            )

        return redirect("emergency")

    return render(
        request,
        "add_emergency_contact.html"
    )