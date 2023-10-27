
#* note that list indexing starts with zero, so that when len() function determines the size of the list, the last element is of index "len() - 1"

iran_provinces = ["Fars", "Tehran", "Bushehr", "Esfahan"] 
print(len(iran_provinces))
print(f"last element: {iran_provinces[len(iran_provinces)-1]}")

#* to add lists as elements to a list
Fars = ["Shiraz", "Kazerun", "Abadeh",]
Bushehr = ["Bushehr", "Borazjan", "Dashti"]

iran_provinces = [Fars, Bushehr]

print(iran_provinces)