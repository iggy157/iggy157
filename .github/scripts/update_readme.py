#!/usr/bin/env python3
"""
Auto-update README.md with:
- Current weather in Shizuoka
- Academic year status (auto-updates on April 1st)
- Random inspirational quote
"""

import os
import re
from datetime import datetime
import requests

# Configuration
README_PATH = "README.md"
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
SHIZUOKA_LAT = "34.9769"
SHIZUOKA_LON = "138.3831"

def get_academic_year():
    """Calculate academic year based on current date"""
    now = datetime.now()
    year = now.year
    month = now.month

    # Japanese academic year starts April 1st
    if month < 4:
        # Before April = still previous academic year
        base_year = year - 1
    else:
        # April or later = new academic year
        base_year = year

    # Determine year level (assuming started as B3 in 2024)
    # B3: 2024/04 - 2025/03
    # B4: 2025/04 - 2026/03
    # M1: 2026/04 - 2027/03
    # M2: 2027/04 - 2028/03

    start_year = 2024  # Started as B3 in April 2024
    years_elapsed = base_year - start_year

    year_names = ["B3", "B4", "M1", "M2"]
    year_names_en = ["3rd Year Undergraduate", "4th Year Undergraduate", "1st Year Master's", "2nd Year Master's"]
    year_names_cn = ["本科三年级", "本科四年级", "硕士一年级", "硕士二年级"]

    if years_elapsed < len(year_names):
        return {
            "ja": year_names[years_elapsed],
            "en": year_names_en[years_elapsed],
            "cn": year_names_cn[years_elapsed]
        }
    else:
        return {
            "ja": "M2+",
            "en": "Master's Graduate",
            "cn": "硕士毕业"
        }

def get_weather():
    """Fetch current weather for Shizuoka"""
    if not WEATHER_API_KEY:
        return {
            "condition": "☁️",
            "temp": "N/A",
            "description": "API key not configured"
        }

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={SHIZUOKA_LAT}&lon={SHIZUOKA_LON}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Map weather conditions to emojis
        weather_map = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Fog": "🌫️"
        }

        main_weather = data["weather"][0]["main"]
        temp = round(data["main"]["temp"])

        return {
            "condition": weather_map.get(main_weather, "🌤️"),
            "temp": f"{temp}°C",
            "description": data["weather"][0]["description"].capitalize()
        }
    except Exception as e:
        print(f"Weather API error: {e}")
        return {
            "condition": "🌤️",
            "temp": "N/A",
            "description": "Unable to fetch weather"
        }

def get_random_quote():
    """Get a random inspirational quote about AI/CS"""
    quotes = [
        '"The question of whether a computer can think is no more interesting than the question of whether a submarine can swim." - Edsger W. Dijkstra',
        '"Artificial intelligence is the new electricity." - Andrew Ng',
        '"The science of today is the technology of tomorrow." - Edward Teller',
        '"Intelligence is the ability to adapt to change." - Stephen Hawking',
        '"The best way to predict the future is to invent it." - Alan Kay',
        '"Machine learning is the last invention that humanity will ever need to make." - Nick Bostrom',
        '"AI is probably the most important thing humanity has ever worked on." - Sundar Pichai'
    ]

    import random
    return random.choice(quotes)

def update_readme():
    """Update README.md with dynamic content"""
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get data
    academic_year = get_academic_year()
    weather = get_weather()
    quote = get_random_quote()
    now = datetime.now()

    # Update weather section
    weather_section = f"""<!-- WEATHER_START -->
**📍 Shizuoka, Japan**
{weather['condition']} Weather: {weather['description']}
🌡️ Temperature: {weather['temp']}
📅 Updated: {now.strftime('%Y-%m-%d %H:%M')} JST
<!-- WEATHER_END -->"""

    content = re.sub(
        r'<!-- WEATHER_START -->.*?<!-- WEATHER_END -->',
        weather_section,
        content,
        flags=re.DOTALL
    )

    # Update academic year in Japanese section
    content = re.sub(
        r'\*\*学年\*\*: [^\n]+',
        f'**学年**: {academic_year["ja"]}（{now.strftime("%Y年%m月")}時点）',
        content
    )

    # Update academic year in English section
    content = re.sub(
        r'\*\*Year\*\*: [^\n]+',
        f'**Year**: {academic_year["en"]} (as of {now.strftime("%B %Y")})',
        content
    )

    # Update academic year in Chinese section
    content = re.sub(
        r'\*\*年级\*\*: [^\n]+',
        f'**年级**: {academic_year["cn"]}（截至{now.strftime("%Y年%m月")}）',
        content
    )

    # Update academic status
    next_level = {"B3": "B4", "B4": "M1", "M1": "M2", "M2": "Graduate"}.get(academic_year["ja"], "Graduate")
    academic_status = f"""<!-- ACADEMIC_STATUS_START -->
**🎓 Academic Status**: {academic_year["ja"]} → {next_level} (Updates April 1st)
**🎯 Current Focus**: Werewolf Intelligence & BDI Modeling
<!-- ACADEMIC_STATUS_END -->"""

    content = re.sub(
        r'<!-- ACADEMIC_STATUS_START -->.*?<!-- ACADEMIC_STATUS_END -->',
        academic_status,
        content,
        flags=re.DOTALL
    )

    # Update quote
    quote_section = f"""<!-- QUOTE_START -->
*{quote}*
<!-- QUOTE_END -->"""

    content = re.sub(
        r'<!-- QUOTE_START -->.*?<!-- QUOTE_END -->',
        quote_section,
        content,
        flags=re.DOTALL
    )

    # Write back
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ README updated successfully!")
    print(f"   Academic Year: {academic_year['ja']} ({academic_year['en']})")
    print(f"   Weather: {weather['condition']} {weather['temp']} - {weather['description']}")
    print(f"   Updated at: {now.strftime('%Y-%m-%d %H:%M:%S')} JST")

if __name__ == "__main__":
    update_readme()
