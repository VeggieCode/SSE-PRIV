FROM python:3.9

RUN mkdir /dependencias
COPY requeriments.txt /dependencias
RUN pip install -r /dependencias/requeriments.txt

ENV EMAIL_PORT=587
ENV EMAIL_HOST=smtp-mail.outlook.com
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


RUN mkdir /code
COPY . /code
WORKDIR /code

RUN useradd -s /bin/bash desarrollador

RUN chown -R desarrollador /code

USER desarrollador

CMD ["/bin/bash","/code/run.sh"]