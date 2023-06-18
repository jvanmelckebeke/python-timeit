FROM python:3.8.0

# install poetry
RUN pip install poetry

# set working directory
WORKDIR /app

# install dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# copy project
COPY . /app/

ENTRYPOINT ["python3", "main.py"]
