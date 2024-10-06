from python:3.11-slim

COPY . /usr/src/cabbage
RUN python -m venv /opt/env
RUN /opt/env/bin/pip install -r /usr/src/cabbage/requirements.txt
RUN touch /usr/src/cabbage/apps/auth/accounts/__init__.py
RUN touch /usr/src/cabbage/apps/auth/babysitters/__init__.py
RUN touch /usr/src/cabbage/apps/nav/search/__init__.py

EXPOSE 5000
CMD ["bash", "/usr/src/cabbage/run.sh"]