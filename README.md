# Frontend
## Описание
Наше решение представляет собой SPA-приложение для работы с обученными на обнаружение различных нарушений безопасности моделями компьютерного зрения и машинного обучения. Пользователь может предоставить модели на вход видео в формате .mp4 и получить проанализированную и обработанную его копию. Также пользователь может ознакомиться с результатом работы моделей через видео плеер на странице, внизу которой даны выбранные моделью временные метки с нарушениями. Помимо этого, программный модуль предоставляет возможность для удобного и наглядного анализа информации с помощью графиков.

## Установка
1. Переход в директорию
```bash
cd frontend
```
2. Установка зависимостей
```bash
npm install
```
3. Запуск
```bash
npm run dev
```

# Backend
## Описание
Это API на Flask, использующий модели компьютерного зрения для автоматического обнаружениюя нарушений правил безопасности на записях с нагрудных камер работников РЖД.
--------------------------------------------------------------------------------------
*ВНИМАНИЕ!* ПРИ ЗАГРУЗКЕ ВИДЕО НА (локальный) СЕРВЕР НУЖНО ПОДОЖДАТЬ НЕКОТОРОЕ ВРЕМЯ, ПОКА МОДЕЛИ ЕГО АНАЛИЗИРУЮТ. Работоспособность можно отследить по запросам.
--------------------------------------------------------------------------------------

## Установка и запуск
### Linux
1. Клонирование репозитория:

```bash
git clone https://github.com/muz-muzzy/RRWViolationDetection.git
```
2. Переход в директорию проекта:
```bash
cd RRWViolationDetection/backend
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
cd RRWViolationDetection/backend
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