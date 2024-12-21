    import requests
    from bs4 import BeautifulSoup

    # URL of the website to scrape
    url = 'https://www.mastercard.co.in/en-in.html'

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and print the title of the webpage
        title = soup.title
        print('Title:', title.text)
        print('Title:', title.text)

        # Find and print other information from the webpage
        # Example: Extract all the links on the page
        print('Links on the page:')
        for link in soup.find_all('a'):
            print(link.get('href'))
        for meta in soup.find_all('meta'):
            print(meta.get('name'))
        # You can further navigate the HTML structure to extract specific information

    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
