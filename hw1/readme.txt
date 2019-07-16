Ismael Carreno
ismaelcarreno

1: Hello World!
Code:
def main():

    print("Hello!")
    yourname = input("Enter your name: ")
    print("Hello", yourname)
    color = input("Enter your favorite color: ")
    candy = input("Enter your favorite candy: ")
    print(yourname, "enjoys", candy, "and his favorite color is", color)

main()
Version of Python: 3.7.4
Explanation: This program simply greets you, takes in your name and other information to make a concise summary of you. The main functions of the code are ‘print’ and ‘input’.

2: Converter
Code:
def main():

    print("This program will convert Fahrenheit to Celsius!")

    Ftemp= eval(input("Enter the temperature in Fahrenheit: "))
    Ctemp = (5*(Ftemp-32)) / 9
    for a in range(5):
        print(Ctemp,"Celsius")

main()
Version of Python: 3.7.4
Explanation: The program is able to convert Fahrenheit to Celsius and prints this calculation five times. The temperature in Fahrenheit was taken from the input of the user, then it was converted through the formula. It was printed five times through the ‘for loop’ and ‘range’ of five.

3: Unit Conversion
Code:
def main():

    print("This program converts Fahrenheit to Kelvin!")

    FTemp = eval(input("Enter the temperature in Fahrenheit: "))
    KTemp = (FTemp - 32) * 5 / 9 + 273.15
    print(KTemp, "Kelvin.")

main()
Version of Python: 3.7.4
Explanation:  The program is able to convert Fahrenheit to Kelvin. To accomplish this I asked the user for a temperature in Fahrenheit, then I put this number through a formula to calculate the temperature in Kelvin.

4: Slope
Code:
def main():

    print("This program will take the sum for any amount of numbers that you wish!")

    x = eval(input("How many numbers do you want to enter? "))

    list = []

    for i in range(x):
        y = eval(input("Enter an integer: "))
        list.append(y)

    print(sum(list))

main()
Version of Python: 3.7.4
Explanation: The program sums up any amount of numbers that the user states that they will input. For example, if they say that they’re going to input four distinct numbers, then the program will only take four numbers and add these four numbers together. To complete this task I used a ‘for loop’ and used the ‘range’ function to limit the amount of inputs from the user to the amount they indicated at the beginning. I created a list by using ‘list.append’, which added every integer that was inputted by the user into a list to create a sequence. Finally, I used the sum function to add up the list and printed this to output the sum.

5: FibonnaciSequence
Code:
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
Version of Python: 3.7.4
Explanation: This program outputs the Fibonacci sequence up to the nth term of the users choice and indicates the final term of the sequence that is produced for that specific nth term. This was done through a simple ‘for loop’ and ‘range’. Within the loop I used the simultaneous assignment to create the Fibonacci sequence. Each time the program went through the loop it appended the final value to the list to create the sequence.

Part 2: Change
Code:
def main():

    print("This program will give you the minimum amount of coins for change.")
    money = eval(input("Enter an amount of money: "))

    money = money * 100

    if money >= 25:
        quarters = money // 25
        money = money - quarters * (25)
    else:
        quarters = 0

    if money >= 10:
        dimes = money // 10
        money = money - dimes * (10)
    else:
        dimes = 0

    if money >= 5:
        nickels = money // 5
        money = money - nickels * (5)
    else:
        nickels = 0

    if money >= 1:
        pennies = money // 1
        money = money - pennies * (1)
    else:
         pennies = 0

    coin = quarters + dimes + nickels + pennies

    print("This is the minimum amount of coins that are needed:", coin)
    print("Quarters:", quarters, "Dimes:", dimes, "Nickels:", nickels, "Pennies:",pennies)
main()
Version of Python: 3.7.4
Explanation: This program accepts any amount of money and tells you the least amount of coins needed for change along with how much of each type of coin is needed. I made it so that it even accepts an input that is over 0.99 by multiplying the amount inputted by the user by 100. Thus, I used 25, 10, 5 and 1 when representing each distinct coin. I used several ‘if... else’ statements and decreased the value of the money that was inputted as it went through each one. When the amount was properly sorted I summed up the amount of quarters, dimes, nickels and pennies to get the total amount of coins needed.
