FROM python:3.11.4-alpine3.18

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

ENV APPDIR /app

WORKDIR ${APPDIR}

COPY customers_service/Pipfile .
COPY customers_service/Pipfile.lock .

RUN pip install --upgrade pip

RUN pip install pipenv
RUN pipenv install --dev --system --deploy

COPY customers_service/ .

ENTRYPOINT [ "pipenv", "run", "flask", "run", "--host=0.0.0.0", "--debug" ]
