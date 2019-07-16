def main():

    print("This program creates the Fibonacci sequence up to any nth term!")

    x = eval(input("Enter the nth term you wish to go up to: "))
    a, b = 0, 1

    list = [1,]
    for i in range(x-1):
        a, b = b, a+b
        list.append (b)
    print("This is your Fibonacci sequence", list)
    print("This is the value for your nth term:", list[x-1])

main()
