def main():

    print("This program will take the sum for any amount of numbers that you wish!")

    x = eval(input("How many numbers do you want to enter? "))

    list = []

    for i in range(x):
        y = eval(input("Enter an integer: "))
        list.append(y)
    
    print(sum(list))

main()
