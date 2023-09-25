import my_parsing
import article

class Make_post():
    def __init__(self, url):       
        self.title = my_parsing.get_first_title(url)
        self.link = my_parsing.get_first_link(url)
        self.summary = article.final_summary(self.link)
        #self.title = 'Биологи нашли неожиданную закономерность в распределении клеток в теле человека'
        #self.link = 'https://habr.com/ru/news/762580/'
        #self.summary = 'Нервная клетка глазами художника. Исследователи из Германии, Канады, Испании и США опубликовали результаты всестороннего изучения количества отдельных клеток каждого типа в типичном организме. Российские ученые обнаружили связь между количеством клеток и биомассой. По их мнению, если разделить клетки на категории по их размеру, то каждая из них вносит примерно одинаковый вклад в массу тела. В организме возможно наличие компромисса между размером и количеством клеток и предполагают существование гомеостаза размеров клеток разных типов.По данным исследователей, размеры наших клеток идеально соответствуют их различным функциям, и любое нарушение этой шкалы часто свидетельствует о наличии заболевания.'
    
    def __str__(self):
        return f'{self.title} \n\nПолный текст по ссылке:\n{self.link}\n\n{self.summary}'

    def __repr__(self):      
        return f'{self.title}, {self.link}'

class Make_post_link(Make_post):

    def __init__(self, link):
        self.title = my_parsing.get_title_from_link(link)
        self.link = link
        self.summary = article.final_summary(self.link)
        #self.summary = 'Нервная клетка глазами художника. Исследователи из Германии, Канады, Испании и США опубликовали результаты всестороннего изучения количества отдельных клеток каждого типа в типичном организме. Российские ученые обнаружили связь между количеством клеток и биомассой. По их мнению, если разделить клетки на категории по их размеру, то каждая из них вносит примерно одинаковый вклад в массу тела. В организме возможно наличие компромисса между размером и количеством клеток и предполагают существование гомеостаза размеров клеток разных типов.По данным исследователей, размеры наших клеток идеально соответствуют их различным функциям, и любое нарушение этой шкалы часто свидетельствует о наличии заболевания.'

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

# link = 'https://habr.com/ru/news/762580/'
# url = 'https://habr.com/ru/news/'
# post = Make_post(url)
# print(post)
# post1 = Make_post_link(link)
# print(post1)
