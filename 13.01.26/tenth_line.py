with open('file.txt', 'r') as file:
    lines = file.readlines()
    if len(lines) >= 10:
        print(lines[9])  # Index 9 corresponds to the tenth line (0-based index)
