while True:
    opration = int(input('''
Select the Opration:
1. Addtion
2. Subtraction
3. Multiplication
4. Division
'''))
    if opration in (1,2,3,4):
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        if opration == 1 :
            result = n1 + n2
            print(f"{n1} + {n2} = {result}")
        elif opration == 2 :
            result = n1 - n2
            print(f"{n1} - {n2} = {result}")
        elif opration == 3 :
            result = n1 * n2
            print(f"{n1} * {n2} = {result}")
        elif opration == 4 :
            result = n1 / n2
            print(f"{n1} / {n2} = {result}")
        else:
           print("Erro, Enter choice (1/2/3/4):")
        nextcalculate = input("Let's do  next caculation ,Press any key to continue  (yes/no)")
        if nextcalculate == 'no':
                              break
    else:
        print("Error, Please choice the opration from 1 to 4")
