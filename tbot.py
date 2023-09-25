import telebot
from telebot import types
import class_post
import time
import my_parsing

token = '6329148877:AAFC-4Z2Ju-n4go8N9tQG-Gbxm2hgvSgn_o'
bot = telebot.TeleBot(token)
develop_source = 'https://habr.com/ru/flows/develop/news/'
admin_source = 'https://habr.com/ru/flows/admin/news/'
design_source = 'https://habr.com/ru/flows/design/news/'
management_source = 'https://habr.com/ru/flows/management/news/'
marketing_source = 'https://habr.com/ru/flows/marketing/news/'
popsci_source = 'https://habr.com/ru/flows/popsci/news/'
all_source = 'https://habr.com/ru/news/'
source = []

@bot.message_handler(commands = ['start'])
def start_message(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	settings = types.KeyboardButton("Выбор источника новостей")
	auto_posting = types.KeyboardButton("Начать авто-постинг")
	markup.add(settings, auto_posting)
	bot.send_message(message.chat.id,'Привет, выбери настройки бота или запусти авто-постинг\nПо умолчанию источник - Все потоки', reply_markup = markup)

@bot.message_handler(func=lambda message: message.text=='Выбор источника новостей')
def flow_selection(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Все потоки") 
	item2 = types.KeyboardButton("Разработка")
	item3 = types.KeyboardButton("Администрирование")
	item4 = types.KeyboardButton("Дизайн")
	item5 = types.KeyboardButton("Менеджмент")
	item6 = types.KeyboardButton("Маркетинг")
	item7 = types.KeyboardButton("Научпоп")
	item8 = types.KeyboardButton("По ключевому слову")
	item9 = types.KeyboardButton('Удалить источник')
	item10 = types.KeyboardButton('Назад')
	markup.add(item7, item2, item3, item4, item5, item6, item1, item8, item9, item10)
	bot.send_message(message.chat.id,'Выбери откуда получать новости', reply_markup = markup)

@bot.message_handler(func=lambda message: message.text=='Назад')
def return_menu(message):
	markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	settings = types.KeyboardButton("Выбор источника новостей")
	auto_posting = types.KeyboardButton("Начать авто-постинг")
	markup1.add(settings, auto_posting)
	bot.send_message(message.chat.id,'выбери настройки бота или запусти авто-постинг', reply_markup = markup1)

@bot.message_handler(func=lambda message: message.text=='По ключевому слову')
def personal(message):
	msg = bot.send_message(message.chat.id, 'Введите ключевое слово')
	bot.register_next_step_handler(msg, make_personal_url)

def make_personal_url(words):
	words_txt = words.text
	words_txt = words_txt.split()
	words_txt = '%20'.join(map(str, words_txt))
	personal_source = ['https://habr.com/ru/search/?q=','&target_type=posts&order=date']
	personal_url = personal_source[0] + words_txt + personal_source[1]
	source.append(personal_url)

@bot.message_handler(func=lambda message: message.text=='Удалить источник')
def delete_smt(message):
	list_source = [class_post.Get_tag_from_url(url) for url in source]
	msg = bot.send_message(message.chat.id, f'Что удалить?\n{list_source}')
	bot.register_next_step_handler(msg, del_from_source)

# тут добавить обработку исключения на ввод слова, которого нет в списке
# не удалить по ключу
def del_from_source(message):
	source.list.remove(message)

@bot.message_handler(func=lambda message: message.text=='Разработка')
def develop_app(message):
	source.append(develop_source)

@bot.message_handler(func=lambda message: message.text=='Администрирование')
def admin_app(message):
	source.append(admin_source)

@bot.message_handler(func=lambda message: message.text=='Дизайн')
def design_app(message):
	source.append(design_source)

@bot.message_handler(func=lambda message: message.text=='Менеджмент')
def manag_app(message):
	source.append(management_source)

@bot.message_handler(func=lambda message: message.text=='Маркетинг')
def market_app(message):
	source.append(marketing_source)

@bot.message_handler(func=lambda message: message.text=='Научпоп')
def pop_app(message):
	source.append(popsci_source)

@bot.message_handler(func=lambda message: message.text=='Начать авто-постинг')
def menu(message):
	if len(source) == 0:
		source.append(all_source)
	#bot.send_message(message.chat.id, text=source)
	first_posts = ["1" for i in range(len(source))]
	for indx, url in enumerate(source):
		post1 = class_post.Make_post(source[indx])
		first_posts[indx] = post1.link
		bot.send_message(message.chat.id, text = f'Источник: {class_post.Get_tag_from_url(source[indx])}\n{post1}')

	while(True):
		# НЕ ЗАБЫТЬ ПОМЕНЯТЬ НА ПОЛЧАСА
		time.sleep(5)
		for indx, url in enumerate(source):	
			list_link = my_parsing.get_links_list(source[indx])
			list_link.reverse()
			if first_posts[indx] == class_post.Make_post(source[indx]).link:
				bot.send_message(message.chat.id, text = f'{class_post.Get_tag_from_url(source[indx])}Новыx новостей нет')
				continue

			for index, linki in enumerate(list_link):
				if list_link[index - 1] == first_posts[indx]:
					post1 = class_post.Make_post_link(list_link[index])
					first_posts[indx] = class_post.Make_post_link(list_link[index]).link
					bot.send_message(message.chat.id, text = f'Источник: {class_post.Get_tag_from_url(source[indx])}\n{post1}')
			
bot.infinity_polling(timeout = 5, long_polling_timeout = 10)

