games = ["Minecraft", "Terraria", "Portal", "Subnautica", "Roblox"]

print(games[-1])
print(games[-2])
print(games[0])

print("====================")

numbers = [5, 10, 15, 20, 25, 30, 35, 40]

print(numbers[0:3])
print(numbers[3:6])
print(numbers[-3:])
print(numbers[2:])

print("====================")

names = ["Peter", "Anne", "Thomas", "Claire", "Martin", "Eve"]

print("Number of Names:", (len(names)))
print(names[-3:])
names[-1] = "David"
names.append("Philip")
print(names)

print("====================")

games_2 = ["Minecraft", "Terraria", "Roblox"]

games_2.append("Subnautica")
games_2.insert(1, "Portal")
games_2.extend(["GTA V", "The Sims"])
games_2.remove("Roblox")

last_game = games_2.pop(-1)

print(games_2)
print(last_game)
print(len(games_2))

print(games_2[0:2])
print(games_2[-2:])