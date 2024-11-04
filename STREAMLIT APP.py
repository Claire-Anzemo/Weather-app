# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:28:30 2024

@author: stacy
"""

import streamlit as st
import requests
import pandas as pd
import time

# Set up headers and sections
st.title("Global Weather Dashboard")

# Load and display cleaned data
st.header("Data Dashboard")
response = requests.get("http://localhost:5000/weather_data")
data = pd.DataFrame(response.json())
st.dataframe(data)

# Simulated live Kafka updates
st.header("Live Weather Updates")
data_placeholder = st.empty()

# Simulate live updates
for i in range(5):  # In a real scenario, listen to Kafka Consumer
    updated_data = data.sample(1)
    data_placeholder.write(updated_data)
    time.sleep(1)

    