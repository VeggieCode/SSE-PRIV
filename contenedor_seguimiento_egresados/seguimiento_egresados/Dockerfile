FROM python:3.9

RUN mkdir /dependencias
COPY requeriments.txt /dependencias
RUN pip install -r /dependencias/requeriments.txt

ENV EMAIL_PORT=""
ENV EMAIL_HOST=""
ENV EMAIL_HOST_USER=""
ENV EMAIL_HOST_PASSWORD=""
ENV DEFAULT_FROM_EMAIL=""
ENV SERVER_EMAIL=""
ENV SECRET_KEY=""
ENV DB_NAME=""
ENV DB_USER=""
ENV DB_PASSWORD=""
ENV DB_HOST=""
ENV DB_PORT=3306
ENV PATH_PREFIX=""

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN chmod +x run.sh

RUN useradd -s /bin/bash desarrollador

RUN chown -R desarrollador /code

USER desarrollador

CMD ./run.sh