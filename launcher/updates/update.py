import requests
import os
import shutil
from rich.console import Console
from time import sleep
from rich.progress import track
import zipfile


console = Console(highlight=False)

LOGO = """
╔════╗╔═══╗╔══╗╔══╗╔╗╔╗───╔╗──╔══╗╔╗╔╗╔╗─╔╗╔══╗╔╗╔╗╔═══╗╔═══╗
╚═╗╔═╝║╔═╗║║╔╗║║╔═╝║║║║───║║──║╔╗║║║║║║╚═╝║║╔═╝║║║║║╔══╝║╔═╗║
──║║──║╚═╝║║╚╝║║╚═╗║╚╝║───║║──║╚╝║║║║║║╔╗─║║║──║╚╝║║╚══╗║╚═╝║
──║║──║╔╗╔╝║╔╗║╚═╗║║╔╗║───║║──║╔╗║║║║║║║╚╗║║║──║╔╗║║╔══╝║╔╗╔╝
──║║──║║║║─║║║║╔═╝║║║║║───║╚═╗║║║║║╚╝║║║─║║║╚═╗║║║║║╚══╗║║║║─
──╚╝──╚╝╚╝─╚╝╚╝╚══╝╚╝╚╝───╚══╝╚╝╚╝╚══╝╚╝─╚╝╚══╝╚╝╚╝╚═══╝╚╝╚╝─
"""


def process_data():
    sleep(0.02)


def progress(text):
    for _ in track(range(100), description=f'[green]{text}'): 
        process_data()

def download(url, filename, path=None):
    if path == None:
        response = requests.get(url)
        open(filename, "wb").write(response.content)
    else:
        if os.path.exists(path):
            if os.path.exists(f"{path}\{filename}"):
                os.remove(f"{path}\{filename}")
            response = requests.get(url)
            open(filename, "wb").write(response.content)
            shutil.move(filename, path)


console.print(LOGO, justify="center")
console.print("Установщик обновлений", justify="center")
folder = '..'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            if file_path != "..\Temp":
                shutil.rmtree(file_path)
    except Exception as e:
        print('Не удалось удалить файл %s. Причина: %s' % (file_path, e))
progress("Загрузка архива лаунчера...")
download("https://raw.githubusercontent.com/MaksimKoreshkin/TrashLauncher/main/TrashLauncher.zip", "TrashLauncher.zip", "..")
progress("Распаковка архива...")
with zipfile.ZipFile("..\TrashLauncher.zip") as zip:
    zip.extractall("..")
os.remove("update.py")
