# Example of break statement

names = [
    "Shyam",
    "harry",
    "Garry",
    "Barry"
]

for name in names:
    if name == "Garry":
        break
    print("Names before break are :- ", name)


# Example of continue statement

games = [
    "pubg",
    "free-fire",
    "cod",
    "efootball",
    "subway surfers",
    "dark souls",
    "wukong",
    "god of war",
    "plants vs zombies",
    "gta vi",
    "robbery bob"
]

for game in games:
    if game == "wukong":
        continue
    print("Games before break are :- ", game)
