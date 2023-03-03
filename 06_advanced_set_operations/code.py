friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

friends_two = friends.union(abroad)
print(friends_two)


art = {"Bob", "Jen", "Rolf", "Charlie" }
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)