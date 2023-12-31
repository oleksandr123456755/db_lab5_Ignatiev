import psycopg2

# Параметри підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname='lab_3',
    user='Ignatiev',
    password='5432',
    host='localhost',
    port='5432'
)

# Шлях до CSV-файлу та назва таблиці
csv_file = 'cars.csv'
table_name = 'new_table'

# Виконання імпорту даних
with conn.cursor() as cursor:
    with open(csv_file, 'r') as f:
        next(f)  # Пропустити заголовок (якщо він існує)
        cursor.copy_from(f, table_name, sep=',')
    conn.commit()

# Закриття з'єднання
conn.close()
