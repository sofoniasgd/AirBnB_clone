#!/usr/bin/python3
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

fs = FileStorage()
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass
try:
    os.remove(file_path)
except:
    pass
try:
    fs._FileStorage__objects.clear()
except:
    pass
ids = []

# First create
for i in range(1):
    print("bm1 = BaseModel()")
    bm = BaseModel()
    bm.updated_at = datetime.utcnow()
    print("fs.new(bm1)")
    fs.new(bm)
    ids.append(bm.id)

try:
    os.remove(file_path)
except:
    pass
print("fs.save()")
for key, value in fs._FileStorage__objects.items():
    print("obj_id=|{}|\nobj=|{}|".format(key, value))
fs.save()
try:
    fs._FileStorage__objects.clear()
except:
    pass
print("fs.reload()")
fs.reload()
for key, value in fs._FileStorage__objects.items():
    print("obj_id=|{}|\nobj=|{}|".format(key, value))

all_reloaded = fs.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload 1")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 1 {}".format(id))

from models import storage
storage.reload()
print("storage.reload()")

# Second creatie
for i in range(2):
    print("bm{} = BaseModel()".format(i))
    bm = BaseModel()
    print("bm{}.save()".format(i))
    bm.save()
    for key, value in storage._FileStorage__objects.items():
        print("obj_id=|{}|\nobj=|{}|".format(key, value))
    ids.append(bm.id)
try:
    os.remove(file_path)
except:
    pass
print("storage.save()")
storage.save()
for key, value in storage._FileStorage__objects.items():
    print("obj_id=|{}|\nobj=|{}|".format(key, value))
try:
    fs._FileStorage__objects.clear()
except:
    pass
print("storage.reload()")
storage.reload()
for key, value in storage._FileStorage__objects.items():
    print("obj_id=|{}|\nobj=|{}|".format(key, value))

all_reloaded = storage.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload 2")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 2 {}".format(id))

try:
    os.remove(file_path)
except Exception as e:
    pass
