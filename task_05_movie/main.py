from cmath import e


def get_input_parameters():

    love_film = []
    film_count = int(input('Сколько фильмов хотите добавить: '))
    for _ in range(film_count):
        fil = input('Введите название фильма: ')
        love_film.append(fil)
    return love_film




def display_result(favorite_films, errors):

    print('Ваш список любимых фильмов:', favorite_films)




def add_favorite_film(new_favorite_films, available_films):

    film = []
    errors = []
    for i in new_favorite_films:
        if i in available_films:
            film.append(i)
        else:
            errors.append(i)
            print("Ошибка такого фильма нет на сайте!")

    return film, errors


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
