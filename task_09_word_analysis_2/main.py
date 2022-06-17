def get_input_parameters():
    word_list = []
    word = input('Введите слово: ')
    word_list.append(word)
    return word_list



def display_result(is_palindrome):

    print(is_palindrome)



def check_palindrome(word):

    flag = False
    if word == word[:: -1]:
        flag = True
    else:
        print('Слово не является палиндромом')
    return flag
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
