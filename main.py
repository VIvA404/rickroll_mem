import time
import webbrowser
import tqdm


n = input("Введите имя файла: ")
print("load...")
time.sleep(1)

for i in tqdm.tqdm(range(100)):
    time.sleep(0.01)

webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
