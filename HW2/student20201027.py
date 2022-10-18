#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']

row_id = 1;
sum_list = []

for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v

		sum_list.append(sum_v)
	row_id += 1

#grade

sorted_list = sorted(sum_list)
sorted_list.reverse()

#학점 비율 설정
  
row_id2 = 1
length = len(sum_list)
cal_grade = []
cal_grade.append((int)(length * 0.3)) 
cal_grade.append((int)(length *0.7))
cal_grade.append((int)(length))
#학점 계산

row_id2 = 1

for row in ws:
	if row_id2 != 1:
		if ws.cell(row = row_id2, column = 7).value <= (sorted_list[cal_grade[0]]):
			if ws.cell(row = row_id2, column = 7).value <= (int)(length * 0.3 *0.5): 
				ws.cell(row = row_id2, column = 8).value = 'A+'
			else:
				ws.cell(row = row_id2, column = 8).value = 'A0'
		elif ws.cell(row = row_id2, column = 7).value <= (sorted_list[cal_grade[1]]):
			if ws.cell(row = row_id2, column = 7).value <= (int)(length * 0.7 * 0.5):
				ws.cell(row = row_id2, column = 8).value = 'B+'
			else:
				ws.cell(row = row_id2, column = 8).vlaue = 'B0'
		else:
			if ws.cell(row = row_id2, column = 7).value <= (int)(length * 0.5):
				ws.cell(row=row_id2, column = 8).value = 'C+'
			else:
				ws.cell(row = row_id2, column=8).value = 'C0'	


wb.save("student.xlsx")
