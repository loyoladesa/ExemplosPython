# instead of doing

a = 1
b = 2
c = 3

# you can do

a,b,c = 1,2,3

#instead of doing

data_1 = []
data_2 = []
data_3 = []
data_4 = []

# you can do

data_1, data_2,data_3,data_4 = [],[],[],[]

# or use list comprehension

data_1, data_2,data_3,data_4 = [[] for i in range(4)]
