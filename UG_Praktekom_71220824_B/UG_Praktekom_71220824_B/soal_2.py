print ("Alat Pengecek Palindrome")
print ("Masukan kata anda")
x = str(input(">> "))
print ("")
def funPalindrome():
    if x == x[::-1]:
        print ("Yes")
        print ("Jika dibalik ",x[::-1])
    else:
        print ("No")
        print ("Jika dibalik ",x[::-1])

funPalindrome()