import json
import os
import django
import random       
from django.db import models 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_project.settings")
django.setup()

import json
from faker import Faker
from bank.models import Customer, Branch, Loan, Employee, Account, Transaction

def __main__():

    fake = Faker()
    data = []

    # for i in range(100):
    #     data.append({
    #         "transaction_type": random.choice(['deposit', 'withdrawal', 'transfer']),
    #         "amount": round(random.uniform(100, 10000), 2),
    #         "transaction_date": fake.date_between(start_date='-1y', end_date='today').isoformat(),
    #         "description": fake.sentence(nb_words=6)
    #     })

    # with open("Transaction.json", "w") as f:
    #     json.dump(data, f, indent=4)

    # print("Transaction.json generated")

    account = list(Account.objects.all())
    with open("Transaction.json", "r") as f:
        
        data = json.load(f)
        common_account = random.choice(account)
        for item in data:
           Transaction.objects.create(
            account=common_account,
            transaction_type=item["transaction_type"],
            amount=item["amount"],
            transaction_date=item["transaction_date"],
            description=item["description"]
            )
             
    print("Data inserted successfully!")
    
if __name__ == "__main__":
    __main__()