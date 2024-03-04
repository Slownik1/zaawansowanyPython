def display_name(name):

    for x in name:
        print(x)

    name_lista = [x for name in name]

    print(name_lista)

def display_number(numbers):

    for n in numbers:
        if n%2==0:
            print(n)

def display_number_2(numbers):

    print(numbers[::2])

if __name__ == '__main__':

    #Zadanie 1

    name =['Dawid', 'Bartek', 'Ala', 'Kasia', 'Ania']

    #display_name(name)

    #Zadanie 2

    numbers=list(range(5))
    print(numbers)

    #display_number(numbers)

    display_number_2(numbers)