a = int(input("enter a number:"))
# if statement 1

if(a%2 == 0):
    print("a is even")
# end of if statement 1

# if statement 2
if(a>=18):
    print("You are above the age of consent")
elif(a<0):
    print("You are entering invalid negative age")

elif(a==0):
    print("You are entering  0 , which is an invalid age")
else:
    print("You are below the age of consent")

# end of if statement 2
print("Thank you!")