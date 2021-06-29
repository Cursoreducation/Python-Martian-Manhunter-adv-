import re
import os

if os.path.exists('Secret.log'):
    os.remove('Secret.log')
with open('django-success.log', 'r') as logfile:
    while True:
        line = logfile.readline()
        if not line:
            break
        line = re.sub(r'\[\d*\/\w*\/\d*\s(\d{2}:?){3}\]', '[XX/XXX/XXXX XX:XX:XX]', line)

        line = re.sub(r'\/admin\/', '/****/', line)

        with open('Secret.log', 'a') as file:
            file.write(line)
