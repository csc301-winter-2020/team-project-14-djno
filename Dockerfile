FROM python:3.7

COPY /backend/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./backend /backend

CMD  ./backend/app.py