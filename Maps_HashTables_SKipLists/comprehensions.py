sal_info_keys = ["Austin","Portland","Dallas"]
sal_info_values = ["90000","100000","89000"]

# sal_info = {}
# for key,value in zip(sal_info_keys,sal_info_values):
#     sal_info[key] = value
# print(sal_info)

sal_info = {sal_info_keys[indx]:sal_info_values[indx] for indx in range(0,len(sal_info_keys))}
print(sal_info)
