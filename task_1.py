def total_salary(path):
	sum = 0
	avg = 0	
	try:
		with open(path, 'r', newline='', encoding='utf-8') as file:
			lines = [el.strip() for el in file.readlines()]
			for line in lines:
				line_arr = line.split(',')
				sum += float(line_arr[1])				
		avg = sum/len(lines)
		return sum, avg
	except FileNotFoundError:		
		return None, None


total, average = total_salary("./salary_file.txt")
if total is not None and average is not None:
	print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
	print(f"Помилка, такого файла не існує")
