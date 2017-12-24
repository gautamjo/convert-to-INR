from urllib.request import urlopen
import json
from prettytable import PrettyTable
import time
import sys

def open_txt_file(file):
    for text in file:
        print(text.strip())
        time.sleep(.5)

def fetch_base_currency(base):
    try:
        url = urlopen('http://api.fixer.io/latest?base=' + base)
        url_read = url.read().decode('utf-8')
        return url_read
    except TimeoutError:
        print('The program exited because it took an unusually long time to connect. \
        Kindly run the program again.')
        sys.exit()

def url_to_json(url):
    json_file = json.loads(url)
    return json_file

def get_keys(rates):
    keys = [key for key, val in rates.items() if key not in 'INR']
    keys.append('USD')
    return keys

def money_table(keys, currency_names):
    data = zip(keys, currency_names)
    table = PrettyTable(field_names=['Currency CODE', 'Currency NAME'])

    for d in data:
        table.add_row([d[0], d[1]])

    print(table.get_string(sortby='Currency CODE'))
    print()

def input_base():
    base = input('Enter currency code you wish to convert to INR: ').upper()
    return base

def currency_code(base):
    while True:
        keys = get_keys(rates)
    
        if base in keys:
            url = fetch_base_currency(base)
            json_file = url_to_json(url)

            rate = json_file['rates']
            inr = float(rate['INR'])
            return inr
        else:
            print('Enter valid Currency Code')
            continue

def exchange_rate_table(base, inr):
    table = PrettyTable(field_names=[base + ' to INR exchange rate as on', 'Rate'])
    table.add_row([json_file['date'], 'Rs. ' + str(inr)])
    print(table)
    print()
            
def convert_base_to_inr(base, inr):
    while True:
        try:
            tab = PrettyTable(field_names=[base, 'Amount in INR'])
            amount = float(input('Convert ' + base + ' to Rupees.\nEnter amount: '))
            converted_amount = amount * inr
            tab.add_row([amount, round(converted_amount, 2)])
            print(tab)
            break
        except ValueError:
            print("Please enter amount in digits")
            continue

def change_currency_code():
    while True:
        change_base = input('Do you wish to change currency code? Press Y or N: ').upper()
        if change_base.startswith('Y'):
            input_currency_code()
            ask_again()
        elif change_base.startswith('N'):
            break
        else:
            print('Press Y or N')

# opening intro text file
print()
file = open('test_file_cnvt_2_inr.txt', 'r')
open_txt_file(file)
print()

# setting up default values for base as USD to print all the available 
# currency codes and their respective names.
base_usd = 'USD'
setup_url = fetch_base_currency(base_usd)
json_file = url_to_json(setup_url)
rates = json_file['rates']
inr_rate = float(rates['INR'])

keys = get_keys(rates)
currency_names = ['Australian Dollar', 'Bulgarian Lev', 'Brazilian Real', 'Canadian Dollar', 'Swiss Franc',
                  'Chinese Yuan', 'Czech Koruna', 'Danish Krone', 'British Pound', 'Hong Kong Dollar', 'Croatian Kuna',
                  'Hungarian Forint', 'Indonesian Rupiah', 'Israeli New Shekel', 'Japanese Yen', 'South Korean Won',
                  'Mexican Peso', 'Malaysian Ringgit', 'Norwegian Krone', 'New Zealand Dollar', 'Philippine Peso',
                  'Polish Zloty', 'Romanian Leu', ' Russian Ruble', 'Swedish Krona', 'Singapore Dollar', 'Thai Baht',
                  'Turkish Lira', ' South African Rand', 'Euro', 'US Dollar']

money_table(keys, currency_names)
print()
# setting up user input values
base = input_base()
inr = currency_code(base)
exchange_rate_table(base, inr)
convert_base_to_inr(base, inr)

# setting up loops to ask for another convertion
while True:
    ask_again = input('Convert another amount? Press Y or N: ').upper()
    if ask_again.startswith('Y'):
        print()
        convert_base_to_inr(base, inr)
    elif ask_again.startswith('N'):
        break
    else:
        print('Press Y or N')

# setting up loop for change of currency code
while True:
    print()
    change_base = input('Do you wish change currency code? Press Y or N: ').upper()
    if change_base.startswith('Y'):
        base = input_base()
        inr = currency_code(base)
        exchange_rate_table(base, inr)
        convert_base_to_inr(base, inr)
        # setting up loops to ask for another convertion
        while True:
            ask_again = input('Convert another amount? Press Y or N: ').upper()
            if ask_again.startswith('Y'):
                print()
                convert_base_to_inr(base, inr)
            elif ask_again.startswith('N'):
                break
            else:
                print('Press Y or N')
    
    elif change_base.startswith('N'):
        break
    else:
        print('Press Y or N')

print()
print('Thank You for using Convert2INR. This program was made by chamber underground. \
Contact us at apps@chamberunderground.com')