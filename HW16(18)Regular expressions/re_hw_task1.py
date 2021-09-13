import re

if __name__ == "__main__":
    with open("django_success.log") as file:
        res = ''.join(file.readlines())
        res = re.sub(r'\/admin\/', '/x_x_x_x/', res)
        res = re.sub(r"\[\d+\/\w+\/\d*\s\d+:\d*:\d*]", "[XX/XXX/XXXX XX:XX:XX", res)
        with open("django_success_done.log", "a") as file_done:
            file_done.write(res)

