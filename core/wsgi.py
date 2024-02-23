"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DOTENV_FILE_PATH = BASE_DIR / ".env"

dotenv.read_dotenv(str(DOTENV_FILE_PATH))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
