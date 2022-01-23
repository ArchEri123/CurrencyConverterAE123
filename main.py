import requests, json
import sys

#add functionality for ISO codes, direct currency codes, or currency name
#add flags at line ~95?

#gets URL for country exchange rates
url = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=c6029f50-68cb-11ec-9ff0-3708e9297674")
text = url.text
data = json.loads(text)


#gets URL for country and its currency code for more user-friendly input
urlcode = requests.get("https://pkgstore.datahub.io/core/currency-codes/codes-all_json/data/029be9faf6547aba93d64384f7444774/codes-all_json.json")
#print("Title 'PNG' @ 'https://tinyurl.com/currpng'")
countryCode = input("Enter the country name (Converts from USD): ")
codetext = urlcode.text
codedata = json.loads(codetext)


#lists that help for user selection when a country has more than one currency
currencies = []
currency_codes = []


#list of unsupported currencies based on user input
unsupported_currencies = []
unsupported_codes = []


#i helps track if given country exists
i = 0


#checks country
for row in codedata:
  #sees if country matches current row
  if row['Entity'] == countryCode.upper():
    #check if currency is supported
    try:
      currency_data = data['data'][row['AlphabeticCode']]
      currencies.append(row['Currency'])
      currency_codes.append(row['AlphabeticCode'])
    except KeyError as error:
      unsupported_currencies.append(row['Currency'])
      unsupported_codes.append(row['AlphabeticCode'])
      pass
  else:
    i += 1

#removes any duplicates
proper_unsupported_currencies = list(set(unsupported_currencies))
proper_unsupported_codes = list(set(unsupported_codes))


unsupported_i = 0
if len(currencies) == 0:
  #ends program if country does not exist
  if i == 441:
    sys.exit(f'--- "{countryCode.lower().capitalize()}" could not be found in the converter database ---\n\n\n')

  #ends program if country has no supported currencies
  else:
    print(f"This is a list of all currencies in {countryCode.lower().capitalize()} (None of them work with this converter): ")
    for i in proper_unsupported_currencies:
        print(f"{i} ({proper_unsupported_codes[unsupported_i]})", end = "; ")
    sys.exit(f'\n--- None of the currencies in "{countryCode.lower().capitalize()}" are compatible with this converter ---\n\n\n')
    


    

#removes any duplicates
proper_currencies = list(set(currencies))
proper_currency_codes = list(set(currency_codes))

#checks how many currencies the given countr has
currency_count = len(proper_currencies)

#conditional that lets user decide which currency (if more than 1) they want to convert to

if currency_count > 1:
  print(f"There seems to be more than one currency in {countryCode}. Here are the currencies found: ")
  for i in proper_currencies:
    count = proper_currencies.index(i)
    print(f"Currency #{count+1}: {i} ({proper_currency_codes[count]})")
  correct_currency = input("Please enter the correct currency CODE to convert to.")
  if correct_currency in proper_currency_codes:
    value = input("enter USD to convert from: ")
    country_data = data['data'][correct_currency]
    value_to_int = int(value)
    country_lower = countryCode.lower()
    currect_currency_name = proper_currencies[currency_codes.index(correct_currency)]
    print(f"${value} USD to currency in {country_lower.capitalize()} is approximately {round(country_data*value_to_int)} {correct_currency_name}s.")
  else:
    print(f"{correct_currency} is invalid.")
    #MAKE FLAGS



#takes USD to convert 
try: 
  value = input("enter how many USD to convert from: ")
  country_data = data['data'][currency_codes[0]]
  value_to_int = int(value)
  country_lower = countryCode.lower()
except ValueError:
  print("Invalid USD input.")

#conversion completes, program ends
print(f"${value} USD to currency in {countryCode.capitalize()} is approximately {round(country_data*value_to_int)} {currencies[0]}s.")
  

    




k

