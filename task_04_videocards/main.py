def get_input_parameters():

    old_video_cards = []
    nVidia_count = int(input('Введите кол-во видеокарт: '))

    for card in range(nVidia_count):
        print(card + 1, 'Видеокарта:', end = ' ')
        num = int(input())
        old_video_cards.append(num)
    return old_video_cards



def display_result(old_video_cards, new_video_cards):

    print('Старый список видеокарт:', video_cards)
    print('Новый список видеокарт:', result_video_cards)



def select_video_cards(video_cards):

    new_list = max(video_cards)
    new_list2 = [i for i in video_cards if i != new_list]

    return  new_list2





if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
