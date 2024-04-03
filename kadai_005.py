# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:59:01 2024

@author: excal
"""

#step1 necesssary libraries
import matplotlib.pyplot as plt
import numpy as np 

#step2 create a ２×３　grid ob subplots
nrows, ncols = 2, 3
fig, axes = plt.subplots(nrows, ncols, figsize=(12, 8), tight_layout=True)

#step3 plt different types of graphs in each subplot
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
data_hist = np.random.normal(0, 1, 1000)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

#line plot
# y0のデータを使用しして、折れ線グラフを作成
y0 = [1, 2, -5, 2]
axes[0, 0].plot(y0)
axes[0, 0].set_title("Line Plot")

#line plot
#正弦関数を使用して作成
axes[0, 1].plot(x, y_sin)
axes[0, 1].set_title("Sine Function")

#histogram
#正規分布に従うサンプルデータdata_histをしようしてヒストグラムを作成している。
#ビン数は２０です
axes[0, 2].hist(data_hist, bins=20, color="orange")
axes[0, 2].set_title("Histogram")

#scatter plot
#ランダムな x_scatter　と　y_scatter のデータを使用して散布図を作成
axes[1, 0].scatter(x_scatter, y_scatter, color="green")
axes[1, 0].set_title("Scatter Plot")

#Bar plot
#学生の名前　・　数学のスコア　を使用して棒グラフを作成
students = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
math_scores = [85, 83,  89, 92, 88]
axes[1, 1].bar(students, math_scores, color="purple")
axes[1, 1].set_title("Math Scores")

# Pie chart
# カテゴリラベル　と　値　を使用して円グラフを作成
#　パーセンテージ表示を設定
categories = ["A", "B", "C", "D"]
values_pie = [20, 35, 30, 15]
axes[1, 2].pie(values_pie, labels=categories, autopct="%1.1f%%", startangle=90)
axes[1, 2].set_title("Category Distribution")

plt.show()