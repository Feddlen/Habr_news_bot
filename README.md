# Habr_news_bot
## Описание
Бот парсит новости с хабра по выбранным топикам, если появилась новая статья, то парсит текст статьи и генерирует краткое описание с помощью обученой модели с HuggingFace.
- Ссылка на модель - [MBARTRuSumGazeta](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)

## Используемые библиотеки
telebot, requests, BeautifulSoup, transformers, time

## Как использовать
Отправьте боту команду /start, чтобы начать взаимодействие. Выберите одну из следующих опций:

- "Начать авто-постинг" - По умолчанию будет выбран источник "Все потоки"
- "Выбор источника новостей" - Выбор одного или нескольких сточников "Разработка", "Администрирование" и тд.

### Пример работы бота

![image](https://github.com/Feddlen/Habr_news_bot/assets/128243078/5afecc36-2cb1-4055-a9ab-9e1caa4a23db)


  
