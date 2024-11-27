# Над лабораторной работой работали:
Студенты группы к.205с9-4
```
Коновод Кирилл
```
```
Лихачев Михаил
```
# install pip requirements:
```
pip install fastapi uvicorn jinja2 joblib
```
or
```
pip3 install fastapi uvicorn jinja2 joblib
```
or 
```
pip3 install -r requirements.txt
```
# Структура:
```
laba6-main/
├── app.py               # Основной файл приложения FastAPI
├── train_model.py       # Скрипт для обучения и сохранения модели
├── iris_model.joblib    # Файл с сохранённой моделью (генерируется train_model.py)
├── templates/           # Папка для HTML-шаблонов
│   └── index.html       # Главная веб-страница с формой ввода
├── static/              # (опционально) Папка для стилей CSS или изображений
├── requirements.txt     # Файл с зависимостями проекта (для установки pip)
└── run.py               # Скрипт для запуска сервера (альтернатива uvicorn)

```
