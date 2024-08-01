
# while loop , with if , else

# i = 10;
# while i < 20:
#     if i % 7 == 0:
#         i += 1;
#         continue;
#     elif i == 17:
#         break;
#     print(i);
#     i += 1;


# while loop
# to print all odd numbers

# i  = 1;
# while i <10:
#     print(i);
#     i = i + 2;

# For Loop
# Array = [10,20,30,40,50];
# for x in  Array:
#     x = x + 1;
#     print(x);
   

# Range function

# print(list(range(1,10,2)));


# if , elif , else ,Nested if , input function , type casting


# c1 = int(input("Enter ur Age:  "));
# if c1 > 18:
#     print("You r eligible to vote !");
#     Vote = input("Which party u r going to vote ?");
#     if Vote == "DMK":
#         print("good");
#     else:
#         print("bad");
 

# elif c1 == 18:
#     print("You r eligible to vote ! , but ");
#     print("Apply for voter ID");
# else:
#     print("Not eligible to vote !");


# Program to print Multiline strings 



# para = [];
# print("Enter the para: ");
# while True:
#     line = input();

#     if line:
#       para.append(line);
#     else:
#       break;
# print(para);

# output = "\n".join(para);
# print(output);


# Random Function

# import random;
# print(random.randrange(2,30));

# Print all Keywords

# import keyword;
# print(keyword.kwlist)


# Lists , Slicing , Indexing , ID() , Type() 

a = [1,2,"orange","apple",25.5];

# print(a,type(a),id(a))
# print(a[1])

# Indexing
# a[1] = 10;
# print(a[1])

# Slicing
# print(a[0:3])
# print(a[0:])
# print(a[:3])
# print(a[-1])
# print(a[-4:-1])

# copy function
# b = a.copy();
# print(b);

# count()
# print(a.count(25.5))

# Index()
# print(a.index("orange"))

# Length function
# print(len(a));


# Max and Min function
# print(max(a))
# print(min(a))

# Pop () , remove a element using index
# print(a.pop(0));
# print(a)

# Clear function
# print(a.clear());

# Remove function
# a.remove(2);
# print(a)

# Append function
# print(a.append("gold"))
# print(a)

# Insert function - inserting at a particular position
# a.insert(2,"silver");
# print(a)


# Extend function
# print(a.extend(b));
# print(a)

# Adding lists
# print(a + b);


# List Constructor 
# print(list("Arvin"));

# Sort ASC & DEC
# a = [20,30,40,70,10];
# b = [110, 140 , 130 , 120];
# print(a.sort());
# print(b.sort(reverse = True));
# print(a,b)

# Reverse function
# print(a.reverse())
# print(a);

# Del function  - delete element using index
# del a[0];
# print(a);



# Tuples r ordered , immutable  !!  - () Bracket
# To recognize a single character as a tuple

# a = (1,)
# print(type(a))
# if not using comma , it recognizes as integer!


# Sets - {} Bracket 
# Sets cant be indexed , will not be in order , can change any index , can add 
# Removes Duplicate values automatically



# Add method to add another element
# a = {"ram","sam"};
# a.add("Bam");
# print(a)


# To Join 2 Sets , use Update()
# b = {"gold","silver","orange"};
# b.update(a);
# print(b)


# Discard function ( doesnt show error if name is not there , if there removes)
# a.discard("ram");
# print(a)

# Union Function
# c = a.union(b)
# print(c)

# a.add("gam");
# a.add("gold");
# print(a)


# Shows Common values
# c = a.intersection(b)
# print(c)

# Updates the intersected value in 1st set
# a.intersection_update(b)
# print(a)

# prints the uncommmon in 2nd set 
# c = a.symmetric_difference(b)
# print(c)

# if u want to add the uncommon on 1st set use update!
# a.symmetric_difference_update(b)
# print(a)

# if common data is there means - it is joint data , so false  , 
#  if there is no common , nothing to join , so disjoint !
# c = a.isdisjoint(b)
# print(c)

# if a doesn't has b's values its not subset !
# c = a.issubset(b)
# print(c)


# if b has a's values , then its true , to find b from a , its superset !

# c = b.issuperset(a)
# print(c)


# Dictionaries

Details = {
    "name" : "Arvin",
    "Number" : 9566,
    "Date" : 23082002
}

# get() 
# print(Details.get("Date"))

# Accessing
# print(Details["Number"])


# to get only Keys  - Keys ()
# print(Details.keys())


# to get only values  - values ()
# print(Details.values())


# to get only items  - items ()
# print(Details.items())

# updating  a value in dictionary , also adds a new value and also updates !
# Details.update({"name" : "Male"})
# print(Details)