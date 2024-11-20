import requests
from bs4 import BeautifulSoup



def Scraper(url):
    
    File = open("out.csv","a") 
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(webpage.content,'html.parser')
    Title = soup.find('span',attrs={'id':'productTitle'})
    Title_string =Title.string.strip().replace(',','')
    File.write(f"product name : {Title_string},\n")
    # WholePrice = soup.find('span',attrs={'class':'a-price-whole'})
    # File.write(f"{WholePrice},\n")
    Rate = soup.find('span',attrs={'data-hook':'rating-out-of-text'}).string
    File.write(f"product rating: {Rate},\n")
    Reviewcount = soup.find('span',attrs={'data-hook':'total-review-count'}).string.replace(',','')
    File.write(f"product review count: {Reviewcount},\n")
    
    File.close()
    # print(WholePrice)
    print(Title_string)
    print(Rate)
    print(Reviewcount)

if __name__ == '__main__':
    urlFile = open("url.txt",'r')
    
    for link in urlFile.readlines():
        Scraper(link)