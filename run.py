import asyncio
from fastapi import FastAPI
from fastapi.routing import APIRoute
from hypercorn.config import Config
from hypercorn.asyncio import serve

# Импорт вашего приложения
from app import app

async def main():
    config = Config()
    config.bind = ["127.0.0.1:8000"]  # Адрес и порт
    await serve(app, config)

if __name__ == "__main__":
    asyncio.run(main())
