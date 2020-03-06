FROM python:3.6-alpine

COPY backend/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./backend /backend

ENTRYPOINT [ "python" ]

CMD [ "./backend/app.py" ]