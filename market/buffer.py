from flask import flash
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
def predict(price, company, id):
    sc = StandardScaler()
    df = pd.read_csv("C:\\Users\\angai\\Downloads\\shoes.csv")
    df.drop_duplicates()
    bool = False
    if company in df["Company"].unique():
        def parse(x):
            x = x[1:]
            if "," in x:
                x = x.replace(",", '')
            return int(x)

        df["Price"] = df["Price"].apply(lambda x: parse(x))
        df["Real Price"] = df["Real Price"].apply(lambda x: parse(x))
        data = df[df["Company"] == company]
        print(price)
        if price<0 or price>max(data["Real Price"]):
            flash("The price seems too much give a more reasonable price. Max price is: " + str(max(data["Real Price"])), category="danger")
            bool=False
            return bool
        x = data["Real Price"]
        y = data["Price"]
        Y = data["Price"]
        X = data["Real Price"]
        # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        reg = LinearRegression()
        price = (price - (np.mean(np.array(X)))) / (np.std(np.array(X)))
        X = sc.fit_transform(X.values.reshape(-1, 1))
        Y = sc.fit_transform(Y.values.reshape(-1, 1))
        reg.fit(X, Y)
        Y_Pred = reg.predict(X)
        Y_Pred1 = reg.predict(np.array([price]).reshape(-1, 1))
        y1 = list(Y_Pred1)[0][0]
        # print(y1)
        # print(price)
        y11 = int(y1 * np.std(np.array(y)) + np.mean(y))
        price1 = price * np.std(np.array(x)) + np.mean(np.array(x))
        plt.plot(X, Y_Pred, label="Regression Line", c="b")
        # plt.text(4, 4, str(price), c="r")
        plt.scatter(price, y1, c="r", label="Your price")
        plt.text(price, y1 + 1, str(price1) + " - " + str(y11), c="r")
        plt.scatter(X, Y, label="Actual", c="g", alpha=0.7)
        plt.legend()
        plt.title(company + " - Analysis")
        plt.show()
        # print("Root mean Square Error: " + str(mean_squared_error(Y, Y_Pred)))
        # print("Mean Absolute Error: " + str(mean_absolute_error(Y, Y_Pred)))
        bool=True
        return y11, bool
    else:
        flash("No such company exists", category="danger")
        bool=False
        return bool
def represent(company):
    df = pd.read_csv("C:\\Users\\angai\\Downloads\\shoes.csv")
    df.drop_duplicates()
    bool = False
    if company in df["Company"].unique():
        def parse(x):
            x = x[1:]
            if "," in x:
                x = x.replace(",", '')
            return int(x)

        df["Price"] = df["Price"].apply(lambda x: parse(x))
        df["Real Price"] = df["Real Price"].apply(lambda x: parse(x))
        data = df[df["Company"] == company]
        x = data["Real Price"]
        y = data["Price"]
        plt.xlabel(company)
        plt.boxplot(y)
        plt.show()
def represent_bar(company):
    df = pd.read_csv("C:\\Users\\angai\\Downloads\\shoes.csv")
    df.drop_duplicates()
    df.isnull().sum()
    bool = False
    if company in df["Company"].unique():
        def parse(x):
            x = x[1:]
            if "," in x:
                x = x.replace(",", '')
            return int(x)

        df["Price"] = df["Price"].apply(lambda x: parse(x))
        df["Real Price"] = df["Real Price"].apply(lambda x: parse(x))
        data = df[df["Company"] == company]
        x = data["Real Price"]
        y = data["Price"]
        plt.xlabel(company)
        x = ["maximum price", "minimum price"]
        y = [max(y), min(y)]
        plt.bar(x, y)
        plt.show()