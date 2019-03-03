#!/usr/bin/env python

import os
import sys

from django.core.management import execute_from_command_line


sys.path.append('src')
sys.path.append('tests/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.app.settings')

execute_from_command_line(sys.argv)
