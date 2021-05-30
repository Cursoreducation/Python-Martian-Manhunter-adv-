"""
3.
class Profile:
    ""
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    ""
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
        self.information = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday,
                            self.age, self.sex]

    def __repr__(self):
        return f"It is my profile: {self.information}"


profile = Profile("Maksym", "Sharko", "+380687056509", "Lviv, Komarova street", "maks.sharko02@gmail.com", "23.04.2002",
                  "19", "man")
print(profile)

