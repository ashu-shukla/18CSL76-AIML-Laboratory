# DataSet:
# sky,airtemp,humidity,wind,water,forcast,enjoysport
# sunny,warm,normal,strong,warm,same,yes
# sunny,warm,high,strong,warm,same,yes
# rainy,cold,high,strong,warm,change,no
# sunny,warm,high,strong,cool,change,yes

import csv
a = []
print('The given training dataset:')
with open('enjoysport.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        a.append(row)
        print(row)

no_attributes = len(a[0])-1

print('The initial values of hypothesis')
s = ['0']*no_attributes
g = ['?']*no_attributes
print('Specific', s)
print('General', g)
for j in range(0, no_attributes):
    s[j] = a[1][j]

print(s)
print('Computing elimination')
temp = []
for i in range(0, len(a)):
    print('----------------------------------------------------------')
    if a[i][no_attributes] == 'yes':
        for j in range(0, no_attributes):
            if a[i][j] != s[j]:
                s[j] = '?'
        for j in range(0, no_attributes):
            for k in range(0, len(temp)):
                if temp[k][j] != '?' and temp[k][j] != s[j]:
                    del temp[k]
        print('For positive training', i, 'the Specific Hypothesis is', s)
        if len(temp) == 0:
            print('For positive training', i, 'the general Hypothesis is', g)
        else:
            print('For positive training', i, 'the general Hypothesis is', temp)
    if a[i][no_attributes] == 'no':
        for j in range(0, no_attributes):
            if s[j] != a[i][j] and s[j] != '?':
                g[j] = s[j]
                temp.append(g)
                g = ['?']*no_attributes
        print('For negative training', i, 'the Specific Hypothesis is', s)
        print('For negative training', i, 'the general Hypothesis is', temp)
