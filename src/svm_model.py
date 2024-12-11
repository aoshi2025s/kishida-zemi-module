from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from joblib import dump
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd

"""
vectorsは、シリアライズされたベクトル化モデル
targetsは、学習データに対する正解ラベル

targets = [0, 1, 1, 0]
"""


def serialize_svm_model(vectors, targets, feature_names):
    input_train, input_test, output_train, output_test = train_test_split(
        vectors, targets, test_size=0.3, random_state=None
    )

    # スケーリング(標準化)
    sc = StandardScaler()
    sc.fit(input_train)
    input_train_std = sc.transform(input_train)
    input_test_std = sc.transform(input_test)

    # グリッドサーチ
    param_list = [0.001, 0.01, 0.1, 1, 10, 100]
    best_score = 0
    best_parameters = {}
    for C in param_list:
        svm = SVC(kernel="linear", C=C)
        scores = cross_val_score(svm, vectors, targets, cv=5)
        score = np.mean(scores)
        if score > best_score:
            best_score = score
            best_parameters = {"C": C}
    print(f"最良スコア={best_score}")
    print(f"最良ハイパーパラメータ={best_parameters}")

    # 学習
    svc_model = SVC(kernel="linear", **best_parameters)
    svc_model.fit(input_train_std, output_train)

    # 学習データで精度確認・近藤行列
    pred_train = svc_model.predict(input_train_std)

    print(classification_report(output_train, pred_train))
    df_cfm = pd.DataFrame(confusion_matrix(output_train, pred_train))
    print(df_cfm)

    accuracy_train = accuracy_score(output_train, pred_train)
    print("training data accuracy: %.2f" % accuracy_train)

    # テストデータで精度確認・混同行列
    pred_test = svc_model.predict(input_test_std)
    df_cfm = pd.DataFrame(confusion_matrix(output_test, pred_test))
    print(df_cfm)
    accuracy_test = accuracy_score(output_test, pred_test)
    print("test data accuracy: %.2f" % accuracy_test)

    # modelのシリアライズ
    dump(svc_model, "../joblib/svm_model.joblib")
    dump(feature_names, "../joblib/feature_names.joblib")
