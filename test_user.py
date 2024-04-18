#!/usr/bin/python3
from models.user import User

my_model = User()
my_model.email = "zeph@gmm.com"
my_model.password = "psw@123"
my_model.first_name = "sofi"
my_model.last_name = "dub"
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
