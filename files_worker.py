import csv
import json


data_rows = [
    {
        'departure point': 'Kiev',
        'departure time': '12:00',
        'destination point': 'London',
        'arrival time': '23:00',
        'cost ticket': '500$'
    },
    {
        'departure point': 'Kiev',
        'departure time': '6:00',
        'destination point': 'Paris',
        'arrival time': '15:00',
        'cost ticket': '90$'
     },
    {
        'departure point': 'Borispil',
        'departure time': '9:50',
        'destination point': 'Berlin',
        'arrival time': '14:10',
        'cost ticket': '300$'
    }
]

fieldnames = [
    'departure point',
    'departure time',
    'destination point',
    'arrival time',
    'cost ticket'
]

file_path_csv = "schedules/schedule.csv"
file_path_json = "schedules/schedule.json"
def data_cvs_json(file_path, data, fieldnames,file_path_json):
    with open(file_path, 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()

        for input_row in data:
            writer.writerow(input_row)

    with open(file_path_json, "w") as fh:
            json.dump(file_path, fh, indent=4, sort_keys=True)

# def reader(file_path_csv, data, file_path_json):
#         with open(file_path_csv, newline='') as csvfile:
#                 reader = csv.DictReader(csvfile)
#
#                 for row in reader:
#                     print( f"{row=}" )
#                     data.append(row)
#
#         with open(file_path_json, "w") as fh:
#             json.dump(data, fh, indent=4, sort_keys=True)
data_cvs_json(file_path_csv, data_rows, fieldnames,file_path_json)
# data = []
# reader(file_path_csv,data,file_path_json)
# print(data)
