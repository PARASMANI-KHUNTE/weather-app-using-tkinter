import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    if city:
        # API endpoint and parameters
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,  # Get city name from entry widget
            "appid": "8c8b3ba834b5e7f54be59bf53d0b85dd",  # Your OpenWeatherMap API key
            "units": "metric"  # Set units to metric for Celsius
        }

        # Send GET request to the API
        response = requests.get(url, params=params)

        # Check if request was successful
        if response.status_code == 200:
            # Extract data from the response
            data = response.json()
            temperature = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            # Display the weather information
            result_label.config(text=f"Weather: {weather_desc}\nTemperature: {temperature}°C")
        else:
            # Display error message
            result_label.config(text="Error fetching weather data. Please try again later.")
    else:
        # Display error message if no city entered
        result_label.config(text="Please enter a city.")

root = tk.Tk()
root.title("Weather App")

# Styling
root.configure(background="#f0f0f0")
root.geometry("400x200")

title_label = tk.Label(root, text="Weather App", font=("Helvetica", 20), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City:", bg="#f0f0f0")
city_label.pack()

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather, bg="#4CAF50", fg="white")
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#f0f0f0")
result_label.pack()

root.mainloop()
