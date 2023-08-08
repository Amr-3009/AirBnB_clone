#!/usr/bin/python3
"""
init for storage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

try:
    storage.reload()
except FileNotFoundError:
    pass
