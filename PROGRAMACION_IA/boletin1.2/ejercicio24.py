from datetime import datetime

def sumaendiaslaborables (*numeros):
    if (datetime.today().weekday() >4):
        print("No son dias laborables")
    else:
        return sum(numeros)

print(sumaendiaslaborables(2,5,4,3,2,4,6,7,4,3,3))