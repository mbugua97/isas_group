import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle



data = pd.read_csv('dataset.csv', usecols=['Item', 'rainfall', 'avg_temp'])

X_train, X_test, y_train, y_test = train_test_split(data[['avg_temp', 'rainfall']], data['Item'], test_size=0.25)


clf = DecisionTreeClassifier()


clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)





with open('crop_model.pkl', 'wb') as f:
    pickle.dump(clf, f)
