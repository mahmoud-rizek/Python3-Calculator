print("Select operation.")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Dividu")

choice = int(input("Enter choice (1/2/3/4): "))

while True:
    if choice in (1,2,3,4):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        if choice == 1:
            resulte = number1 + number2
            print(f"{number1} + {number2} = {resulte}")
        elif choice == 2:
            resulte = number1 - number2
            print(f"{number1} - {number2} = {resulte}")
        elif choice == 3 :
            resulte = number1 * number2
            print(f"{number1} * {number2} = {resulte}")
        elif choice == 4 :
            resulte = number1 / number2
            print(f"{number1} / {number2} = {resulte}")
        else:
            print("Erro, Enter choice (1/2/3/4):")
           
        nextcaculation = input("Let's do  next caculation (yes/no)")
        if nextcaculation == "no":
            break
    else:
        print("Error, Enter choice from this list(1/2/3/4):")
