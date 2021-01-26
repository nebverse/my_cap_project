import sys
import scipy
import matplotlib
import pandas as pd
import numpy
import sklearn

# print("Python : {}".format(sys.version))
# print("scipy : {}".format(scipy.__version__))
# print("matplotlib : {}".format(matplotlib.__version__))
# print("pandas : {}".format(pandas.__version__))
# print("numpy : {}".format(numpy.__version__))
# print("sklearn : {}".format(sklearn.__version__))

from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master.iris.csv"
# url = "Iris.csv"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pd.read_csv(url, names=names)

# print(dataset.head(10))
# print(dataset.describe())
# print(dataset.groupby("class").size())
# print(dataset)

# univariate

# dataset.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# histgram

# dataset.hist()
# pyplot.show()

# multivariate

# scatter_matrix(dataset)
# pyplot.show()

# create training and test dataset

array = dataset.values
x = array[:, 0:4]
y = array[:, 4]
x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.2, random_state=1)

# Logistic regression
# Linear Discriminant Analysis
# K-nearest neighbours
# Classification and Regrssion Trees
# Gaussian Naive Bayes
# Support Vector Machines

models = []

models.append(("LR", LogisticRegression(solver="liblinear", multi_class="ovr")))
models.append(("LDA", LinearDiscriminantAnalysis()))
models.append(("KNN", KNeighborsClassifier()))
models.append(("NB", GaussianNB()))
models.append(("SVM", SVC(gamma="auto")))

# print(models)
results = []
names = []

for name,model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=None)
    cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring="accuracy")
    results.append(cv_results)
    names.append(name)
    # print(f"{name}: {cv_results.mean()} ({cv_results.std()})")

# compare models

pyplot.boxplot(results, labels=names)
pyplot.title("Algorithm Comparison")
# pyplot.show()

# make a prdiction on SVM

model = SVC(gamma="auto")
model.fit(x_train, y_train)
predictions = model.predict(x_validation)

print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))