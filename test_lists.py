test_data = { "hello": ["world", 1], "test": ["val", 2] }
test_data2 = [["hello", "world", 1], ["test", "val", 2] ]

# if "hello" in test_data:
	# if 1 in test_data["hello"]:
		# print("true")
	# else:
		# print("false")
# else: 
	# print("false")
	
# if "hello" in test_data2[0]:
	# print("true")
# else:
	# print("false")
	
n_1 = "hey"
n_2 = "there"
n_3 = 3
test_data.update({n_1: [n_2, n_3]})
print(test_data)