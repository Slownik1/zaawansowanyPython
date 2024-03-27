import argparse

import requests
from brawery import Brawery


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


def getBrawery(city):

    URL='https://api.openbrewerydb.org/v1/breweries'

    if city!=None:
        URL += f'?by_city={city}'
    else:
        URL += '?per_page=20'

    response = requests.get(URL)

    if (response.status_code==200):
        data = response.json()
        list_of_brawery = [Brawery(brawery) for brawery in data]
        for brawery in list_of_brawery:
            print(brawery)
    else:
        print("Error")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='Python',
        description='Python',
        epilog='Input city')
    parser.add_argument('--city', help='Specify citys', default=None)
    args = parser.parse_args()

    say_hi_result = say_hi('Dawid', 'Białek')
    print(say_hi_result)

    print(multiply(2, 4))

    is_even_result = is_even(2)
    if (is_even_result):
        print("Parzysta")
    else:
        print("Nieparzysta")

    print(chack_triangle(3, 2, 6))

    list1=[2, 3, 4, 5, 6]
    print(check_list(list1, 10))

    list2=[2, 5, 6, 3]
    print(marge_list(list1, list2))

    getBrawery(args.city)
