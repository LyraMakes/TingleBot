import requests
import time
import random
from bs4 import BeautifulSoup

# Constant Definitions
URL = "https://www.amazon.com/kindle-dbs/entity/author/B00SF2MTYK?_encoding=UTF8&node=283155&offset=0&pageSize=1000&searchAlias=stripbooks&sort=author-sidecar-rank&page=1&langFilter=default#formatSelectorHeader"

# List of book images
books = []


def wait_for(secs: int):
  for i in range(secs):
    print(secs - i, end="\r")
    time.sleep(1)


def request_page(url: str, recursion=1):
  print("Attempt {0} of retrieving page: {1}".format(recursion, url))
  page = requests.get(url)
  print("HTTP Status Response code: {0.status_code}".format(page))
  if page.status_code == 200:
    return page
  elif page.status_code == 404:
    print("Status code 404: Retrying in 30 seconds")
    wait_for(30)
    return request_page(url, recursion + 1)
  else:
    print("Error code {0.status_code} received".format(page))
    raise Exception


def update_imgs() -> type(None):
  page = request_page(URL)
  page_soup = BeautifulSoup(page.content, 'html.parser')

  search_results = page_soup.find(id="searchWidget")

  img_list = search_results.find_all('img')

  global books
  books = [img['src'] for img in img_list]


def get_img() -> str:
  global books
  if not books:
    update_imgs()
  return random.choice(books)
