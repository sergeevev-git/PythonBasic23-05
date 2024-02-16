FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip "poetry==1.7.1"

RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY ./homework_06/ ./