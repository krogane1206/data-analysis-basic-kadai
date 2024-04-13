# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 00:05:04 2024

@author: excal
"""

#サンプルデータの取得
#サンプルデータの分割
#予測モデルのインスタンス化
#予測モデルの学習
#予測モデルの評価
#予測

#1、サンプルデータの取得
#ワインの成分　および　種別のデータを取得
from sklearn.datasets import load_wine

#インポートしたload_wine関数を実行して、datasetに代入
dataset = load_wine()
dataset

dataset.data

dataset.feature_names

import pandas as pd
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df.head()

dataset.target

df['category'] = dataset.target
df.head()

#ワインの成分13要素　と　ワインの種別　データが178レコード存在することを確認。
df.shape

#2、サンプルデータの分割
#機械学習の予測モデルにインプットする側のデータ　→　ワインの成分を代入
x = dataset.data
#予測値として出力される側のデータ　→　ワインの種別を代入
y = dataset.target

#学習用データ　と　テストデータに分割する
from sklearn.model_selection import train_test_split

#学習データ　と　テストデータ　を分割。第一引数に「説明変数」・第二引数に「目的変数」をセット。
#学習　と　テスト　の分割比率は、7：3の比率で分割。　→　test_size　のパラメータを調整。
#機械学習のモデル構築の際　→　random_state　を設定することで乱数生成を制御する。
train_test_split(x, y, test_size = 0.3, random_state = 5)

#超重要　→　目的変数で予測された値が、実際の目的変数とどれだけ近いかを確認する
#学習データの精度は良いが、テストデータの精度は良くない場合（過学習）の為。、

#説明変数の学習データ、説明変数のテストデータ、目的変数の学習データ、目的変数のテストデータ
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=5)

print(x.shape, x_train.shape, x_test.shape, y.shape, y_train.shape, y_test.shape)

#3、予測モデルのインスタンス化について
#モデル構築　→　決定木　から　ランダムフォレストへ　変更する
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=3)

#４、予測モデルの学習
#　この学習を実行することで、学習を完了する
model.fit(x_train, y_train)


#５、予測モデルの評価
#　説明変数x(ワインの成分)のテストデータ　→　x_testを指定する。その予測値をy_predに代入。
#y_pred = model.predict(x_test)
#y_pred

# 目的変数y（ワインの種別）のテストデータを確認する。
y_test

#metricsモジュールのaccuracy_score関数を実行すること　→　正解率を出力
#y_testの54データのうち、y_predのデータがいくつヒットしたのか割合が正解率。

#from sklearn.metrics import accuracy_score

#インポートしたaccuracy_score関数を実行します。第一引数にテストデータであるy_testを、第２引数に予測値であるy_predをセット
#accuracy_score(y_test, y_pred)

#学習用データ　と　テストデータの比較
model.score(x_train, y_train)
model.score(x_test, y_test)
