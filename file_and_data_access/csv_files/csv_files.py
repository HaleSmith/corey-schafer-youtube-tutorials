# References https://www.youtube.com/watch?v=q5uM4VKywbA
# If data contains a delimiter in a field, encloses " "
# Example: john-doe -> field0-"john-doe"-field2
# Can pass delimiter as a read argument
# May need line terminator argument

import csv

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")

new_section(f"Opening file using context manager and csv.reader")
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # An object in memory
    print(f"Printout csv_reader: {csv_reader}")
    print("Reading each line:")
    for line in csv_reader:
        print(line)

new_section(f"Reading individual components from a line, without headers")
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # An object in memory
    next(csv_reader)  # Skips over the header
    for line in csv_reader:
        print(line[2])

new_section(f"Writing to a new file and changing delimiter to '-'")
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # An object in memory
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-', lineterminator='\n')
        for line in csv_reader:
            csv_writer.writerow(line)
print("See new_names.csv")

new_section(f"Writing to a new file and changing delimiter to a tab")
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # An object in memory
    with open('new_names2.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t', lineterminator='\n')
        for line in csv_reader:
            csv_writer.writerow(line)
print("See new_names2.csv")

new_section(f"Reading a new file with wrong delimiter")
with open('new_names2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # An object in memory
    print("Read in with wrong delimiter")
    for line in csv_reader:
        print(line)

new_section(f"Reading a new file with correct delimiter specified")
with open('new_names2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for line in csv_reader:
        print(line)

new_section(f"Using the dict reader to auto-parse headers")
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['email'])

new_section(f"Using the dict writer to auto-parse headers")
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names3.csv', 'w') as new_file:
        # Declare what the fields are
        fieldnames = ['first_name', 'last_name', 'email']
        # More arguments required
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,
                                    delimiter='\t', lineterminator='\n')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
print("See new_names3.csv")

new_section(f"dict writer to only include some fields")
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names4.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,
                                    delimiter='\t', lineterminator='\n')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
print("See new_names4.csv")