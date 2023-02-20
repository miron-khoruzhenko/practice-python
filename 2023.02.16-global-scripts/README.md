# Инфо

## Как создать глобальный скрипт Python?

После написания глобального скрипты питон нужно создать shell файл и там написать небольшой скрипт который будет вызывать написанную нами программу.

```sh
#!/bin/bash
python path/to/script/main.py
```

После этого нужно дать права скрипту

```bash
	sudo chmod +x /path/to/script/ourscript.sh
```

и в самом конце переместить этот файл в любое место которое есть в `$PATH`. Что бы увидеть эти места можно прописать. Я перемещаю в `/usr/local/bin`

```bash
echo $PATH
sudo mv /path/to/script/ourscript.sh /usr/local/bin
```

## Как работает GNP (Generate New Project)

Скрипт выводит все папки из `gnp-src`. После копирует и переименовывает выбранную папку в формате `YYYY.MM.dd-project-name` и переносит ее в `cwd` (current working directory). 