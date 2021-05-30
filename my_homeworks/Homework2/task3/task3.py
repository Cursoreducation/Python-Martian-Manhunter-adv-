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
        self.parameters = [self.name, self.last_name, self.phone_number,
                           self.address, self.email, self.birthday, self.age, self.sex]

# 1st variant: to return only list, like was assigned in Task
    def __str__(self):
        return str(self.parameters)

# 2nd variant: returns formatted string
    # def __str__(self):
    #     return (f'Name: {self.name}; Last name: {self.last_name}; ph number: {self.phone_number};' +
    #             f'Address: {self.address}; Email: {self.email}, Birthday: {self.birthday};' +
    #             f'Age: {self.age}; Sex: {self.sex}')


if __name__ == '__main__':
    my_profile = Profile(name='Dmytrii', last_name='Basov', phone_number='09312345687', address='Kyiv',
                        email='dimon4a2009@gmail.com', birthday="15.04.1997", age='24', sex='male')

    print(my_profile)
