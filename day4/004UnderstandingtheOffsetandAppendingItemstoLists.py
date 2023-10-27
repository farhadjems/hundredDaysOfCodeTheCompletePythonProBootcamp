
iran_provinces = ["Fars", "Tehran", "Bushehr", "Esfahan"] 

print(iran_provinces[0]) # to print each element of list
print(iran_provinces[2])

#negative indexing starts from the end
print(iran_provinces[-1])

#to edit an element, just assign to it 
iran_provinces[1] = "Kurdistan"

#to add a new element
iran_provinces.append("Tehran")

# to extend a list with another list
iran_provinces.extend(["Azerbaijan", "Alborz", "Sistan and Baluchistan"])



print(iran_provinces) # to print the list 