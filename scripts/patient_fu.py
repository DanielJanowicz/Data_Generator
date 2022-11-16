import pandas as pd
from dotenv import load_dotenv
import os
from faker import Faker
from faker.providers import DynamicProvider
import uuid
import random

load_dotenv()
fake = Faker()


follow_up = [
{
    'MRN': str('E' + str(random.randint(11111, 99999))), 
    'SSN': fake.ssn(),
    'Last_Name': fake.last_name(),
    'First_Name': fake.first_name(),
    'DOB': fake.date_of_birth(),
    'Last_Contact': fake.date_between(start_date='-1y', end_date='today'),
    'Hospital_Code': str('0' + str(random.randint(1, 5))),
    #'Contact_Method': fake.element(elements=('Phone', 'Letter', 'Physician', 'Email'))
} for x in range(250)]

df_fu = pd.DataFrame(follow_up)

df_fu.drop_duplicates(subset=['MRN'], inplace=True)
df_fu.to_csv('datasets/follow_up.csv', index=False)
