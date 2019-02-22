import csv

with open('PAO System.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    dict = {}
    arr = []
    tuple = (1, 2, 'hi', "aa")

    for line in csv_reader:
        dict[line[0], line[1]] = [line[1], line[2]]
    for k, v in dict.items():
        print type(k), ">", type(v)

