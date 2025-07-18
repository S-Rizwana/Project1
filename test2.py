from bs4 import BeautifulSoup
import requests

url = "https://internshala.com/job/detail/remote-product-marketeer-fresher-jobs-at-hotnot1686567005"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify()[:1000])  # Print first 1000 characters of the page