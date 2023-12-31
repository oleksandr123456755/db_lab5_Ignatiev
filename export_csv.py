import psycopg2
import csv

# Параметри підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname='lab_3',
    user='Ignatiev',
    password='5432',
    host='localhost',
    port='5432'
)
# Функція для експортування даних з таблиці у CSV-файл
def export_table_to_csv(table_name, file_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    data = cursor.fetchall()

    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])  # Записуємо заголовки стовбців
        writer.writerows(data)

# Виклик функції для кожної таблиці
export_table_to_csv('car', 'car_data.csv')  # Назва таблиці та файлу CSV для першої таблиці
export_table_to_csv('manufacturer', 'manufacturer_data.csv')  # Назва таблиці та файлу CSV для другої таблиці
export_table_to_csv('location', 'location_data.csv')  # Назва таблиці та файлу CSV для третьої таблиці
export_table_to_csv('new_table', 'new_table_data.csv')  # Назва нової таблиці та файлу CSV

# Закриваємо підключення до бази даних
conn.close()
