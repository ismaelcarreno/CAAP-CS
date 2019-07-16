def main():

    print("This program will convert Fahrenheit to Celsius!")

    Ftemp= eval(input("Enter the temperature in Fahrenheit: "))
    Ctemp = (5*(Ftemp-32)) / 9
    for a in range(5):
        print(Ctemp,"Celsius")

main()
