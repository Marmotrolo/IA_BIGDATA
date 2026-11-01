nombre=input("Dime tu nombre")
cesar=3

listanumerosdenombre= [chr(((ord(i)-96+cesar)%26)+96) for i in nombre ]

print(listanumerosdenombre)