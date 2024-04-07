# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 00:45:19 2024

@author: excal
"""

#カテゴリー列の要素（弁当、デザートなど）の出現頻度をカウントして、結果を棒グラフで表示
#商品番号列の商品番号ごとに、注文数の基本統計量を求める

import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

#csvファイルをデータフレームとして読み込む
df = pd.read_csv("C:/Users/excal/OneDrive/デスクトップ/統計・分析方法/サムライエンジニア/python/授業/sample_pandas_6.csv")

#category data　を読み込む
category_df = pd.read_csv("C:/Users/excal/OneDrive/デスクトップ/統計・分析方法/サムライエンジニア/python/授業/category.csv")

#商品番号をマージ
df = pd.merge(df, category_df[['商品番号', 'カテゴリー']], how = 'inner', on='商品番号')
df

#各カテゴリーを集計
category_counts = df['カテゴリー'].value_counts()
print(category_counts)

#集計結果を棒グラフに表示する
category_counts.plot(kind = 'bar')

# 商品番号ごとの注文数の基本統計量を計算
order_stats = df.groupby('商品番号')['注文数'].describe()

# 統計情報を表示
print(order_stats)
