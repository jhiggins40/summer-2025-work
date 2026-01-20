import json

# --- CONFIGURATION ---
json_path = r"/home/all_tables.json"   # Replace with full path to your file
target_database = "DatabaseName" # specify any database you want to target/print table names from

# --- LOAD JSON ---
with open(json_path, "r") as f:
    data = json.load(f)

# --- EXTRACT TABLES BY DATABASE ---
tables_by_db = {}
for table in data.get("TableList", []):
    db = table.get("DatabaseName", "").lower()
    name = table.get("Name", "").lower()

    if db not in tables_by_db:
        tables_by_db[db] = []
    tables_by_db[db].append(name)

# --- FORMAT FOR YAML ---
for db, tables in tables_by_db.items():
    print(f"- name: {db}")
    print(f"  schema: {db}")
    print(f"  tables:")
    for table_name in sorted(tables):
        print(f"    - name: {table_name}")
    print()

