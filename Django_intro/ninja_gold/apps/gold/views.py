from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random
import datetime

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
        request.session["activity"] = []
    return render(request, "gold/index.html")


def process_money(request):
    location = request.POST["building"]
    if request.method == "POST":
        if location == "farm":
            money = random.randrange(10, 21) + int(request.session["gold"])
            request.session["gold"] = money
        elif location == "cave":
            money = random.randrange(5, 11)
            request.session["gold"] += money
        elif location == "house":
            money = random.randrange(2, 6)
            request.session["gold"] += money
        elif location == "casino":
            money = random.randrange(-50, 51)
            request.session["gold"] += money
        if money < 0:
            money *= -1
            color = "text-danger"
            outcome = "lost"
            date_time = str(datetime.datetime.now())
            activity = request.session["activity"]
            activity.append(
                {
                    "location": location,
                    "money": money,
                    "color": color,
                    "outcome": outcome,
                    "date_time": date_time,
                }
            )
            request.session["activity"] = activity
        else:
            color = "text-success"
            outcome = "won"
            date_time = str(datetime.datetime.now())
            activity = request.session["activity"]
            activity.append(
                {
                    "location": location,
                    "money": money,
                    "color": color,
                    "outcome": outcome,
                    "date_time": date_time,
                }
            )
            request.session["activity"] = activity
    print(request.session["gold"])
    return redirect("/")

