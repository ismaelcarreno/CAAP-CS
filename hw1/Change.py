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
    print("Quarters:", quarters, "Dimes:", dimes, "Nickels:", nickels, "Pennies:", pennies)
main()
