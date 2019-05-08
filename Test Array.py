array1d = ["a","b","c","d"]
#print(array1d[1])
#print(array1d)

array2d = [["a","b","c","d"],["e","f","g","h"]]
#print(array2d[1][1])
#print(array2d)

array3d = [[["a","b","c","d"],["e","f","g","h"]],
           [["i","j","k","l"],["m","n","o","p"]]]

#print(array3d[1][1][1])
#print(array3d)


#Rules for simple Arrays:

#Appending something to an array; in the format of:
#   name_of_array.append(whatever you want to append)

array1d.append("e")

#Deleting an item from an array; in the format of:
#   name_of_array.pop(position of item)

array1d.pop(4)

#Or if you don't know the position of the item, use:
#   name_of_array.delete(whatever you want to delete)

array1d.append("e")
array1d.delete("e")


#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	        Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	        Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	        Sorts the list
