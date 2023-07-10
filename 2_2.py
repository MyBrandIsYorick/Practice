tv_shows = ["Friends", "Supernatural", "Riverdale", "Adventure Time"]
for programms in tv_shows:
    print(programms)
print("Input the new show")
new_show = str(input())
print("What position do u want to insert new tv show?")
pos = int(input())
tv_shows.insert(pos, new_show)
print(tv_shows)
