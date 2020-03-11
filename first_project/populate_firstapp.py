import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django 
django.setup()

# Faker population script 
import random
from firstapp.models import AccessRecord, Webpage, Topic
from faker import Faker

 
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'New', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t 

def populate(N=5):

    for entry in range(N):

        # get the topic for entry    
        top = add_topic()

        # create the topic for the entry 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry 
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake accessrecord 
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print('Populating complete!') 
