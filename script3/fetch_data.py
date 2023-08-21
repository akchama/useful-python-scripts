import os
import datetime
import requests
import json

def fetch_weather_data():
    base_url = "https://api.weather.com/v1/location/LTAC:9:TR/observations/historical.json"
    api_key = "e1f10a1e78da46f5b10a1e78da96f525"
    start_date = datetime.date(2021, 8, 1)
    end_date = datetime.date(2023, 8, 16)
    subdir = "temperatures"

    if not os.path.exists(subdir):
        os.mkdir(subdir)

    while start_date < end_date:
        next_month_start = (start_date.replace(day=1) + datetime.timedelta(days=31)).replace(day=1)
        current_end_date = min(next_month_start - datetime.timedelta(days=1), end_date)

        params = {
            "apiKey": api_key,
            "units": "e",
            "startDate": start_date.strftime('%Y%m%d'),
            "endDate": current_end_date.strftime('%Y%m%d')
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            filename = f"{start_date.strftime('%Y-%m')}.json"
            filepath = os.path.join(subdir, filename)

            with open(filepath, 'w') as file:
                json.dump(data, file)

            print(f"Saved data for {start_date.strftime('%Y-%m')} to {filename}.")
        else:
            print(f"Error fetching data for date range {start_date} to {current_end_date}.")

        start_date = next_month_start

if __name__ == "__main__":
    fetch_weather_data()
