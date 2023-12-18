from randomuser import RandomUser
import pandas as pd

r =RandomUser()
some_list =r.generate_users(10)
name =r.get_full_name()

for user in some_list:
    print (user.get_picture())