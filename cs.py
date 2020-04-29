import xlwings as xw
app=xw.App(visible=True,add_book=False)
app.display_alerts=False
app.screen_updating=False
filepath=r'f:\py\example1.xlsx'
wb=app.books.open(filepath)
wb.sheets['pdata'].range('A2').value='rensehng'
wb.save()
wb.close()
app.quit()