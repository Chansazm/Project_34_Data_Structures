import csv

with open('TreeOrdersSubset.csv', mode = 'r') as infile:
    reader = csv.reader(infile)
    
    treeOrders = {}
    for row in reader:
        key = row[0]
        
        if (key not in treeOrders):
            treeNum = row[1] 
            treeOrders[key] = treeNum
        else:
            treeNum = row[1]
            prev_count = treeOrders[key]
            treeOrders[key] = int(prev_count) + int(treeNum)
print(treeOrders.items())
infile.close()