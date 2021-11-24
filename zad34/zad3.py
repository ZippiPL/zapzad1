api_url = 'https://api.openbrewerydb.org/breweries.json'
"""import request"""
import json

def print_hi(name,surname) :
    print(f'Cześć, {name} {surname}!')

def multiplay(number_one , number_sec) -> int:
    return number_one*number_sec

def check_even(number) -> bool:
    return (number % 2 == 0)

def write_check_even(yes_no):
    if yes_no == True:
        print('Liczba Parzysta')
    else:
        print('Liczba Nieparzysta')

def check_if_bigger_smaller(liczba: int,liczbaa: int,liczbaaa: int) -> bool:
    suma = liczba + liczbaa
    if suma >= liczbaaa:
        return True
    else:
        return False

def check_avail(lista: list,number: int) -> bool:
    if lista.__contains__(number) == True:
        print("Zawiera")
    else:
        print("Niezawiera")
        return False

def check_avail_square(lista: list,listaa: list)-> list:
    duzalista = lista + listaa
    duzalista = list(dict.fromkeys(duzalista))
    return duzalista

def request_to_api():
   """" response = requests.get(api_url)
    print(response.status_code)
    print(response.json())

    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    jprint(response.json())

class Brawery(object):
    def __init__(self,api_url):

     id: int
     obdb_id: str
     name: str
     brewery_type: str
     street: str
     address_2: str
     address_3: str
     city: str
     state: str
     county_province: str
     postal_code: int
     country: str
     longitude: float
     latitude: float
     phone: int
     website_url: str
     updated_at: datetime
     created_at: datetime
     """
"""

"""
if __name__ == '__main__':
    print_hi('Denis','Duda')
    print(multiplay(5,5))
    check_even_variable_numer_one = check_even(4)
    check_even_variable_numer_two = check_even(5)
    print(check_if_bigger_smaller(1,2,3))
    print(check_if_bigger_smaller(1,2,5))
    write_check_even(check_even_variable_numer_one)
    write_check_even(check_even_variable_numer_two)
    check_avail([3,4,5],2)
    check_avail([3, 4, 5], 4)
    print(check_avail_square([1,2,3,4,5,6,6,6,6,6,6,7, 8 , 1 , 2 , 3 ,],[12,2,1,5]))
    request_to_api()