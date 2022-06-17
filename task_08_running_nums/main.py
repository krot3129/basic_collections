def get_input_parameters():

    task_list = []
    list_input = int(input('Введите кол-во элементов в списке: '))
    for _ in range(list_input):
        number = int(input('Введите элементы списка: '))
        task_list.append(number)
    shift = int(input('Введите сдвиг: '))
    return shift, task_list



def display_result(shifted_list):

    print('Сдвинутый список:', shifted_list)



def shift_list(shift, original_list):


    original_list = original_list[ - shift:] + original_list[:-shift]
    return original_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    shift, original_list = get_input_parameters()  # получаем параметры
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
