import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','New_Project.settings')

import django
django.setup()


#Fake Population Script
import random
from first_app.models import User_Info
from faker import Faker

fakegen = Faker()
# topics = ['Search','Social','News','Games','Marketplace','Technology']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):
        # top = add_topic()

        fake_name = fakegen.name()
        fake_address = fakegen.address()
        fake_email = fakegen.email()

        ui = User_Info.objects.get_or_create(name = fake_name, addres=fake_address, email=fake_email)[0]


if __name__ == "__main__":
    print("Start Get Population")
    populate(20)
    print("Complated .... ")