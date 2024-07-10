dictionary={"cat":"meow","dog":"bowbow","snake":"bussbuss"}
for i,j in dictionary.items():
    print(i,"-->",j)
print("\n")   
for j in dictionary.values():
    print(j)
print("\n")

## Adding other values in dictionary (You can alse use dictionary.update() to add values to dictionary)
dictionary["cow"]="Moo"
print("The new item is added to dictionary:")
print(dictionary)
print("\n")

## Changing the sound for any item in dictionary
dictionary["dog"]="Bark"
print("The new sound item for dog is:")
print(dictionary)
print("\n")
## Deleting the items from dictionary (you can also use dictionary.popitem() to remove values in dictionary)
del dictionary["snake"]
print("Deleting snake item from dictionary")
print(dictionary)