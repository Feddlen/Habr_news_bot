import my_parsing
import summary

url = "https://habr.com/ru/news/763052/"

def get_text_for_summary(url):
    soup = my_parsing.make_soup(url)
    all_title = soup.find_all("div", "tm-article-body")
    text = ""
    for i in all_title:
        text += i.text
    delim = '. '
    text_list = [x+delim for x in text.split(delim) if x]
    return text_list

def make_pieces_for_summary(url):
    text_list_all = get_text_for_summary(url)
    one_piece = ''
    all_pieces = []
    for i in range(0, len(text_list_all)):
        if len(text_list_all[i]) > 600:
            text_slice = text_list_all[i]
            text_slice = text_slice[:599]
            all_pieces.append(text_slice)
            continue

        if (len(one_piece) + len(text_list_all[i])) <= 600:
            one_piece += text_list_all[i]
            continue

        all_pieces.append(one_piece)
        one_piece = text_list_all[i]

    all_pieces.append(one_piece)
    return all_pieces

def final_summary(url):
    text = make_pieces_for_summary(url)
    final_summary = [summary.make_summary(i) for i in text]
    final_summary = ' '.join(final_summary)
    return final_summary

# text = ['Нервная клетка глазами художника. Исследователи из Германии, Канады, Испании и США опубликовали результаты всестороннего изучения количества отдельных клеток каждого типа в типичном организме.', 'Российские ученые обнаружили связь между количеством клеток и биомассой. По их мнению, если разделить клетки на категории по их размеру, то каждая из них вносит примерно одинаковый вклад в массу тела.', 'В организме возможно наличие компромисса между размером и количеством клеток и предполагают существование гомеостаза размеров клеток разных типов.', 'По данным исследователей, размеры наших клеток идеально соответствуют их различным функциям, и любое нарушение этой шкалы часто свидетельствует о наличии заболевания.']
# print(''.join(text))

# l = make_pieces_for_summary(url)
# for i in l:
#     print(len(i))
#print(len(l))
# print('sum len l\n', sum(map(len, l)))