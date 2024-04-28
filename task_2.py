def get_cats_info(path):
	cats_list = []
	try:
		with open(path, 'r', newline='', encoding='utf-8') as file:
			lines = [el.strip() for el in file.readlines()]
			for line in lines:
				cat_arr = line.split(',')
				cats_list.append({"id": cat_arr[0], "name": cat_arr[1], "age": cat_arr[2]})
		return cats_list		
	except FileNotFoundError:		
		return None


cats_info = get_cats_info("./cats_file.txt")
if cats_info is not None:
	print(cats_info)
else:
	print(f"Помилка, такого файла не існує")