import csv
with open('dep.csv', 'r') as f:
    reader = csv.reader(f)

    with open('new.csv', 'w', newline='') as g:
        writer = csv.writer(g)

        for i in range(5):
            writer.writerow(next(reader))

    with open('new.csv', 'r') as g:
        reader = csv.reader(g)
        for row in reader:
            print(row)
