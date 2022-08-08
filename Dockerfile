FROM python:3

#set envionment variables
ENV PYTHONUNBUFFERED 1

# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip

# switch working directory
WORKDIR /build

# copy the requirements file into the image
COPY requirements.txt .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .
EXPOSE 3000
ENV FLASK_APP=manage.py
ENV DB_NAME=anakin
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV DB_HOST=mysql:3306
ENV APP_ENV=prod

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["manage.py", "run" ]
