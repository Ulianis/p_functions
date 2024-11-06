# task1

def text(): 
    print('''"Don't compare yourself with anyone in this world… 
if you do so, you are insulting yourself." 
                                             Bill Gates''' )

# text()


# task2

def chisla(num1, num2):
    for i in range(num1+1, num2): 
        if i%2==0 :
            print(i)
# chisla(1, 10)


# task3

def square(storona, zapolnen):
    print(storona * '*')    
    for i in range(storona-2):
        if zapolnen:  
            print(storona * '*')
        else: 
            print('*' + (storona-2)*' ' + '*')
    print(storona * '*') 
# square(5, False)

# task4

def minimum(num1,num2,num3,num4,num5):
    numbers = [num1,num2,num3,num4,num5]
    return min(numbers)
# print(minimum(1,6,10,-5,3))

# task5

def product(nachalo, konets):
    start = nachalo
    end = konets
    if nachalo > konets:
        end=nachalo 
        start=konets
    prod=1
    for i in range(start, end+1):
        prod=i*prod
    return prod
# print(product(2,4))

# task6

def kolvo(chislo):
    return len(str(chislo))
# print(kolvo(123456))

# task7
def palidrom(chislo):
    new_str = str(chislo)
    return new_str[::-1] == new_str 
print(palidrom(456325))