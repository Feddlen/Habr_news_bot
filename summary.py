from transformers import MBartTokenizer, MBartForConditionalGeneration

# article_tex = """""Циркуль и линейка. Часть 1 Всем привет!
# Как-то раз мне захотелось сделать анимацию построения фигуры циркулем и линейкой. Немного погуглив, оказалось, что на английском compass это ещё и циркуль, и что подходящего готового решения нет.
# Всё дальнейшее вылилось в эту статью.Короткое предисловие
# Статью я разделил на две части. В первой — реализация циркуля и линейки, а во второй уже создание анимации на основе написанных классов.
# Сразу проясню некоторые моменты. Писать я буду на python, потому что нужная мне библиотека для анимации (ссылка на неё в конце) написана на нёмi."""

model_name = "IlyaGusev/mbart_ru_sum_gazeta"
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

def make_summary(article_text):
    input_ids = tokenizer(
    [article_text],
    max_length=600,
    padding="max_length",
    truncation=True,
    return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(input_ids=input_ids, no_repeat_ngram_size=4)[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary

# test = make_summary(article_tex)
# print(test)