from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import r2_score as R2
import sys
import pickle
import pandas as pd


def main():
    # 保存したモデルの読み込み
    model = pickle.load(open("src/mymodel.pkl", "rb"))
    
    # 標準入力からデータの読み込み
    input_data = []
    for line in sys.stdin:
        input_data.append(line.strip().split(","))
    
    # 読み込んだモデルで回帰
    df = pd.DataFrame(data=input_data[1:], columns=input_data[0])
    X = df[["MaxEStateIndex", "MinEStateIndex"]]
    y_pred = model.predict(X)

    # 結果を標準出力
    for output in y_pred:
        print(output)

if __name__ == "__main__":
    main()
