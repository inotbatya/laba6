# Импортируем библиотеки
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Загрузка данных
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Обучение модели
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Сохранение модели
joblib.dump(model, "iris_model.joblib")
print("Модель сохранена в файл 'iris_model.joblib'")
