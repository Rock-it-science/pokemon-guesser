# Planning

 - Pokemon dataset
 - Python decision trees?
    - https://scikit-learn.org/stable/modules/tree.html
    - Take input as all steps up until this point, and output is the next question to ask, or making a guess
      - Re-run tree with given input and predict output and get confidence of top predictions
      - If above a threshold, make guess, otherwise ask another question
    - Every round determine which question would provide the greatest utility i.e. which question would remove the most options (want as close to a 50/50 split with each question as possible).
    - Every question is a yes or no question.
      - This requires categorical variables with more than 2 categories to be given dummy variables.
