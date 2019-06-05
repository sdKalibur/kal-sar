import csv

with open ('sample.csv', newline='') as csvfile:
     csv_reader = csv.reader(csvfile, delimiter=';')
     # header = next(csv_reader)
     # header = next(csv_reader)
     data = [ _ for _ in csv_reader ]

for i in range(len(data)):
         if '#' in data[i][0] :
            continue
         else:
            print(data[i])
