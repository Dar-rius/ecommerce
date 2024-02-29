FROM python:3.11-alpine
WORKDIR /app
RUN pip install poetry==1.8.0
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR
COPY . .
EXPOSE 8000
ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
