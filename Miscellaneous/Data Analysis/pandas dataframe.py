import pandas as pd
purchase_1 = pd.Series({'bgn': 5, 'ugb': 2, 'uhn': 9})
purchase_2 = pd.Series({'bgn': 999, 'ugb': 234, 'uhn': 176})
purchase_3 = pd.Series({'bgn': 99, 'ugb': 24, 'uhn': 16})
new = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['store1', 'store2', 'store3'])
k = []
for index, row in new.iterrows():
	print (row['bgn'])
	k.append(row['bgn'] * 2)
new['kimmmm'] = k
print (new)
print (new[new.index == 'store1'].mean())