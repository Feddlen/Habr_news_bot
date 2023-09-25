import my_parsing
import article

class Make_post():
    def __init__(self, url):       
        self.title = my_parsing.get_first_title(url)
        self.link = my_parsing.get_first_link(url)
        self.summary = article.final_summary(self.link)
        
    def __str__(self):
        return f'{self.title} \n\nПолный текст по ссылке:\n{self.link}\n\n{self.summary}'

    def __repr__(self):      
        return f'{self.title}, {self.link}'

class Make_post_link(Make_post):

    def __init__(self, link):
        self.title = my_parsing.get_title_from_link(link)
        self.link = link
        self.summary = article.final_summary(self.link)
       
class Get_tag_from_url():
    def __init__(self, url):
        if url == 'https://habr.com/ru/flows/develop/news/':
            self.tag = 'Разработка'
        elif url == 'https://habr.com/ru/flows/admin/news/':
            self.tag = 'Администрирование'
        elif url == 'https://habr.com/ru/flows/design/news/':
            self.tag = 'Дизайн'
        elif url == 'https://habr.com/ru/flows/management/news/':
            self.tag = 'Менеджмент'
        elif url == 'https://habr.com/ru/flows/marketing/news/':
            self.tag = 'Маркетинг'
        elif url == 'https://habr.com/ru/flows/popsci/news/':
            self.tag = 'Научпоп'
        elif url == 'https://habr.com/ru/news/':
            self.tag = 'Все потоки'
        else:
            self.tag = 'По ключевому слову'

    def __str__(self):
        return f'{self.tag}\n'

