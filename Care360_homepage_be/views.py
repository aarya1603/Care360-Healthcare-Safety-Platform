from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import os

from google import genai
from django.core.mail import send_mail

# ============================================================
# HOME PAGE
# ============================================================

def home(request):
    return render(
        request,
        "Care360.html"
    )


# ============================================================
# CONTACT PAGE
# ============================================================

def contact(request):
    return render(
        request,
        "contact.html"
    )

# ============================================================
# GAMES
# ============================================================

def games(request):
    return render(
        request,
        "care360_games.html"
    )


# ============================================================
# ROCK PAPER SCISSORS
# ============================================================

def rps(request):
    return render(
        request,
        "rps.html"
    )


# ============================================================
# SUDOKU
# ============================================================

def sudoku(request):
    return render(
        request,
        "sudoku.html"
    )


# ============================================================
# TIC TAC TOE
# ============================================================

def tictactoe(request):
    return render(
        request,
        "tictaktoe.html"
    )


# ============================================================
# GUESS THE NUMBER
# ============================================================

def guessthenum(request):
    return render(
        request,
        "guessthenum.html"
    )

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        rating = request.POST.get("rating")
        review = request.POST.get("review")


        # Create email message

        subject = "New Care360 Customer Review"

        message = f"""
New Care360 Customer Review
============================

Name:
{name}

Email:
{email}

Rating:
{rating}/5

Review:
{review}

============================
Sent from Care360
"""


        send_mail(

            subject,

            message,

            None,

            ["Care360.c@gmail.com"],

            fail_silently=False
        )


        return render(
            request,
            "contact.html",
            {
                "success": True
            }
        )


    return render(
        request,
        "contact.html"
    )
# ============================================================
# AI CHATBOT
# ============================================================
@csrf_exempt
def ai_chat(request):

    if request.method != "POST":
        return JsonResponse(
            {"reply": "Only POST requests are allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)

        message = data.get("message", "").strip()

        if not message:
            return JsonResponse(
                {"reply": "Please enter a message."},
                status=400
            )

        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            print("ERROR: GEMINI_API_KEY is missing")

            return JsonResponse(
                {"reply": "Gemini API key is not configured."},
                status=500
            )

        print("MESSAGE:", message)
        print("API KEY FOUND: YES")

        client = genai.Client(
            api_key=api_key
        )

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=message
        )

        reply = response.text

        print("GEMINI RESPONSE:", reply)

        return JsonResponse({
            "reply": reply
        })

    except Exception as e:

        print("\n==============================")
        print("GEMINI ERROR")
        print("==============================")
        print("ERROR TYPE:", type(e).__name__)
        print("ERROR:", str(e))
        print("==============================\n")

        return JsonResponse(
            {
                "reply": (
                    "AI Error: "
                    + type(e).__name__
                    + " - "
                    + str(e)
                )
            },
            status=500
        )
    