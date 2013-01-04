#!/usr/bin/env python
import logging
from os import environ
import sys


logger = logging.getLogger(__name__)


if __name__ == "__main__":
  if 'test' in sys.argv:
    environ.setdefault("DJANGO_SETTINGS_MODULE", "redroverme.settings.test")
  else:
    environ.setdefault("DJANGO_SETTINGS_MODULE", "redroverme.settings")

  from django.core.management import execute_from_command_line

  execute_from_command_line(sys.argv)
