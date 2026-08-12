import json
import os
import django
import random       
from django.db import models 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_project.settings")
django.setup()

import json
from faker import Faker
from bank.models import Customer, Branch, Loan, Employee, Account

def __main__(): 

    fake = Faker()
    data = []
    # for i in range(100):

    #     data.append({
    #         "name": fake.name(),
    #         "account_number": str(random.randint(1000000000, 9999999999)),
    #         "account_type": random.choice(['savings', 'current']),
    #         "balance": round(random.uniform(1000, 100000), 2)
    #     })

    # with open('customer.json', 'w') as f:
    #     json.dump(data, f, indent=4)

    # print("customer.json file created successfully with 100 random customer records.")

    with open('customer.json', 'r') as f:
        customer_data = json.load(f)

        for customer in customer_data:
            Customer.objects.create(
                name=customer['name'],
                account_number=customer['account_number'],
                account_type=customer['account_type'],
                balance=customer['balance']
            )
        print("Customer data inserted succcessfully")


if __name__ == "__main__":
    __main__()