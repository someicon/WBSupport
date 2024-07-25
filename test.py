from string import punctuation

restricted_words = {'кабан', 'нворд'}
message = "Зд!!есь напи!сано сообщени!е "


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


print(clean_text(message))
