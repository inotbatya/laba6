from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

# Инициализация FastAPI
app = FastAPI()

# Загрузка шаблонов
templates = Jinja2Templates(directory="templates")

# Загрузка модели
model = joblib.load("iris_model.joblib")
iris_classes = ["Setosa", "Versicolor", "Virginica"]

# Главная страница с формой
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Обработка данных из формы
@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    # Формируем входной массив для модели
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)[0]
    flower_name = iris_classes[prediction]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": flower_name}
    )
