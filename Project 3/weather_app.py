## Simple Beginner friendly code wih great GUI
import tkinter as tk
from tkinter import messagebox
import requests

# ✅ Replace with your own API key from weatherapi.com
API_KEY = "25b0f4fe4f2546938c770815251203"
BASE_URL = "https://api.weatherapi.com/v1/current.json?"

recent_searches = []

def get_weather():
    """Fetches weather data from WeatherAPI and updates UI."""
    city_name = city_entry.get().strip()

    if not city_name:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    complete_url = BASE_URL + "key=" + API_KEY + "&q=" + city_name

    try:
        response = requests.get(complete_url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", f"City not found! {data['error']['message']}")
            result_label.config(text="")
        else:
            current_temperature = data["current"]["temp_c"]
            current_pressure = data["current"]["pressure_mb"]
            current_humidity = data["current"]["humidity"]
            weather_description = data["current"]["condition"]["text"]

            weather_text = (
                f"City: {city_name}\n"
                f"Temperature: {current_temperature}°C\n"
                f"Pressure: {current_pressure} mb\n"
                f"Humidity: {current_humidity}%\n"
                f"Description: {weather_description}"
            )

            result_label.config(text=weather_text)
            update_recent_searches(weather_text)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_recent_searches(weather_text):
    """Updates the UI with the last 5 searches."""
    recent_searches.append(weather_text)
    recent_label.config(text="\n\n".join(recent_searches[-5:]))

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather Application by AD")
root.geometry("650x700")

tk.Label(root, text="Weather App by A_D", fg="brown", font=("Times New Roman", 30, "bold", "italic"),
         borderwidth=1, relief="groove").pack(pady=20)

tk.Label(root, text="Enter City Name:", font=("Arial", 20), fg="gold", borderwidth=1,
         relief="sunken").pack(pady=5)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather,
                                borderwidth=1, relief="raised", fg="purple")
get_weather_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left", fg="blue")
result_label.pack(pady=10)

tk.Label(root, text="Recent Searches:", font=("Arial", 14, "bold")).pack(pady=5)
recent_label = tk.Label(root, text="", font=("Arial", 12), justify="left", fg="darkgreen")
recent_label.pack(pady=10)

root.mainloop()


## For improving it to advance, I have added the database below :-

import tkinter as tk
from tkinter import messagebox
import requests
import sqlite3

# ✅ Replace with your own API key from weatherapi.com
API_KEY = "25b0f4fe4f2546938c770815251203"
BASE_URL = "https://api.weatherapi.com/v1/current.json?"

recent_searches = []

def setup_database():
    """Creates the weather database if not exists."""
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            pressure INTEGER,
            humidity INTEGER,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_weather():
    """Fetches weather data from WeatherAPI and updates UI."""
    city_name = city_entry.get().strip()
    
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    complete_url = BASE_URL + "key=" + API_KEY + "&q=" + city_name
    
    try:
        response = requests.get(complete_url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", f"City not found! {data['error']['message']}")
            result_label.config(text="")
        else:
            current_temperature = data["current"]["temp_c"]
            current_pressure = data["current"]["pressure_mb"]
            current_humidity = data["current"]["humidity"]
            weather_description = data["current"]["condition"]["text"]

            global recent_weather_data
            recent_weather_data = (city_name, current_temperature, current_pressure, current_humidity, weather_description)

            weather_text = (
                f"City: {city_name}\n"
                f"Temperature: {current_temperature}°C\n"
                f"Pressure: {current_pressure} mb\n"
                f"Humidity: {current_humidity}%\n"
                f"Description: {weather_description}"
            )

            result_label.config(text=weather_text)
            save_to_database()
            update_recent_searches(weather_text)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_recent_searches(weather_text):
    recent_searches.append(weather_text)
    recent_label.config(text="\n\n".join(recent_searches[-5:]))

def save_to_database():
    if recent_weather_data:
        conn = sqlite3.connect("weather_data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO weather (city, temperature, pressure, humidity, description) VALUES (?, ?, ?, ?, ?)", recent_weather_data)
        conn.commit()
        conn.close()

# GUI setup
root = tk.Tk()
root.title("Weather Application by AD")
root.geometry("650x700")

setup_database()

tk.Label(root, text="Weather App by A_D", fg="brown", font=("Times New Roman", 30, "bold", "italic"), borderwidth=1, relief="groove").pack(pady=20)
tk.Label(root, text="Enter City Name:", font=("Arial", 20), fg="gold", borderwidth=1, relief="sunken").pack(pady=5)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather, borderwidth=1, relief="raised", fg="purple")
get_weather_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left", fg="blue")
result_label.pack(pady=10)

tk.Label(root, text="Recent Searches:", font=("Arial", 14, "bold")).pack(pady=5)
recent_label = tk.Label(root, text="", font=("Arial", 12), justify="left", fg="darkgreen")
recent_label.pack(pady=10)

root.mainloop()


