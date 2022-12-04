from __future__ import unicode_literals
from tokenize import endpats
import youtube_dl

def my_hook(d):
    # if d['status'] == 'finished':
    print('\n\n' + d['status'] + '\n\n')

ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist':False,
    # 'extract_flat': True,
    # 'dump_single_json': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
    'outtmpl': '[%(uploader)s] %(title)s.%(ext)s',
    # 'progress_hooks' : [my_hook],
}

fileWithURLs = input("Name(path) of file with URLs> ")
fileWithURLs = open(fileWithURLs)
try:
    linksArray = fileWithURLs.read().split("\n")
except:
    print(1)

try:
    for link in linksArray:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            endPath = ydl.download([link])
        
except:
    print(2)



#TODO:пробелы между скачиваниями

#TODO:время скачивания

#TODO:настоящее время (время начала\конца скачивания)

#TODO:Если имя исполнителя и канала одинаковое то пусть будет только имя канала

#!Ошибки: Создать обработчик: Приватный плейлист \ нет видео \ не правильный URL \ в плейлисте нет видео.

#TODO:Вывод ошибки в консоль

#?Есть ли возможность создать отдельный плейлист и удалять оттуда скачанные видео

#TODO:txt файл со всеми названиями скачанных песен
# создать цикл для сканирования папки старых песен 

#TODO:Есть ли скачанные в плейлисте

#TODO: throttled rate RATE - посмотреть опцию для котроля скорости скачивания


input("[Finished]")

