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
        value = madlib['value']
        for blank in blanks:
            word = input(f'{blank}: ')
            index = blanks.index(blank)
            value[index] += word
        print(' '.join(value))
        play = input('Press y for "Yes" or n for "No"')
        if play == 'y':
            is_playing = True
        else:
            is_playing = False


play_game()
