import psycopg2
import json

# Параметри підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname='lab_3',
    user='Ignatiev',
    password='5432',
    host='localhost',
    port='5432'
)

# Функція для отримання даних з таблиці у вигляді словника
def get_table_data_as_dict(table_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return data

# Отримання даних з кожної таблиці
table_names = ['car', 'manufacturer', 'location', 'new_table']  
all_data = {}

for table_name in table_names:
    table_data = get_table_data_as_dict(table_name)
    all_data[table_name] = table_data

# Запис у файл JSON
with open('all_tables_data.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)

# Закриваємо підключення до бази даних
conn.close()
