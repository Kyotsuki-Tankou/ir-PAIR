import sqlite3
import re

def read_and_deduplicate_column(db_file, table_name, column_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    query = f"SELECT DISTINCT {column_name} FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    unique_values = set()
    pattern = re.compile(r'[;|/]+')
    
    for row in results:
        if None in row:
            continue
        values = pattern.split(row[0])
        unique_values.update(values)
    unique_values_list = list(unique_values)
    return unique_values_list

db_file = 'STpair.db'
table_name = 'datasets'
column_name = 'disease'

unique_values = read_and_deduplicate_column(db_file, table_name, column_name)
print(unique_values)
