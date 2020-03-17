import numpy as np


def game_core_v3(number):
    '''Используем алгоритм бинарного поиска для угадывания числа'''
    count = 0
    lower = 0
    upper = 101
    predict = (lower + upper)//2
    while number != predict:
        count+=1
        if number > predict: 
            lower = (upper - lower)//2 + lower
            predict = (lower + upper)//2           
        elif number < predict: 
            upper = (upper - lower)//2 + lower
            predict = (lower + upper)//2                      
    return(count) # выход из цикла, если угадали


def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# Проверяем
score_game(game_core_v3)
