from bs4 import BeautifulSoup
import requests

habr_link = 'https://habr.com'

# response = requests.get(url)
# response.raise_for_status()
# soup2 = BeautifulSoup(response.text, "html.parser")

def make_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

# здесь названиt первой статьи на стр
def get_first_title(url):
    soup = make_soup(url)
    first_title = soup.find('a', 'tm-title__link').text
    return first_title

# ссылка на первую статью
def get_first_link(url):
    soup = make_soup(url)
    tag = soup.find('a', 'tm-title__link')
    href = tag.get('href')
    first_link = habr_link + href
    return first_link

def get_title_from_link(url):
    soup = make_soup(url)
    title = soup.find('h1', 'tm-title tm-title_h1').text
    return title

# здесь все названия статей на стр
def get_titles_list(url):
    soup = make_soup(url)
    all_titles = soup.find_all('a', 'tm-title__link')
    titles_list = [title.text for title in all_titles]
    return titles_list

# лист ссылки на все статьи на стр
def get_links_list(url):
    soup = make_soup(url)
    tag = soup.find_all('a', 'tm-title__link')
    links_list = [habr_link + link.get('href') for link in tag]
    return links_list

# url = 'https://habr.com/ru/news/762580/'
# i = get_title_from_link(url)
# print(i)
# print(first_art)