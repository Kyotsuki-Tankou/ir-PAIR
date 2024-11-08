import requests
from bs4 import BeautifulSoup

def garbage_abstract(url):
    response=requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        abstract_div = soup.find('div', {'class': 'abstract', 'id': 'abstract'})
        if abstract_div:
            abstract_text = (abstract_div.get_text(strip=True)).replace('Keywords:',' \\n Keywords:').replace('Abstract','Abstract\\n')
            # print(abstract_text)
            return abstract_text
        else:
            print(f"Abstract not found at url: {url}" )
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code} at url: {url}")
    return "ERROR ABSTRACT"