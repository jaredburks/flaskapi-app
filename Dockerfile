FROM python:3.6-slim
RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential
# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 8000

#RUN pip install gunicorn
# run the command
#CMD ["python", "./app.py"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--timeout", "600"]

