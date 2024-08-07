import numpy as np
from sklearn.model_selection import train_test_split


def split_run(dataset):

    ### This function is responsible to defining X, y variables and splitting data into train and test

    # Defining variable X, y
    X = dataset.drop(['Churn'], axis=1)
    y = dataset['Churn']

    # Spliting the dataset in Train and Test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test