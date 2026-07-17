import sys
import csv

students = []

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].endswith(".csv") and len(sys.argv)==3 :
    try:
        with open (sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row['name'].split(', ')
                students.append({'first': first_name, 'last': last_name,'house': row["house"]})
        with open(sys.argv[2], 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(students)
    except FileNotFoundError:
        sys.exit ('Could not read invalid_file.csv')
else:
    sys.exit('Not a CSV file')
