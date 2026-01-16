# Read from the file file.txt and output all valid phone numbers to stdout.
python3 -c "
import re
with open('file.txt', 'r') as file:
    for line in file:
        if re.match(r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})
```, line.strip()):
            print(line.strip())
"
