FROM python:3.7.4


# COPY requirements.txt requirements.txt
# COPY requirements.txt requirements.txt
# COPY application.py application.py
COPY . .
# ADD config.py /etc/nginx/
# ADD static /usr/share/nginx/html/
# ADD static /var/www/html/

EXPOSE 8080

RUN pip install -r requirements.txt

# COPY ./backend /backend

ENTRYPOINT [ "python3" ]

# CMD [ "./backend/application.py" ]
CMD [ "application.py" ] 