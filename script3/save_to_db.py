import sqlite3
import json
import datetime
import os

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    date TEXT PRIMARY KEY,
    temperature INTEGER
)
''')

# Directory path
subdir = "temperatures"

# Assuming you've saved data in the format "YYYY-MM.json"
start_year = 2021
end_year = 2023  # Adjust based on your needs
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for year in range(start_year, end_year + 1):
    for month in months:
        file_path = os.path.join(subdir, f"{year}-{month}.json")  # Updated to include subdir
        if os.path.exists(file_path):  # Check if file exists in the subdir
            with open(file_path, 'r') as file:  # Read file from the subdir
                data = json.load(file)
                observations = data.get('observations', [])
                for observation in observations:
                    date = datetime.datetime.fromtimestamp(observation['valid_time_gmt']).strftime('%d/%m/%Y')
                    temperature_f = observation['temp']
                    temperature_c = round(fahrenheit_to_celsius(temperature_f))
                    cursor.execute('INSERT OR REPLACE INTO weather_data (date, temperature) VALUES (?, ?)', (date, temperature_c))

conn.commit()
conn.close()

if __name__ == "__main__":
    print("Data has been saved to the database!")
