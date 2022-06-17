def get_input_parameters():

    cell = []

    count_cell = int(input('Введите кол-во клеток: '))

    for cel in range(count_cell):
        print('Введите эффективность', cel + 1, 'клетки:', end= ' ')
        num = int(input())
        cell.append(num)
    return cell




def display_result(cells):


    print('Неподходящие значения:', result_cells)



def select_cells(cells):

    cell_below = []

    for i in range(len(cells)):
        if i > cells[i] :
            cell_below.append(cells[i])
    return cell_below


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
