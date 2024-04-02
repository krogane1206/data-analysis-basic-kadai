# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:39:32 2024

@author: excal
"""

import numpy as np

A = np.array([[0, 1], [2, 3], [4, 5]])
B = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
#行列の積を計算するコードを作成
#行ベクトル　と　列ベクトル　の内積を要素とする行列が新しく作成される
np.dot(A, B)
#np.dot(A, B) の計算　→　変数ABに代入
AB = np.dot(A, B)
#行列の計算結果を表示する
print("行列の計算結果は以下の通りとなります")
print(AB)

#行列の要素の最大値を求める
np.max(AB)
#行列の要素の最大値を、変数AB_maxに代入する
AB_max = np.max(AB)
#行列の要素の最大値を、表示する
print(f"行列の要素の最大値は{AB_max}です。")
