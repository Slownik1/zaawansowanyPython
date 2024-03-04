
def say_hi(name, surname):
    return f"Cześć {name} {surname}"

def multiply(x, y):
    return x*y

def is_even(number):
    return number%2==0

def chack_triangle(x, y, z):
    return x+y>=z

def check_list(list, value):
    return value in list

def marge_list(list1, list2):
    list_tmp = list1+list2
    list_tmp=list(set(list_tmp))
    list_tmp = [element ** 3 for element in list_tmp]
    return list_tmp

if __name__ == '__main__':

    say_hi_result = say_hi('Dawid', 'Białek')
    print(say_hi_result)

    print(multiply(2, 4))

    is_even_result = is_even(2)
    if(is_even_result):
        print("Parzysta")
    else:
        print("Nieparzysta")

    print(chack_triangle(3,2,6))

    list1=[2,3,4,5,6]
    print(check_list(list1, 10))

    list2=[2, 5, 6, 3]
    print(marge_list(list1, list2))