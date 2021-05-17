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
        self.profile = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]

    def __str__(self):
        return f'User Profile: {self.profile}'


if __name__ == '__main__':
    john = Profile('John', 'Doe', '380931234567', 'Number 4 Privet Drive, Little Whinging, Surrey', 'john.doe@email.com', '04.04.2004', '17', 'male')
    print(john)
