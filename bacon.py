import json

with open("names.json") as f:
    names = json.load(f)
with open("titles.json") as f:
    titles = json.load(f)

m = [len(titles[title]) for title in titles]

print(max(m))

bacon_const = "nm0000102"

# nconst
# tconst

# names : bacon number array

table = {}


def bacon_number(name):
    if name == bacon_const:
        return 0
    if name in table:
        return table[name]
    shared_actors = [[j for j in titles[title]] for title in names[name]]
    lowest = float("inf")
    for i in shared_actors:
        for j in i:
            num = bacon_number(j)
            if num < min:
                lowest = num
    table[name] = lowest + 1
    return table[name]

print(bacon_number("nm5384395"))

with open("bacon.json", "w") as f:
    json.dump(table)
