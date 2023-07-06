#!/usr/bin/python3
"""init package"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
