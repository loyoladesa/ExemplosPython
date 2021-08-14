f = open('dataset.txt','w')
f.write('new_data')
f.close()

with open('dataset.txt','w') as f:
    f.write('novos_dados')

