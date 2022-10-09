import time
import webbrowser

'''input'''

def load_rickroll():
    n = input('введите имя файла:')
    print('load...')
    time.sleep(1)
    print('.../')
    time.sleep(1)
    print('Succsefully!!!')
    '''output'''
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    webbrowser.open_new_tab(url)

load_rickroll()    