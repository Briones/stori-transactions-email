FROM nickgryg/alpine-pandas:3.10.4

WORKDIR /code
RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk add mariadb
RUN apk add gcc musl-dev mariadb-connector-c-dev
RUN python -m pip install --upgrade pip
RUN pip install python-dotenv
RUN pip install mariadb

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 7007
COPY . .
CMD [ "python", "app.py" ]