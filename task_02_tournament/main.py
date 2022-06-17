def display_result(participants_names):

    print('Список имён участников:', participants_names)


def get_participants_names(names):

    name_list = list(names)
    new_list = []

    for name in range(len(name_list)):
        if name % 2 == 0:
            new_list.append(name_list[name])
    return new_list




if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
