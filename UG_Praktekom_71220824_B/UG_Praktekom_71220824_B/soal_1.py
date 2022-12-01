print("Select operation.")
print("1. add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
option = input("Enter choice (1/2/3/4): ")

if option == '1':
    x1 = float(input("Enter first number : "))
    x2 = float(input("Enter second number : ")) 
    def add():
        tambah = float(x1 + x2)
        print (x1, "+", x2, "=", tambah)
    add()

elif option == '2':
    x3 = float(input("Enter first number : "))
    x4 = float(input("Enter second number : ")) 
    def subtract():
        kurang = float(a3 - a4)
        print (x3, "-", x4, "=", kurang)
    subtract()

elif option == '3':
    x5 = float(input("Enter first number : "))
    x6 = float(input("Enter second number : ")) 
    def multiply():
        bagi = float(x5 * x6)
        print (x5, "*", x6, "=", bagi)
    multiply()

elif option == '4':
    x7 = float(input("Enter first number : "))
    x8 = float(input("Enter second number : ")) 
    def divide():
        kali = float(x7 / x8)
        print (x7, ":", x8, "=", kali)
    divide()
else :
    print("error")

    