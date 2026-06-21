while True :
    print("===========================================")
    print("""Please select the Conversion type You want
1. Length Conversions
2. Weight Conversions
3. Temperature Conversions
4. Exit""")
    print("===========================================")
    conv_type = int(input("Select the Option that you want(1,2,3,4) : "))

    if conv_type == 4:
        print("===========================================")
        print("Thank You!")
        print("===========================================")
        break
    elif conv_type == 1:
        while True :
            print("===========================================")
            transform = input("""a. Meter ↔ Kilometer
b. Meter ↔ Centimeter
c. Kilometer ↔ Meter
Select option(a,b,c): """)
            print("===========================================")
            if transform not in ['a','b','c']:
                 print("===========================================")
                 print("Invalid option please select the valid one!!")
                 print("===========================================")
                 continue
            elif transform == 'a' :
                print("===========================================")
                meter = float(input("Enter the Meter value :"))
                print("===========================================")
                print(f"{meter} meters = {meter/1000} kilometers")
                print("===========================================")
            elif transform == 'b' :
                print("===========================================")
                meter = float(input("Enter the Meter value :"))
                print("===========================================")
                print(f"{meter} meters = {meter*100} centimeters")
                print("===========================================")
            else :
                print("===========================================")
                kilometers = float(input("enter the kilometers value :"))
                print("===========================================")
                print(f"{kilometers} kilometers  = {kilometers*1000} meters")
                print("===========================================")
            
            terminate = input("Want to close the 1. Length Conversions Operation(y/n):").lower()
            print("===========================================")
            if terminate =='y':
                break

    elif conv_type == 2:
        while True:
            print("===========================================")
            transform = input("""a.Gram ↔ Kilogram
b. Kilogram ↔ Gram
Select option(a,b): """)
            print("===========================================")
            if transform not in ['a','b']:
                print("===========================================")
                print("Invalid option please select the valid one!!")
                print("===========================================")
                continue
            elif transform == 'a' :
                print("===========================================")
                gram = float(input("enter the Gram value :"))
                print("===========================================")
                print(f"{gram} Grams = {gram/1000} kilograms")
                print("===========================================")
            else :
                print("===========================================")
                kilograms = float(input("enter the kilograms value :"))
                print("===========================================")
                print(f"{kilograms} kilograms = {kilograms*1000} Grams")
                print("===========================================")
        
            terminate = input("Want to close the 2. Weight Conversions Operation(y/n):").lower()
            print("===========================================")
            if terminate =='y':
                break

    elif conv_type == 3:
        while True :
            print("===========================================")
            transform = input("""a. Celsius → Fahrenheit
                             b. Fahrenheit → Celsius
                             Select option(a,b): """)
            print("===========================================")
            if transform not in ['a','b']:
                print("===========================================")
                print("Invalid option please select the valid one!!")
                print("===========================================")
                continue
            elif transform == 'a' :
                print("===========================================")
                Celsius = float(input("enter the Celsius value :"))
                print("===========================================")
                print(f"{Celsius} Celsius = {(9*Celsius)/5 + 32} Fahrenheit")
                print("===========================================")
            else :
                print("===========================================")
                Fahrenheit = float(input("enter the Fahrenheit value :"))
                print("===========================================")
                print(f"{Fahrenheit} Fahrenheit = {5*(Fahrenheit- 32)/9} Celsius")
                print("===========================================")
        
            terminate = input("Want to close the 3. Temperature Conversions Operation(y/n):").lower()
            print("===========================================")
            if terminate =='y':
                break
        
    else :
        print("===========================================")
        print("Invalid option please select the valid one!!")
        print("===========================================")
        continue



