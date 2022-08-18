import json
import csv

def to_json_file(export_file, users):
    json.dump(users, export_file, indent=4)
    export_file.close()

def to_csv_file(export_file, users):
    fieldnames = ['name', 'id', 'home', 'shell']
    writer = csv.DictWriter(export_file, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow({'name':user['name'], 'id':user['id'], 'home':user['home'], 'shell':user['shell']})
        export_file.close()
