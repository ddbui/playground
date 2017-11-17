import csv

csv_file2 = 'tecl.csv'
result_file = "tecl_result_10_30.csv"
array_values = []
header = 0
invest_amount = 2000
empty_line = []
beginning = True
ending = False
#minus_percent = 0.9 # -10%
#plus_percent = 1.1 # +10%
minus_percent = 0.9 # -10%
plus_percent = 1.3 # +30%
#minus_percent = 0.9 # -10%
#plus_percent = 1.5 # +10%
beginning_price = 0
last_result = 0
	
def float_to_int(float_num):
	str_num = str(float_num)
	dot = "."
	dot_index = str_num.index(dot)
	str_num = str_num[:dot_index]
	
	return int(str_num)

##### Read data row-by-row from 2 csv files
with open(csv_file2, 'r') as f1:
	reader1 = csv.reader(f1)
	for row1 in reader1:
		result_array = []
		
		# Print the header
		if header == 0:
			header = 1
			result_array.append("Date")
			result_array.append("Price")
			result_array.append("Investment Amount")
			result_array.append("Shares")
			result_array.append("Minus")
			result_array.append("Plus")
		else:
			# Column 1 = Date (date_)
			# Column 2 = Adjust Closed Price (price_)
			# Column 3 = Investment Amount (invest_amount)
			# Column 4 = Shares (shares_)
			# Column 5 = -10% (minus_)
			# Column 6 = +10% (plus_)
			date_ = row1[0]
			price_ = float(row1[5])
			shares_ = invest_amount / price_
			minus_ = ""
			plus_ = ""
			if beginning == True:
				minus_ = price_ * minus_percent
				plus_ = price_ * plus_percent
				beginning_price = price_
				beginning = False
				beginning_minus = minus_
				beginning_plus = plus_
			else:
				if (price_ <= beginning_minus):
					ending = True
				if (price_ >= beginning_plus):
					ending = True
				if ending == True:
					minus_ = ((price_ - beginning_price) / beginning_price)
					last_result = (invest_amount * minus_) + last_result
					plus_ = last_result
					beginning = True
					ending = False
		
			result_array.append(date_)
			result_array.append(price_)
			result_array.append(invest_amount)
			result_array.append(shares_)
			result_array.append(minus_)
			result_array.append(plus_)
					
		array_values.append(result_array)
		
##### Write data to results file
with open(result_file, 'w', newline='') as fp:
	a = csv.writer(fp, delimiter=',')
	#data = [['Me', 'You'],
	#		['293', '219'],
	#		['54', '13']]
	a.writerows(array_values)