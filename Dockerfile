FROM python:3.11 as base
LABEL maintainer="freedom1294"

RUN apt update -qy && apt install -qy libcairo2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /python_basic_diploma/
WORKDIR /python_basic_diploma
RUN pip install -r requirements.txt

# Копируем исходный код в контейнер
COPY . /python_basic_diploma

# Запускаем приложение
CMD ["python", "main.py"]