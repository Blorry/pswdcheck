# Password Strength API

Небольшой FastAPI-сервис для оценки стойкости пароля. Считает энтропию пароля
в битах исходя из длины и набора используемых символов, классифицирует
результат и умеет генерировать случайные пароли.

## Запуск

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Документация: http://127.0.0.1:8000/docs

## Эндпоинты

- `GET /health` — проверка живости.
- `POST /check` — тело `{"password": "..."}`, возвращает длину, размер алфавита,
  энтропию в битах и категорию стойкости.
- `GET /generate?length=16` — сгенерировать случайный пароль и сразу оценить его.

## Тесты

```bash
pip install ruff pytest
ruff check .
pytest -q
```

## CI

При каждом push и pull request в `main` GitHub Actions запускает линтер и тесты
(см. `.github/workflows/ci.yml`).
