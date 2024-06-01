# RRWViolationDetection
## Описание
Это API на Flask, для работы веб-приложения по автоматическому обнаружению нарушений правил безопасности на записях с нагрудных камер работников РЖД.
## Установка и запуск
### Linux
1. Клонирование репозитория:

```bash
git clone https://github.com/muz-muzzy/RRWViolationDetection.git
```
2. Переход в каталог проекта:
```bash
cd RRWViolationDetection
```
3.  Создание виртуального окружения:
```bash
python3 -m venv venv
```
4. Вход в виртуальное окружение:
```bash
source ./venv/bin/activate
```
5. Установка зависимостей:
```bash
pip install -r requirements.txt
```
6. Скачивание весов модели:
```bash
python3 ./models/DuckingModel/download.py
```
7. Запуск
```bash
python3 app.py
```
### Windows
1. Клонирование репозитория:

```bash
git clone https://github.com/muz-muzzy/RRWViolationDetection.git
```
2. Переход в каталог проекта:
```bash
cd RRWViolationDetection
```
3.  Создание виртуального окружения:
```bash
python -m venv venv
```
4. Вход в виртуальное окружение:
```bash
.\venv\Scripts\activate
```
5. Установка зависимостей:
```bash
pip install -r windows_requirements.txt
```
6. Скачивание весов модели:
```bash
python ./models/DuckingModel/download.py
```
7. Запуск
```bash
python app.py
```

## Роуты
### /getvideos
Метод - GET
Результат - JSON файл вида:
```json
{
    "files": [
        "video1.mp4",
        "video2.mp4", 
        ....
    ]
}
```

### /getvideo/%filename%
Метод - GET
Результат - .mp4 файл (видео)
Отдаёт видео по его названию (передаётся в url, например - "http://127.0.0.1:3000/getvideo/video.mp4").

### /getviolation/%filename%
Метод - GET
Результат - JSON файл с таймкодами нарушений всех видов найденных в видео.
```json
{
    "vest": [6, 12, ...],
    "ducking": [33, 41, ...]
}
```
Отдаёт по его названию (передаётся в url, например - "http://127.0.0.1:3000/getviolation/video.mp4").

### /upload
Метод - POST
Принимает form-data с .mp4 файлом, загружает его на сервер, анализируя его, и сохраняя данные о нём в БД.
Возвращает JSON с сообщением об успехе или неудаче.
