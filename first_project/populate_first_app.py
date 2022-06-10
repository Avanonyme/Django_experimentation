import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_experimentation.settings")

import django
django.setup()

#FAKE POP SCRIPT

import random
from first_app.models import *
from faker import Faker

fakegen=Faker()

topics=['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        #get topic for entry
        top=add_topic()

        #create the fake data for that entry
        url=fakegen.url()
        name=fakegen.company()
        date=fakegen.date()

        #create the new Webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=url,name=name)[0]

        #create fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=date)[0]


if __name__ == '__main__':
    print("populatin script")
    populate(20)
    print("population complete")