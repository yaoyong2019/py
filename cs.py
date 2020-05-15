import xlwings as xw
app=xw.App(visible=False,add_book=False)
app.display_alerts=False
app.screen_updating=False
filepath='example1.xlsx'
wb=app.books.open(filepath)
#print(wb.sheets['pdata'].range('A2').value)
wb.sheets['pdata'].range('A4').value='天道酬勤'  #这句是写了
wb.save()
wb.close()
app.quit()