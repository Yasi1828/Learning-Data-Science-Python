import requests
from bs4 import BeautifulSoup

def Scraper(url):
    # Open the file in append mode
    with open("out.csv", "a") as File:
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'
        }

        # Write the column names if the file is empty
        if File.tell() == 0:
            File.write("Product Name,Product Rating,Product Review Count\n")

        # Fetch the webpage
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, 'html.parser')

        # Extract product details
        Title = soup.find('span', attrs={'id': 'productTitle'})
        Title_string = Title.string.strip().replace(',', '') if Title else 'N/A'
        
        Rate = soup.find('span', attrs={'data-hook': 'rating-out-of-text'})
        Rate_string = Rate.string if Rate else 'N/A'
        
        Reviewcount = soup.find('span', attrs={'data-hook': 'total-review-count'})
        Reviewcount_string = Reviewcount.string.replace(',', '') if Reviewcount else 'N/A'

        # Write to the CSV file
        File.write(f"{Title_string},{Rate_string},{Reviewcount_string}\n")

        # Print the details
        print(f"Product Name: {Title_string}")
        print(f"Product Rating: {Rate_string}")
        print(f"Product Review Count: {Reviewcount_string}")

if __name__ == '__main__':
    urlFile = open("url.txt", 'r')
    
    for link in urlFile.readlines():
        Scraper(link.strip())  # Use strip() to remove any extra whitespace/newline
