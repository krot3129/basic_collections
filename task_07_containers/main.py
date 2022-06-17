def get_input_parameters():
    container_list = []
    container_count = int(input('Введите кол-во контенеров: '))
    for _ in range(container_count):
        container = int(input('Введите веса контенера: '))
        if container < 200:
            container_list.append(container)
        else:
            print('Вес слишком большой')
    new_container = int(input('Введите вес нового контенера: '))

    return container_list, new_container





def display_result(serial_number_new_container):

    print('Порядковый номер нового контенера', serial_number_new_container)



def search_serial_number_new_container(list_container_weights, new_container_weight):


    row = 0
    for  c in range(len(list_container_weights)):
        row = c + 1
        if list_container_weights[c] < new_container_weight:
            break
    print('Номер куда вставить контенер', row)
    return row



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    list_container_weights, new_container_weight = get_input_parameters()  # получаем параметры
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
