import openpyxl

wb = openpyxl.load_workbook(filename='example.xlsx')
print(type(wb))

# Gettng sheets from the workbook
wb.sheetnames()
sheet = wb['sheet3']
print(sheet)
