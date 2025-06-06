# 🌦️ Weather App GUI (Python + Tkinter + SQLite)

This is a GUI-based Weather App that allows users to check real-time weather using the WeatherAPI. It displays temperature, humidity, pressure, and a short description. Recent searches are stored in an SQLite database and shown on screen.

---

## 💡 Features

- GUI Interface (Tkinter)
- Real-time weather data using WeatherAPI
- Weather details: temperature, pressure, humidity, condition
- Input validation and error messages
- SQLite database for storing search history
- Recent 5 searches shown on UI

---

## 📸 Screenshot
---
![p3 1](https://github.com/user-attachments/assets/a24336d0-dc99-4101-8e70-e5da3ae7634c)

---
![p3 2](https://github.com/user-attachments/assets/8cf2b841-6769-4e24-9a8f-0c1057df70b7)

---
![p3 3](https://github.com/user-attachments/assets/6ad04a2e-38f2-4ec6-b00f-6ce510899398)

---

## 🚀 Getting Started
### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Weather-App-GUI.git
cd Weather-App-GUI
```
### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
---
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
---
### 4. Get WeatherAPI Key
- Sign up at https://www.weatherapi.com

- Replace the API key in the script:
```python
API_KEY = "your_actual_api_key"
```
---
### 5. Run the App
```bash
python weather_app.py
```

### 🛠️ Tools Used
- Python 3.x
- Tkinter (GUI)
- SQLite3
- WeatherAPI (API)
- Requests library
