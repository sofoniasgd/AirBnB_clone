#!/usr/bin/python3
"""initializef for engine package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
