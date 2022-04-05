results = []
valid_input = set("1234567890+-^*/%!")

while (True):
	try:
		calculate = input("\nInput: ")
		if valid_input.issuperset(calculate):
			result = f"\nResult: [{ eval(calculate) }]"
			results.append(calculate + eval(calculate))
			print(result)
		elif calculate == "clear":
			clear()
		elif calculate == "history":
			for element in results:
				print(f"\n[{ element }]")
		elif calculate == "end":
			break
	except:
		print("\nInvalid input.")
	

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')