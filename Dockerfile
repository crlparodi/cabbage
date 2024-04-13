from python:3.10.7-slim

RUN apt-get update
RUN apt-get install -y python3-dotenv nginx
COPY . /usr/src/cabbage
RUN python -m venv /opt/env
RUN /opt/env/bin/pip install -r /usr/src/cabbage/requirements.txt
# RUN mkdir /usr/certs
RUN mkdir /var/log/cabbage
COPY ./config/cabbage.conf /etc/nginx/sites-available/cabbage
# COPY nginx-selfsigned.crt /usr/certs/nginx-selfsigned.crt
# COPY nginx-selfsigned.key /usr/certs/nginx-selfsigned.key
# RUN chown -R root:root /usr/certs
# RUN chmod -R 600 /usr/certs
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/cabbage /etc/nginx/sites-enabled/cabbage

EXPOSE 80
CMD ["bash", "/usr/src/cabbage/run.sh"]