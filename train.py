from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

def clean_data(data):
    # Clean and one hot encode data
    df = data.to_pandas_dataframe().dropna()
    string_col=df.select_dtypes(include="object").columns
    df[string_col]=df[string_col].astype("string")
    string_col=df.select_dtypes("string").columns.to_list()
    df = pd.get_dummies(df, columns=string_col, drop_first=False)
    y = df["HeartDisease"]
    x = df.drop("HeartDisease", in_place=True,axis=1)
    return x, y

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))


    ds = TabularDatasetFactory.from_delimited_files(path="https://raw.githubusercontent.com/hknguyen20/nd00333-capstone/refs/heads/master/heart.csv")
    
    x, y = clean_data(ds)

    # TODO: Split data into train and test sets.

    x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=42)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()
