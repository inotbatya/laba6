from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sklearn.externals import joblib  # Для загрузки модели
from sklearn.datasets import load_iris
import numpy as np

# Создание приложения FastAPI
app = FastAPI()

# Подключение HTML-шаблонов и статики
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Загрузка модели
model = joblib.load("iris_model.joblib")
iris = load_iris()

# Главная страница с формой
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

# Обработка предсказания
@app.post("/predict")
async def predict(
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    try:
        # Формирование данных для модели
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)[0]
        flower_name = iris.target_names[prediction]
        return {"flower": flower_name}
    except ValueError:
        raise HTTPException(status_code=400, detail="Некорректные данные. Проверьте ввод.")
