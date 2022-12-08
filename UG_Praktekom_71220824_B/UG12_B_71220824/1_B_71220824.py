print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
x = int(input("Masukan Angka : "))
print("")
print("")
print(' '*(x-2),"*")
for y in range ((x-2),0,-1):
    print(' '*(y-1),"**")
print("**"*x)