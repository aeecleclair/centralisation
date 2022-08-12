FROM python:3.9

ENV POETRY_VERSION=1.1.14
RUN python3 -m pip install poetry==$POETRY_VERSION

WORKDIR /centralisation

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-dev

COPY . .

RUN poetry run python ./build.py