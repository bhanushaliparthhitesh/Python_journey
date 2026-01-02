# if_elif_else_ladder statement
a = int(input("enter a number:"))

if(a>=18):
    print("You are above the age of consent")
elif(a<0):
    print("You are entering invalid negative age")

elif(a==0):
    print("You are entering  0 , which is an invalid age")
else:
    print("You are below the age of consent")

print("Thank you!")