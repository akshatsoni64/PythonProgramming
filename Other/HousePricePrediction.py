import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

test = pd.read_csv('Dataset/test.csv')

x_test = test.drop(
    ['Electrical', 'MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope',
     'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'SaleType', 'SaleCondition', 'RoofStyle',
     'RoofMatl', 'Exterior1st', 'Exterior2nd', 'ExterQual', 'ExterCond', 'Foundation', 'Heating', 'HeatingQC',
     'CentralAir', 'KitchenQual', 'Functional', 'PavedDrive', 'YrSold', 'Id', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF',
     'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'GarageCars', 'GarageArea', 'Street'], axis=1)
x_test.dropna(axis=1, inplace=True)

mod = pickle.load(open('Model/HousePrice.model', 'rb'))

out = mod.predict(x_test)

print(out[0])
