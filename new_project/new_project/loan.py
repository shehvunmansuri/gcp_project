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


    for i in range(100):

    #     data.append({
    #         # "customer": customer.id,
    #         # "branch": branch.id,
    #        "loan_type": random.choice(["Home Loan", "Car Loan", "Personal Loan", "Education Loan"]),
    #        "amount": round(random.uniform(1000.00, 5000000.00), 2),
    #        "interest_rate": round(random.uniform(5.0, 15.0), 2),
    #         "start_date": fake.date_between(start_date='-2y', end_date='today').isoformat(),
    #         "end_date": fake.date_between(start_date='today', end_date='+5y').isoformat(),
    #         })


    # with open("Loan.json", "w") as f:
    #     json.dump(data, f, indent=4)

    # print("Loan.json generated")

        customer = list(Customer.objects.all())
    with open("Loan.json", "r") as f:
        data = json.load(f)

    for item in data:

        common_customer = random.choice(customer)
        Loan.objects.create(
            customer = common_customer,
            loan_type = item["loan_type"],
            amount = item["amount"],
            interest_rate = item["interest_rate"],
            start_date =  item["start_date"],
            end_date = item["end_date"],
        )
    print("✅ Data inserted successfully!")

if __name__ == "__main__":
    __main__()