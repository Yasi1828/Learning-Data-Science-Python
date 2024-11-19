import requests
from bs4 import BeautifulSoup



# def Scraper(url):
    
File = open("out.csv","a") #appendmode
HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
url ='https://www.amazon.com/Travelers-Club-Luggage-Piece-Rose/dp/B07RS4PK3J/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.1faf5a75-f10d-481a-9299-d0fe2e7649bd&dib=eyJ2IjoiMSJ9.xtE2ygiQm_zdOslk9AxF-rhOrNeEtYOgBIK7jJAna4acUNBo292L1q6COzqiF8IoJKDzuL8yYm1w5ODUXF1lW8EJ8nzh42l2R2jigVkssGG1TbRL5Mz4E8Et7wdh_udQwpHPXAbznrWOxSjIVKMJWm_x21IcaklvN5H2QH8WeNZTP5IbPVRQqWHmjE79IzvsVjTX3XyfpiwI0tTNazGZ_ilhaAyd80L0DnAej_9P5p91fK0DhMoIopgKeQ2SzbPDbIbuohYEqNb04Atk-wMDSRRHMCGYlwtQKFhwzBcUhXQ.ZMlv46pS-z2vfbxJZ13QRoFIg8SFv282pUFlEu2I12Q&dib_tag=se&keywords=suitcases&pd_rd_r=b84f2b83-a09b-457e-a97d-59213c57e9ae&pd_rd_w=adlEj&pd_rd_wg=gNWai&pf_rd_p=1faf5a75-f10d-481a-9299-d0fe2e7649bd&pf_rd_r=FBTCTWC0GY0AV9TY0MWV&qid=1732008812&sr=8-2&th=1'


webpage = requests.get(url,headers=HEADERS)
soup = BeautifulSoup(webpage.content,'html.parser')
Title = soup.find('span',attrs={'id':'productTitle'})
print(Title.string) 
    
    
    
    
    
    