from python:3.10.7-slim

COPY . /usr/src/cabbage
RUN python -m venv /opt/env
RUN /opt/env/bin/pip install -r /usr/src/cabbage/requirements.txt

EXPOSE 5000
CMD ["bash", "/usr/src/cabbage/run.sh"]