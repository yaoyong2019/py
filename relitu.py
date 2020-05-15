# import pandas as pd 
# from pyecharts import options as opts
# from pyecharts.charts import HeatMap
# data = pd.read_excel('学生成绩.xlsx') 
# x = data['姓名'].tolist() 
# y = data.columns.values[1:].tolist() 
# values = [[i, j, int(data.iloc[i, j+1])] for i in range(len(x)) for j in range(len(y))]
# myHeatMap = HeatMap() 
# myHeatMap.add_xaxis(x) 
# myHeatMap.add_yaxis("学生成绩", y, values) 
# myHeatMap.set_global_opts(title_opts=opts.TitleOpts(title="HeatMap"), 
#                           visualmap_opts=opts.VisualMapOpts(min_=60, max_=100)) 
# myHeatMap.render(path='学生成绩.html') 
import numpy as np
from numpy import random
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns
sns.set()
N = 20
R = random.randn(N, N)
fig = plt.figure()
sns_plot = sns.heatmap(R)
# fig.savefig("heatmap.pdf", bbox_inches='tight') # 减少边缘空白
plt.show()