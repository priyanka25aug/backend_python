def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

x = int(input("Please enter the value of x "))
y = int(input("Please enter the value of y "))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


choice = input("Enter choice(1/2/3/4): ")



if choice == '1':
    print (add(x,y))

elif choice == '2':
    print (substract(x,y))

elif choice == '3':
    print (multiply(x,y))

elif choice == '4':
    print (divide(x,y))

else:
    print ("invalid input")
    
