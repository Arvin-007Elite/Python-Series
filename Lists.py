# lists r changable , duplicates r allowed , 



myList = ["apple" , 25  , "apple"];


# at slicing with normal method , 0:4 means , only till 3 index it shows op
# negative indexing also the starting 1st index will not be printed

# changing the index
myList[2] = 45;

myList[1] = "green";
# changing as a range of values
myList[:2] = ["pink","gold"]

# it adds new element before the mentioned number
# we can add element where vere we wants
myList.insert(1,"silver")

moList = ["DMK", "ADMK"];
# using append function we can add a element at last
myList.append("purple");

# used to  combine the lists
myList.extend(moList);


# to remove a element from a list
myList.remove("gold");


# to remove an index element - POP()
myList.pop(0)

# del method
del myList[2];



# clear method empties the list 
# myList.clear()

myList.pop(1);

# sorting list alpha order
# myList.sort();

# sorting in descending order
myList.sort(reverse = True);

# reverse the list
myList.reverse();

print(myList)

# copy a list
# miList = myList.copy();r

# LIst method for copying a list
miList = list(myList);

print(miList);


# another way of joining list
m1List = miList + myList;
print(m1List);

# tuple function to convert as tuple
# tuple() 


a = ("orange",) * 2
print(type(a))

# to add or remove an element in tuple , we have to convert it as list , then convert it as tuple

# add() method can add an element 

# update() can  add to sets , it can add set 2 in set 1
# discard method  method removes specific objects


# union() can add the  both sets , multiple sets 
# we can use |   operator  instead of union() 

# intersection() can only prints  duplicates.
# & instead of intersection

# difference () - prints items from set1 that r not in set 2
# - operator instead of difference

# symmetric_difference() - used for elemets that r not in both sets 
# ^ operator

# dict()  function to convert

# get() method is used to get the value in a dictionary
# keys() will get all keys in a dictionary
# values() to get all values in a list
# gets the values with items 
# upadet method used for updateing value

# pop item() is used to pop last item only

