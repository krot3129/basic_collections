def get_input_parameters():

    string = input('Введите слово: ')
    string_list = list(string)
    return string_list



def display_result(number_unique_letters):

    print('Количество уникальных букв в слове:', number_unique_letters)



def count_number_unique_letters(word):

    text = []
    count = 0
    for i in word:
        if i not in text:
            text.append(i)
            count += 1
        elif i in text:
            text.remove(i)
            count -= 1
    return count


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
