import csv

def csv_merge(fl1, fl2, outfl):
    fls, hds, rows = [fl1, fl2], [], []
    for fl in fls:
        with open(fl, mode="r") as read_fl:
            reader = csv.DictReader(read_fl) 
            hds += list(reader.fieldnames) # collect the column heads in a list
            # rows of the reader are dicts, with key the column name and value the entry
            for row in reader: rows.append(row) 
    hds = list(set(hds)) # unique hds
    with open(outfl, mode="w") as write_fl:
        # If hd does not appear in row, write empty space as value
        writer = csv.DictWriter(write_fl, fieldnames=hds, restval='') 
        writer.writeheader()
        for r in rows: writer.writerow(r)
    print(f'Merge of {fl1!r} and {fl2!r} complete, written to {outfl!r}.')

csv_merge("csv1.csv", "csv2.csv", "csv_fin.csv")