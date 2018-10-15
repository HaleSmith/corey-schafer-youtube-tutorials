# References https://www.youtube.com/watch?v=9N6a-VLBa2I
# Code at https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-JSON
# References https://docs.python.org/3/library/json.html
# JavaScript Object Notation
# JSON is a common data format for storing data
# Usually from online APIs or from configuration files
# Module parses json data into a dict
# Tutorial used Yahoo finance API, which was out of order
# Uses https://www.alphavantage.co/documentation/ as API
import json

# Valid JSON data in a Python string
people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section("Load JSON data from text")
data = json.loads(people_string)
print(f"Raw loaded date prints to: {data}")
print(f"Data type: {type(data)}")
print(f"Data type of people: {type(data['people'])}")

new_section("Looping over objects")
for person in data['people']:
    print(person['name'])

new_section("Remove phone number then convert back to JSON")
for person in data['people']:
    del person['phone']
# Indents each level 2 spaces, and field keys are sorted
# Emails before has_license, before name
# .dumps: dump to string
new_string = json.dumps(data, indent=2, sort_keys=True)
print(f"New string: \n {new_string}")

new_section("Loading from file states.json with selected fields")
with open('states.json') as f:
    data = json.load(f)
    for state in data['states']:
        print(state['name'], state['abbreviation'])

new_section("Writing to a new file with some data removed")
with open('states.json') as f:
    data = json.load(f)
    for state in data['states']:
        del state['area_codes']
    with open('new_states.json', 'w') as f:
        json.dump(data, f, indent=2)
print("See new_states.json")

new_section("Reading from an API")
from urllib.request import urlopen
# Alternate API used since tutorial API didn't work
with urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
             "&symbol=MSFT&apikey=demo") as response:
    source = response.read()
print(f"Downloaded data string:\n{source}")
data = json.loads(source)  # Now is a JSON object
print(f"\nData dumped to indented string:\n{json.dumps(data, indent=2)}")
print(f"\nNumber of entries in list: {len(data['Time Series (Daily)'])}\n")
open_prices = dict()
for date in data['Time Series (Daily)']:  # Extract date vs open price
    open_price = float(data['Time Series (Daily)'][date]['1. open'])
    print(f"Date: {date}, open price: ${open_price}")
    open_prices[date] = open_price
print(f"\nOpen price on 20180822: {open_prices['2018-08-22']}")



