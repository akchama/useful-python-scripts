import sqlite3
import argparse

def list_data_sorted_by_date():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM weather_data 
    ORDER BY 
        SUBSTR(date, 7, 4),   -- Yıl
        SUBSTR(date, 4, 2),   -- Ay
        SUBSTR(date, 1, 2)    -- Gün
    ''')

    for row in cursor.fetchall():
        date, temperature = row
        print(f"Tarih: {date}, Sıcaklık: {temperature}°C")

    conn.close()

def list_data_for_temperature(temperature):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM weather_data WHERE temperature = ?', (temperature,))

    for row in cursor.fetchall():
        date, temp = row
        print(f"Tarih: {date}, Sıcaklık: {temp}°C")

    conn.close()

def list_data_for_date(target_date):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM weather_data WHERE date = ?', (target_date,))

    row = cursor.fetchone()
    if row:
        date, temperature = row
        print(f"Tarih: {date}, Sıcaklık: {temperature}°C")
    else:
        print(f"{target_date} için veri bulunamadı.")

    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Hava Durumu Veri Gösterici')
    parser.add_argument('-d', action='store_true', help='Tarihe göre sıralanmış olarak bütün verileri listele')
    parser.add_argument('-t', metavar='TARIH', help='Belirtilen tarih için sıcaklık sorgusu (format: GG/AA/YYYY)')
    parser.add_argument('-s', metavar='SICAKLIK', type=int, help='Belirtilen sıcaklık için tüm tarihleri listele')

    args = parser.parse_args()

    if args.d:
        list_data_sorted_by_date()
    elif args.t:
        list_data_for_date(args.t)
    elif args.s:
        list_data_for_temperature(args.s)

if __name__ == '__main__':
    main()
