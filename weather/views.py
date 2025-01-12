from django.shortcuts import render
import requests

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "fcc3b6b33d89d96dba7f76fbfd8c2920"
icon_url = "https://openweathermap.org/img/wn/{}@2x.png"

def get_weather(city):
    params = {"q": city, "appid": api_key, "lang": "en"}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code != 200 or "name" not in data:
            return None
        city = data["name"].capitalize()
        country = data["sys"]["country"]
        temp = int(data["main"]["temp"] - 273.15) 
        icon = data["weather"][0]["icon"]
        condition = data["weather"][0]["description"]
        
        return {
            "city": city,
            "country": country,
            "temp": temp,
            "icon": icon_url.format(icon),
            "condition": condition
        }
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

def weather_view(request):
    city = request.GET.get("city", "").strip() 
    weather_data = None

    if city:
        weather_data = get_weather(city)
    
    return render(request, "weather/weather.html", {"weather_data": weather_data})
