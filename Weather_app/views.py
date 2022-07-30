from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def weather_home(request):
    if request.method=="POST":

        city_name=request.POST.get("CITY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={str(city_name)}&appid=5506586ddd34ec74ad1bf32b8a54ed0d"
        res = requests.get(url)
        data = res.json()

        print(data)

    # dt_string = now.strftime("%B %d, %Y %H:%M:%S")
        if data["cod"] != "404":

            weather1 = int(data["main"]["temp"] - 273.15), int(data["main"]["temp_min"] - 273.15), int(
            data["main"]["temp_max"] - 273.15), data["main"]["feels_like"] - 273.15, data["main"][
                               "pressure"] - 273.15, data["weather"][0]["main"], data["weather"][0]["description"], \
                           data["main"]["humidity"], data["wind"]["speed"], data["name"]
            print(weather1[-1])
            return render(request,"details.html",{"Temperature":weather1[0],
                                                  "Max_temp":weather1[2],
                                                  "Min_temp":weather1[1],
                                                  "pressure":weather1[4],
                                                  "feeling_like":str(weather1[3])[0:6],
                                                  "Wind_speed":weather1[-2],
                                                  "Humidity":weather1[-3],
                                                  "Clouds":weather1[6],
                                                  "City":weather1[-1]




                                                  })
        else:
            return HttpResponse("<script>alert('please enter a valid city')</script>")

    return render(request,'weather_app.html')


