import csv
import json

# names = {}
# with open("name.basics.tsv") as name_file:
#     reader = csv.reader(name_file, delimiter="\t")
#     for row in reader:
#         names[row[0]] = row[-1].split(",")
# 
# with open("names.json", "w") as output:
#     json.dump(names, output, indent = 4)

titles = {}

with open("title.principals.tsv") as name_file:
    reader = csv.reader(name_file, delimiter="\t")
    for row in reader:
        if not row[0] in titles:
            titles[row[0]] = []
        titles[row[0]].append(row[2])

with open("titles.json", "w") as output:
    json.dump(titles, output, indent = 4)


