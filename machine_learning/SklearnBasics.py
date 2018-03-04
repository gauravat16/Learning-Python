import sklearn
import numpy as np
import pandas as pd
import os.path

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib

data_set_url = 'data/winequality-red.csv'

data = pd.read_csv(data_set_url, delimiter=';')

y = data.quality
x = data.drop('quality', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123, stratify=y)

if os.path.isfile('data/rf_regressor.pkl'):
    clf2 = joblib.load('data/rf_regressor.pkl')

    print(clf2.predict(x_test))


else:
    pipeline = make_pipeline(preprocessing.StandardScaler(),
                             RandomForestRegressor(n_estimators=100))

    hyperparameters = {'randomforestregressor__max_features': ['auto', 'sqrt', 'log2'],
                       'randomforestregressor__max_depth': [None, 5, 3, 1]}

    clf = GridSearchCV(pipeline, hyperparameters, cv=10)

    clf.fit(x_train, y_train)

    print(clf.best_params_)

    y_pred = clf.predict(x_test)
    print(r2_score(y_test, y_pred))
    print(mean_squared_error(y_test, y_pred))

    joblib.dump(clf, 'data/rf_regressor.pkl')
