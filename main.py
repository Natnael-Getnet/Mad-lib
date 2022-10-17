import requests


def get_random_mad_lib():
    response = requests.get('http://madlibz.herokuapp.com/api/random')
    return response.json()


def play_game():
    is_playing = True
    while is_playing:
        print('Welcome Madlib Game.')
        madlib = get_random_mad_lib()
        blanks = madlib['blanks']
        values = madlib['value']
        word_list = []
        for blank in blanks:
            word = input(f'{blank}: ')
            word_list.append(word)
        for num in range(len(values) - 2):
            values[num] = values[num] + word_list[num]
        matlib = []
        for value in values:
            matlib.append(value)
        matlib.remove(0)
        print(''.join(matlib))
        play = input('Press y for "Yes" or n for "No"')
        if play == 'y':
            is_playing = True
        else:
            is_playing = False


play_game()
