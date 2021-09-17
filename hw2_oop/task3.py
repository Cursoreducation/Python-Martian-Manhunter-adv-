"""
3. class Profile:
Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
Override a printable string representation of Profile class and return: list of the params mentioned above
"""


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.params = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]

    def __str__(self):
        return 'Params={0}'.format(self.params)


person_profile = Profile('Peter', 'White', '0983175405', 'Koop. 9/1', 'ex@gmail.com', '21.01.1999', 23, 'male')
print(person_profile)