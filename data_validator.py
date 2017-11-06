import re
import math
from datetime import *

class DataValidator():
    def __init__(self):
        self.data = None
        self.valid = True

    def im_valid(self):
        return self.valid

    def is_person_valid(self, person):
        valid = False
        if self.im_valid():
            if re.match(r'[a-z][0-9]{3}', (person).lower()):
                if len(str(person[0])) >= 5:
                    valid = True
        return valid

    def is_sex_valid(self, sex):
        valid = False
        if self.im_valid():
            if sex[1].upper() == "M" or (sex[1]).upper() == "F":
                valid = True
        return valid

    def is_date_valid(self, date):
        valid = False
        if self.im_valid():
            try:
                datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                valid = False
        return valid

    def is_birthday_valid(self, birthday, age):
        valid = False
        if self.im_valid():
            the_date = datetime.strptime(birthday, "%d-%m-%Y")
            test_age = math.floor(((datetime.today() - the_date).days / 365))
            if test_age == int(age):
                valid = True
        return valid

    def is_sales_valid(self, sales):
        valid = False
        if self.im_valid():
            if re.match(r'[0-9]{3}', sales):
                valid = True
        return valid

    def is_bmi_valid(self, bmi):
        valid = False
        if self.im_valid():
            if re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b', (bmi).upper()):
                valid = True
        return valid

    def is_income_valid(self, income):
        valid = True
        if self.im_valid():
            try:
                if int(income):
                    if len(str(int(income))) > 3:
                        valid = True
            except ValueError:
                valid = False
        return valid

    def validate(self):
        add_to = []
        for person in self.data:
            self.valid = self.is_person_valid(person[0])
            self.valid = self.is_sex_valid(person[1])
            self.valid = self.is_date_valid(person[6])
            self.valid = self.is_birthday_valid(person[6], person[2])
            self.valid = self.is_sales_valid(person[3])
            self.valid = self.is_bmi_valid(person[4])
            self.valid = self.is_income_valid(person[5])
            if self.valid:
                add_to.append(person)
        return add_to

    def start(self, data):
        self.data = data
        self.valid = True
        contents = self.validate()
        return contents