def get_input_parameters():
    num_list = []
    numbers = int(input('Введите кол-во элементов списка: '))
    for _ in range(numbers):
        num = int(input('Введите числа: '))
        num_list.append(num)
    return num_list


def display_result(sorted_list):

    print(sorted_list)


def sort_list(original_list):

    original_list.sort()
    return original_list



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
