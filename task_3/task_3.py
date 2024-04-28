import sys
from pathlib import Path
from colorama import Fore, Back, Style

def list_directory(path, level = 0):
	if not path.is_dir():
		raise ValueError(f"Зазначений шлях {path} не є директорією.")

	indent = '    ' * level
	try:
		for item in path.iterdir():
			if item.is_dir():
				print(Fore.BLUE + f"{indent}{item.name}/")
				list_directory(item, level + 1)
			else:
				print(Fore.GREEN + f"{indent}{item.name}")
	except PermissionError:
		print(Fore.RED + f"{indent}Немає доступу до папки: {item.name}")
	

def main():
    if len(sys.argv) != 2:
        print("Використання: python task_3.py [шлях до директорії]")
        sys.exit(1)

    path = Path(sys.argv[1])
    print(path)
    if not path.exists():
        print(Fore.RED + "Зазначений шлях не існує.")
        sys.exit(1)

    list_directory(path)

if __name__ == '__main__':
    main()