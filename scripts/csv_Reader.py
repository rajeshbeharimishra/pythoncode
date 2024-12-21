import csv
filename="sample_data.csv"

def read_cell(x, y):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

print (read_cell(4, 3)) 