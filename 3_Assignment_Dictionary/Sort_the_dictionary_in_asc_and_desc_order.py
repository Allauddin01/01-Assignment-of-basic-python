
import operator
dict_1={'A':1, 'C':2, 'B':3,'E':5,'D':4,'G':7,'F':6 }
print(dict_1) #print  the oringinal dictionary
sort_d=sorted(dict_1.items(),key=operator.itemgetter(1))
print('the dictionary is in Ascending order',sort_d)
sor_1=dict(sorted(dict_1.items(),key=operator.itemgetter(1),reverse=True))
print(sor_1)

