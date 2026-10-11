def menu():
    print()
    try:
        return input("Entre '+' to find sum of numbers \n"
        "Entre '-' to find sub of numbers \n"
        "Entre '*' to find product of numbers \n"
        "Entre '/' to find division of numbers \n"
        "Entre '0' to Exit the calculator : ")             
    except ValueError:
        print('Entre a Valid choice')

def add(*args):
    total = 0
    for numnbers in args:
        total += numnbers
    return total

def sub(*args):
    total = args[0]
    for numnbers in args[1:]:
        total -= numnbers
    return total

def mul(*args):
    total = 1
    for numnbers in args:
        total *= numnbers
    return total

def div(*args):
    total = args[0]
    for numnbers in args[1:]:
        total /= numnbers
    return total   

print()
print('================================')
print('======WELCOME TO CALCULATOR=====')
print('================================')
while True:
    u = menu()
    match u:
         case '+':
                 add_numbers = []
                 while True:
                     add_n = input("Entre numbers you want to find sum of and Entre '=' to calculate : ")
                     if add_n == '=':
                        break
                     add_numbers.append(int(add_n))
                 print(add(*add_numbers))          
         case '-':
                 sub_numbers = []
                 while True:
                     sub_n = input("Entre numbers you want to find subtractions of and Entre '=' to calculate : ")
                     if sub_n == '=':
                        break
                     sub_numbers.append(int(sub_n))
                 print(sub(*sub_numbers))            
         case '*':
                 mul_numbers = []
                 while True:
                     mul_n = input("Entre numbers you want to find product of and Entre '=' to calculate : ")
                     if mul_n == '=':
                        break
                     mul_numbers.append(int(mul_n))
                 print(mul(*mul_numbers))            
         case '/':
                 div_numbers = []
                 while True:
                     div_n = input("Entre numbers you want to find divisors of and Entre '=' to calculate : ")
                     if div_n == '=':
                        break
                     div_numbers.append(int(div_n))
                 print(div(*div_numbers))            
         case '0':
                 print('Thanks for using the calculator❤')
                 print('See you later☺')
                 break
         case _:
                 print('Entre a valid option from menu')        
