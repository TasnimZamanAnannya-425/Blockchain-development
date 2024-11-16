
def input_values():
    num1 = int(input("enter first value:\n"))
    num2 = int(input("enter second value:\n"))
    process_values(num1, num2)

def process_values(x, y):
    total = x + y
    display_result(total)

def display_result(total):
    print("total value is", total)

while True:
    num1,num2 = input_values()
    total = process_values(num1,num2)

    display_result(total)
    choice = input("do you want to continue(yes/no)?")
    if choice == "yes" or choice == "Yes" or choice =="Yes":
        print("Program is running")
    else:
        print("Program is terminated 😂")
        break



