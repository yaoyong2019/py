import xlwings as xw
app=xw.App(visible=False,add_book=False)
app.display_alerts=False
app.screen_updating=False
filepath='example1.xlsx'
wb=app.books.open(filepath)
wb.sheets['pdata'].range('A1').value='rs'
sht=wb.sheets[1]
rng1=sht.range('A1')#单元格
rng2=sht[0,2]#单元格第一行第三列
rng3=sht.range('B2:B6')#单元格，实际为B2~F2
rng4=sht[2:7,3]#单元格第三行第4至第8列共6
rng5=sht.range('c1').options(transpose=True)#按列写入
rng6=sht.range('d1:d3').options(transpose=True)
rng7=sht.range('e1').expand('table')#二维表
rng1.value='Hello'
rng2.value='ppp'
rng3.value=[1,2,3,4,5]
rng4.value=[12,24,36,48,50,65]
rng5.value=[33,44,55,66,77,88]
rng6.value=['a','b','c','d']
rng7.value=[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

#读取
print(sht.range('a1:d4').value)
a = sht.range('a1:d1').value
print(a)
# for i in a:
#   print(i)
#   print(type(i))

# a = sht.range('a:a').value#1048576个元素的列表
# print(len(a))

#读取一列
rng = sht.range('a1').expand('table')
nrows = rng.rows.count
b = sht.range(f'a1:a{nrows}').value
b1= sht.range('a1:a6').value
print(len(b),nrows)
print(b,b1)

#读取一行
rng = sht.range('b1').expand('table')
ncols = rng.columns.count
#用切片
fst_col = sht[0,:ncols].value#第一行
fst_col1= sht[1,1:ncols].value#第二行

print(len(fst_col))
print(fst_col,fst_col1)
for i in fst_col:
  print(i)

wb.save()
wb.close()
app.quit()