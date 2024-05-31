FROM python:3.9

ENV PATH="/scripts:${PATH}"
COPY requeriments.txt /requeriments.txt
RUN pip install -r /requeriments.txt

RUN mkdir /code
COPY . /code
WORKDIR /code
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN useradd desarrollador
RUN chown -R desarrollador /code

USER desarrollador

CMD ["entrypoint.sh"]