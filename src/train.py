from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import r2_score as R2
from sklearn.model_selection import train_test_split
import sys
import pickle
import pandas as pd

# データセットの読み込み
dataset_df = pd.read_csv("dataset.csv")

# データセットから説明変数と回帰対象の変数を取り出し(今回はWater Solubilityを回帰)
X = dataset_df[["MaxEStateIndex", "MinEStateIndex"]]
y = dataset_df["Water Solubility"]

# 学習用と評価用にデータを分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 線形回帰
model = LR()
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 決定係数R2でモデルの性能評価
print("Train score: ", R2(y_train, y_train_pred))
print("Test score: ", R2(y_test, y_test_pred))

##モデルの保存
pickle.dump(model, open("src/mymodel.pkl", "wb"))

