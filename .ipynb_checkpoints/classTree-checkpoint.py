from sklearn import tree
import pandas as pd
import matplotlib as plt
import graphviz

# Load data
df = pd.read_csv('data/pokemon_preprocessed.csv')

X = df.drop(['name', 'id'] , axis=1)
y = df.id

# Fit model classification tree model
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

# Plot the tree
tree.plot_tree(clf)
#dot_data = tree.export_graphviz(clf, out_file=None)
#graph = graphviz.Source(dot_data)
#graph.render("tree")