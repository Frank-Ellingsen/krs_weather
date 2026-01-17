# KRS Weather Analytics

## Overview
This project analyzes historical weather data for **Kristiansand (KRS)** and transforms raw API data into **clear, business-ready insights**.  
The focus is on **automation, time-series analysis, and storytelling with data**, rather than ad-hoc exploration.

The project generates **static, shareable outputs** (HTML dashboards and CSV files) that can be hosted via GitHub Pages or reused in reports and presentations.

---

## Business Use Case
Weather trends are relevant for planning and decision-making across multiple domains, such as:
- Operations & logistics
- Energy consumption
- Tourism and event planning
- Infrastructure and risk assessment

This project demonstrates how raw weather data can be converted into **reliable, repeatable analytics outputs** that support trend analysis and decision-making.

---

## Key Features
- Automated ingestion of weather data
- Time-series analysis of temperature and precipitation
- Export of **ready-to-share HTML visualizations**
- Downloadable CSV snapshots of recent records
- Reproducible workflow using Python

---

## Tools & Technologies

| Tool | How it’s used |
|-----|--------------|
| **Python** | Data ingestion, transformation, analysis, and automation |
| **Pandas** | Data cleaning, aggregation, and time-series handling |
| **Plotly** | Interactive visualizations exported as standalone HTML |
| **APIs** | Retrieval of historical and current weather data |
| **GitHub Pages** | Hosting static analytics outputs |
| **CSV** | Lightweight data sharing and validation |

---

## Project Structure

krs_weather/
├── weather_snapshot.py # Main script generating analytics outputs
├── weather.ipynb # Exploratory analysis and validation
├── requirements.txt # Python dependencies
├── docs/ # Static output for GitHub Pages
│ ├── index.html
│ ├── temperature_trend.html
│ ├── precipitation_trend.html
│ └── last_100_weather_records.csv


