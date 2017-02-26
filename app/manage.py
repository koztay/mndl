#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mandal.settings")
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce2.settings.new_theme")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
