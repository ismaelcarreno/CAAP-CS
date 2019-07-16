def main():

    print("This program converts Fahrenheit to Kelvin!")

    FTemp = eval(input("Enter the temperature in Fahrenheit: "))
    KTemp = (FTemp - 32) * 5 / 9 + 273.15
    print(KTemp, "Kelvin.")

main()
