# Есть фрагмент текста, состоящий из предложений.
# Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным или восклицательным знаком (или несколькими такими знаками).
# Слова состоят только из латинских букв, разделяются отделяются пробелами или запятыми с пробелами.
# Предложение может состоять из одного слова.
# Составить предложение из первых слов предложений фрагмента.
# Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
# Предложение должно заканчиваться точкой.

# text = 'Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it`s difficult... Claro..'
# text2 = 'Holla....'
#
#
def get_sentenses_from_text(text: str) -> list:
    symbols = ['.', '!', '?']
    sentences = []
    sentence = ''
    for s in text:
        if s not in symbols:
            sentence += s
        else:
            sentences.append(sentence)
            sentence = ''
    return [sentence.strip() for sentence in sentences if sentence]


def get_first_word_from_sentence(sentence: str) -> str:
    first_word = ''
    for s in sentence:
        if s.isalpha():
            first_word += s
        else:
            break
    return first_word


def generate_sentence(text: str) -> str:
    result = ''
    words = [get_first_word_from_sentence(sentence) for sentence in get_sentenses_from_text(text)]
    if words:
        result = ' '.join(words).capitalize()
    return result + '.'


print(generate_sentence(text))
print(generate_sentence(text2))

import re

text = 'Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it`s difficult... Claro..'
text2 = 'Holla....'

regex = "^([A-Z][a-z]*)|[.!?] ([A-Z][a-z]*)|\n([A-Z][a-z]*)"


def generate_sentence(text: str) -> str:
    regex_obj = re.compile(regex)
    result = regex_obj.findall(text)
    filtered_list = []
    for i, value in enumerate(result):
        filtered_list += result[i]
    i = 0
    words_list = []
    for i in filtered_list:
        if i:
            words_list.append(i)
    j = 1
    result_words_list = [filtered_list[0]]
    while j < len(words_list):
        result_words_list.append(str(words_list[j]).lower())
        j += 1
    sentence = ' '.join(str(x) for x in result_words_list)
    sentence += '.'
    return sentence


print(generate_sentence(text))
print(generate_sentence(text2))
