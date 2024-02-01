import sys
import requests
from bs4 import BeautifulSoup
import db_connect
from pymongo.errors import DuplicateKeyError

# Get the current working directory
current_path = sys.path[0]
print(f"Current working directory: {current_path}")

# URL of the Wikipedia page containing the list of most populous municipalities in Belgium
url = 'https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population'

# Send an HTTP GET request to the URL and parse the content with BeautifulSoup
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Select relevant HTML tags within the page
rows = soup.select('table.wikitable tr')[1:]  # Start from 1 as the first row contains headers

city_list = []

# Iterate over each row to extract municipality names and population information
for row in rows:
    columns = row.select('td')

    # Check if the row contains information about a municipality
    if columns:
        city = columns[1].select_one('a').text
        flag_element = columns[1].select_one('img')
        flag = flag_element['src'] if flag_element and 'src' in flag_element.attrs else None
        province = columns[2].text.strip() if columns[2].text.strip() else None

        population = columns[3].text.strip().replace(',', '')  # Remove commas and spaces from the population data
        population = int(population) if population.isdigit() else None  # Convert population to integer (set to None if not numeric)

        # Store the extracted data in a dictionary
        city_data = {'country': 'Germany', 'province': province, 'flag': flag, 'city': city, 'population': population}
        city_list.append(city_data)

# Add the country information to the formatted data before inserting into the MongoDB collection
formatted_data = {'Germany': city_list}

print(formatted_data)

# Connect to the MongoDB database
db_connection = db_connect.get_db_connection()

# Check if data for this country already exists in the collection before insertion
existing_data = db_connection.find_one({'Germany': {'$exists': True}})

if existing_data:
# If the country already exists, you may decide whether to update or skip the insertion
        print(f"Data for {formatted_data.keys()} already exists in the database.")
else:
        try:
# Insert data into the database
                db_connection.insert_one(formatted_data)
                print(f"Inserted data for {formatted_data.keys()} into the database.")
        except DuplicateKeyError:
# If the same data already exists (duplicate key), ignore the error
                print(f"Data for {formatted_data.keys()} already exists in the database.")
