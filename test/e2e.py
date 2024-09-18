import requests
from bs4 import BeautifulSoup
import sys

def test_scores_service(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        score = soup.find(id='score').text

        if score.isdigit() and 1 <= int(score) <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main_function():
    url = 'http://localhost:5000'
    if test_scores_service(url):
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == '__main__':
    main_function()
