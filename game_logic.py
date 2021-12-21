from sklearn import tree
import pandas as pd
import numpy as np

# Create the classification tree

# Load data
df = pd.read_csv('data/pokemon_preprocessed.csv')

X = df.drop(['name', 'pokedex_number'] , axis=1)
y = df['pokedex_number']

# Fit model classification tree model
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

tree = clf.tree_
node = 0      #Index of root node
while True:
    feat,thres = tree.feature[node],tree.threshold[node]
    #print(feat,thres)
    v = float(input(f"The value of {X.columns[feat]}: "))
    if v<=thres:
        node = tree.children_left[node]
    else:
        node = tree.children_right[node]
    if tree.children_left[node] == tree.children_right[node]: #Check for leaf
        label = np.argmax(tree.value[node])
        print("We've reached a leaf")
        print(f"Predicted Label is: {label} {df.loc[df['pokedex_number'] == label+1]['name']}")
        break