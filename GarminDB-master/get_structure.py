import sqlite3

# Connect to your GarminDB database
conn = sqlite3.connect('/Users/juanvecino/HealthData/DBs/garmin_activities.db')

# Get a list of all tables
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = conn.execute(tables_query).fetchall()

# Loop through each table and get its structure
for table in tables:
    table_name = table[0]
    print(f"\nStructure of table: {table_name}")

    # Query to get structure of the table
    table_structure_query = f"PRAGMA table_info({table_name});"
    table_structure = conn.execute(table_structure_query).fetchall()

    # Print the structure of the table
    for column in table_structure:
        print(
            f"Column ID: {column[0]}, Name: {column[1]}, Type: {column[2]}, Not Null: {column[3]}, Default: {column[4]}, Primary Key: {column[5]}")

conn.close()
