# a = 10;
# b = 10;
# c = a+b;
# print(c);
# d ="arvin"
# e = True;

# print(id(a));
# print(id(b));
# print(id(c));

# print(type(a));
# print(type(d));
# print(type(e));

# import keyword;
# print(keyword.kwlist);

# Name = input("Enter the Name: ");
# print(Name);

# var1 =input("Enter the number : ");
# var2 =input("Enter the number : ");
# var3 = print(var1 + var2);

# var4 = int(input("Enter the number: "));
# var5 = float(input("Enter the number: "));
# var6 = var5 + var4;
# print(var6);

# Name1,Name2,Name3 = input("Enter the names: ").split(",");
# print(Name1,Name2,Name3)

# para = """ My name is Arvin""";
# print(para);

# import random
# print(random.randrange(2,8));







# a = "Arvin  "
# b = "kritik " +a 
# c = a + b;
# print(c)
# print(b)
# print(a+b)

# print("Enter the names:  ",c)


# a = 40;
# b = 50;
# c = "my age is {}, {}"
# print(c.format(a,b));

# a = " i am Arvin";
# print("Arvin" not in a);

# a = "i am arvin";

# if "arvin" not in a:
#     print("unavailable");
# else:
#     print(a);

# a = [10,20,30,40];
# b = [50,60,70,80];
# c = a;
# if c is not  b:
#     print("not matched")
# else:
#     print(c);

# a = "kenny";
# b = "arvin";
# c = "kritik";
# print(a,b,c);
# print(a + b + c);


# a = "kenny";
# print(a.upper());
# b = "OMEGA";
# print(b.lower());

# print(a.capitalize());



# problem till the concepts of if-else :

# st_1 = 100;
# st_2 = 95;
# st_3 = 90;
# colors_1 = ["red", "green", "blue"];
# colors_2 = ["yellow","pink","white"];
# parties_1 = ("dmk","admk");
# parties_2 = ("bjp","ntk");
# areas_1 = {"tamilnadu","kerala"};
# areas_2 = {"karnataka","andhra"};
# dict = {"name":"arvin",
#         "age":24,
#         "pincode":600049
#         }
# print("Calculation of ur mark:  ");
# t1 = int(input("Enter the 1st mark: "));
# t2 = int(input("Enter the 1st mark: "));
# t3 = int(input("Enter the 1st mark: "));





# Total_1 = st_1 + t1; type: ignore
# Total_2 = st_2 + t2; type: ignore
# Total_3 = st_3 + t3; type: ignore



# print(Total_1 ,"is my total of 2 subjects");


# if  Total_1 > 100:
#     print("passed");
#     if Total_1 >= 150:
#         print("excellent score");
#     elif Total_1 >= 120 & Total_1 <= 149:
#         print("average");

# elif  Total_1 <= 120 & Total_1 < 100:
#     print("just passed");
# else:
#     print("failed");


# print("total of 2 subjects:  " , Total_2);




# print("total of 2 subjects: " , Total_3);



# for loop 

# for i in range(0,10,2):
#     print(i);



# while loop

i = 10;
while i < 20:
    if i % 7 == 0:
        i += 1;
        continue;
    elif i == 17:
        break;
    print(i);
    i += 1;
    