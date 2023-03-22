import pandas as pd

path = '_chat.txt'
# Read the text file
with open(path, encoding='utf-8') as f:
    lines = f.readlines()

# lists to store the data
date = []
hour = []
author = []
message = []

line_counter = 1
for i, line in enumerate(lines):
    try:
        # Extract date
        date_part = line.split('[')[1].split(',')[0].strip()
        if len(date_part) > 0:
            date.append(date_part)

        # Extract hour
        hour_part = line.split(',')[1].split(']')[0].strip()
        if len(hour_part) > 0:
            hour.append(hour_part)

        # Extract author
        author_part = line.split(']')[1].split(':')[0].strip()
        if len(author_part) > 0:
            author.append(author_part)

        # Extract message
        message_part = line[20:].split(':')[1].strip()
        if len(message_part) > 0:
            message.append(message_part)
            
        line_counter = line_counter + 1
        print(date[i], hour[i], author[i], message[i])

    except IndexError:
        print("error")
        continue

df = pd.DataFrame({'Date': date, 'Hour': hour, 'Author': author, 'Message': message})
print(df)