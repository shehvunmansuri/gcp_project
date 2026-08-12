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
    #         "account_type": random.choice(['savings', 'current']),
    #         "balance": round(random.uniform(1000, 100000), 2)
    #     })

    # with open("Account.json", "w") as f:
    #     json.dump(data, f, indent=4)

    print("Account.json generated")

    customer = list(Customer.objects.all())
    branch = list(Branch.objects.all())
    with open("Account.json", "r") as f:
        
        data = json.load(f)
        common_customer = random.choice(customer)
        common_branch = random.choice(branch)
        for item in data:
            Account.objects.create(
                customer = common_customer,
                branch = common_branch,
                account_type = item["acccount_type"],
                balance = item["balance"],

            )
    print("Data inserted successfully!")
    
if __name__ == "__main__":
    __main__()