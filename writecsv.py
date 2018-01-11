import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([, 'col2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])

    