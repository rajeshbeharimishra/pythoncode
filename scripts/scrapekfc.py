import requests
from bs4 import BeautifulSoup

# URL of the webpage containing KFC store locations
url = 'https://locations.burgerking.co.uk/aberdeen'

# Send an HTTP request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find store elements
    store_elements = soup.find_all('div', class_='restaurant__card')

    for store in store_elements:
        # Extract store address
        address = store.find('h3', class_='restaurant__name').text.strip()

        # Extract coordinates if available
        coordinates_element = store.find('a', class_='c-button')
        if coordinates_element:
            # Extract X/Y coordinates
            coordinates_url = coordinates_element['href']
            x_y_coordinates = coordinates_url.split('=')[-1].split(',')
            x_coordinate, y_coordinate = x_y_coordinates[0], x_y_coordinates[1]
        else:
            x_coordinate, y_coordinate = None, None

        # Print store details
        print("Address:", address)
        print("X Coordinate:", x_coordinate)
        print("Y Coordinate:", y_coordinate)
        print()

else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
