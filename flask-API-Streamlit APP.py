# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:03:50 2024

@author: stacy
"""

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the cleaned data
data = pd.read_csv('C:/Users/stacy/Downloads/weather/Cleaned_GlobalWeatherRepository (1).csv')

@app.route('/weather_data', methods=['GET'])
def get_weather_data():
    return jsonify(data.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(port=5000)
    
    
    


