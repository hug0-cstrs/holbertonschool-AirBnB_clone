#!/usr/bin/python3
"""init package"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
