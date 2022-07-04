from django.shortcuts import render
from datetime import datetime


def landing(request):
    current_datetime = datetime.now()
    current_datetime_str = f"{current_datetime.year}-{current_datetime.month}-{current_datetime.day}"

    context = {
        "weather": "비",
        "temperature": 29,
        "weather_data": {
            "weather": "맑음",
            "temperature": 32,
        },
        "top_average": [
            "이정후", "강백호", "전준우", "A", "B"
        ],
        "top_hitters": [
            {
                "name": "이정후",
                "average": "0.350",
            },
            {
                "name": "강백호",
                "average": "0.349",
            },
            {
                "name": "전준우",
                "average": "0.348",
            },
        ],
        "now_data": current_datetime,
        "now_string": current_datetime_str
    }

    return render(request, "landing/index.html", context)


def base(request):
    return render(request, "base.html")


def extends(request):
    return render(request, "landing/extend.html")
