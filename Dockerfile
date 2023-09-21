FROM python:3.11-slim-bullseye

RUN pip install --upgrade pip

RUN pip install poetry==1.5.1

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /code/service/
WORKDIR /code/service

# Installing requirements
RUN poetry install --without dev

# Copying actuall application
COPY . /code/service/
RUN mkdir /settings && mv /code/service/_service /settings/_service
RUN poetry install --without dev

ENV SETTINGS_MODULE=ci

EXPOSE 9090

CMD ["/usr/local/bin/python", "__main__.py"]
