# DataSet:
# Outlook,Temperature,Humidity,Windy,Play
# overcast,hot,high,False,yes
# overcast,cool,normal,True,yes
# overcast,mild,high,True,yes
# overcast,hot,normal,False,yes
# rainy,mild,high,False,yes
# rainy,cool,normal,False,yes
# rainy,cool,normal,True,no
# rainy,mild,normal,False,yes
# rainy,mild,high,True,no
# sunny,hot,high,False,no
# sunny,hot,high,True,no
# sunny,mild,high,False,no
# sunny,cool,normal,False,yes
# sunny,mild,normal,True,yes


import pprint
import numpy as np
import pandas as pd
df = pd.read_csv('4data.csv')

# print(df)


def find_entropy_of_whole_dataset(df):
    col = df.keys()[-1] # Get the last column name.
    entropy = 0 # Initialize entropy to 0.
    values = df[col].unique() # Get unique values of that col, here it is 'yes' and 'no'.
    for value in values: # For each unique value we will calculate the entropy.
        fraction = df[col].value_counts()[value]/len(df[col]) # Getting the fraction [9+,5-] ==> 9/14 and 5/14
        entropy = entropy+(-fraction*np.log2(fraction))# Getting the log2 ==> 9/14(log2(9/14))  and  5/14(log2(5/14))
    # Returning the datasets entropy
    return entropy


def find_entropy_attribute(df, attr):
    col = df.keys()[-1]
    target_variables = df[col].unique()
    attr_variables = df[attr].unique()
    attr_entropy = 0
    for variable in attr_variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attr][df[attr] == variable]
                      [df[col] == target_variable])
            den = len(df[attr][df[attr] == variable])
            if num==0:
                entropy=0
            else:
                fraction=num/(den)
                entropy = entropy+(-fraction*np.log2(fraction))
        final_fraction = den/len(df)
        attr_entropy = attr_entropy+(-final_fraction*entropy)
    return attr_entropy


def find_winner(df):
    IG = []
    for key in df.keys()[:-1]:
        dataset_entropy=find_entropy_of_whole_dataset(df)
        IG.append(dataset_entropy+find_entropy_attribute(df, key))
    # Returning the attribute name with highest IG.
    return df.keys()[:-1][np.argmax(IG)]


def get_subtable(df, node, value):
    # print(df[df[node] == value].reset_index(drop=True))
    return df[df[node] == value].reset_index(drop=True)


def buildtree(df, tree=None):
    node = find_winner(df)
    attr_values = np.unique(df[node])
    # print(attr_values)
    if tree is None:
        tree = {}
        tree[node] = {}
        for value in attr_values:
            subtable = get_subtable(df, node, value)
            clvalue, counts = np.unique(subtable['Play'], return_counts=True)
            # print(counts)
            if len(counts) == 1:
                tree[node][value] = clvalue[0]
            else:
                tree[node][value] = buildtree(subtable)
        return tree


t = buildtree(df)
pprint.pprint(t)
