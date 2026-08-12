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
    #         "branch_name":fake.company(),
    #         "branch_code":str(random.randint(1000000000, 9999999999)),
    #         "address":fake.address(),
    #         "phone_number":str(random.randint(1000000000, 9999999999))
    #     })

    # with open('branch.json', 'w') as f:
    #     json.dump(data, f, indent=4)

    # print("branch.json file created successfully with 100 random branch records.")

    with open('branch.json', 'r') as f:
        branch_data = json.load(f)

        for branch in branch_data:
            Branch.objects.create(
                branch_name=branch['branch_name'],
                branch_code=branch['branch_code'],
                address=branch['address'],
                phone_number=branch['phone_number']
            )
        print("Branch data inserted succcessfully")


if __name__ == "__main__":
    __main__()