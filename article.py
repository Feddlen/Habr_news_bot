import parsing
import summary

# Функция для получения текста статьи по ссылке
def get_text_for_summary(url):
    soup = parsing.make_soup(url)
    all_title = soup.find_all("div", "tm-article-body")
    text = ""
    for i in all_title:
        text += i.text
    delim = '. '
    text_list = [x+delim for x in text.split(delim) if x]
    return text_list

# Функция разделения текста на части определеной длины для модели
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
    
# Функция генерации краткого содержания
def final_summary(url):
    text = make_pieces_for_summary(url)
    final_summary = [summary.make_summary(i) for i in text]
    final_summary = ' '.join(final_summary)
    return final_summary
