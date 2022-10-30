# Задание 1:
# Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'
#
# Задание 2:
# Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'
#
# Задание 3:
# Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.
#
# Задание 4:
# Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
#
# Задание 5:
# Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить, что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

# Task1
word = input('Enter word: ')
lower_word= word.lower()
if (lower_word[::1]) == (lower_word[::-1]):
    print('+')
else:
    print('-')

# Task2
text = input('Enter text: ')
word = input('Enter word: ')

if word in text:
    print('yes')
else:
    print('no')

# Task3
word = input('Enter word: ')

if word.startswith('abc'):
    new_word = word.replace('abc', 'www')
    print(new_word)
else:
    print(str(word) + 'zzz')

# Task4
word = input('Enter word: ')
alpha_word = ' '
if word.isalnum():
    for i in word:
        if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            alpha_word = alpha_word + i
    print(alpha_word)
else:
    print(word)

# Task5

email = str(input('Enter your email: '))

if email.count('@' and '.') == 1:
    addres_part = (email.split('@'))
    domain_part = str(addres_part[1]).split('.')
    if len(str(addres_part[0])) > 0 and len(str(domain_part[0])) > 0 and len(str(domain_part[1])) > 0:
        print(f'Email {email} is correct')
    else:
        print(f'Email {email} is Incorrect')
else:
    print(f'Email {email} is Incorrect')
