#coding:utf-8

import sys

def getCSV(datafile):
	f = open(datafile,"r")
	res = f.read()
	f.close()
	return res

def order():
	data = getCSV("order.csv")
	line = data.split("\n")
	i = 1
	for row in line:
		try:
			column = row.split(",")
			field = len(column)
			ingredient = column[2].split(";")
			field_i_o = len(ingredient[0].split(":"))
			field_i_p = len(ingredient[1].split(":"))
			msg = "line:%d, field:%d, field_i_o:%d, field_i_p:%d" % (i, field, field_i_o, field_i_p)
			print msg
			i += 1
		except:
			print row

if __name__ == '__main__':
	args = sys.argv
	if not len(args) == 2:
		print "1 argument is required."
		quit()
	if args[1] == "order":
		order()

