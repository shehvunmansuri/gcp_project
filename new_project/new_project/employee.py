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
    #         "email": fake.email(),
    #         "employee_id": str(random.randint(1000000000, 9999999999)),
    #         "position": random.choice(["Manager", "Analyst", "Developer", "Designer"]),
    #         "phone_number": str(random.randint(1000000000, 9999999999)),
    #         "address": fake.address(),
    #         "hire_date": fake.date_between(start_date='-10y', end_date='today').isoformat(),
    #     })

    # with open("Employee.json", "w") as f:
    #     json.dump(data, f, indent=4)

    # print("Employee.json generated")

    branch = list(Branch.objects.all())
    with open("Employee.json", "r") as f:
        data = json.load(f)

        common_branch = random.choice(branch)
        for item in data:
            Employee.objects.create(
                name = item["name"],
                email = item["email"],
                employee_id = item["employee_id"],
                position = item["position"],
                branch = common_branch,
                phone_number = item["phone_number"],
                address = item["address"],
                hire_date =  item["hire_date"],
            )
    print("Data inserted successfully!")
    
if __name__ == "__main__":
    __main__()