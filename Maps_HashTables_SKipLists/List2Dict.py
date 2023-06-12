sal_info_keys = ["Austin","Portland","Dallas"]
sal_info_values = ["90000","100000","89000"]

sal_info = {}

indx = 0
for key in sal_info_keys:
    values = sal_info_values[indx]
    sal_info[key] = values
    
print(sal_info)