# Program make a simple calculator that can add, subtract, multiply and divide using functions
#Vanisha
# define functions
def add(x, y):
   """This function adds two numbers"""

   return x + y

def sub(x, y):
   """This function adds two numbers"""

   return x - y


# take input from the user
print("Select operation.")
print("1.Add")

print("2.Sub")

choice = str(raw_input("Enter choice(1/2):"));

num1 = int(raw_input("Enter first number: "))
num2 = int(raw_input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
if choice == '2':
   print(num1,"-",num2,"=", sub(num1,num2))
else:
   print("Invalid input")