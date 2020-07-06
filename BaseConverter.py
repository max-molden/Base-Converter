class BaseConversion:

	def __init__(self, num_convert, conversion):
		self.num_convert = num_convert	# the given number on which to perform conversions
		self.orig_num = num_convert		# need to save it so can use this num in the output, self.num_convert will go to 0 bc of my logic
		self.conversion = conversion    # will be a number [0, 5] for now, supports back and forth between 10 and 2, 8, 16, maybe add more later
		self.result = ''				# starting as empty string so can concatenate digits infront of it, see logic later
		self.num_len = 0				# initialized to 0, to be used when converting back to base 10, will get len of str, see in funcs to conv to base 10
		self.dec_sum = 0 				# start at 0, will be running sum for when converting back to base 10
		self.PickConversion()			# calls func to decide which converter function to call
		self.conversion_str = ''		# creates empty string to change in func call; takes numerical pick for conversion see self.conversion, 
										# and makes it a string detailing what conversion was done to mmake output look nice
		self.ConversionChoiceToStr()	# calls func that does above ^^
		self.OutputResults()			# calls output function

	def PickConversion(self):			# takes numerical input from given list in print out [0,5] (for now) and decides which function to use for conversion then calls it
		if self.conversion == 0:
			self.Base10toBase2()
		elif self.conversion == 1:
			self.Base2toBase10()
		elif self.conversion == 2:
			self.Base10toBase8()
		elif self.conversion == 3:
			self.Base8toBase10()
		elif self.conversion == 4:
			self.Base10toBase16()
		elif self.conversion == 5:
			self.Base16toBase10()

	def Base10toBase2(self):			# converts Base 10 to Base 2, returns result as an int
		# emulating a do while loop with a while true then an if inside for break condition
		self.num_convert = int(self.num_convert)
		while (True):
			div_rem = self.num_convert % 2
			div_result = self.num_convert // 2
			self.num_convert = div_result
			self.result = str(div_rem) + self.result

			if (self.num_convert == 0):
				break

		return self.result

	def Base10toBase8(self):			# converts Base 10 to Base 8, returns result as an int
		self.num_convert = int(self.num_convert)
		# emulating do while loop with while true and an if inside for break condition
		while (True):
			div_rem = self.num_convert % 8
			div_result = self.num_convert // 8
			self.num_convert = div_result
			self.result = str(div_rem) + self.result

			if (self.num_convert == 0):
				break

		return self.result

	def Base10toBase16(self):			# converts Base 10 to Base 16, returns result as an int
		self.num_convert = int(self.num_convert)
		hex_dict = {10:'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'} 		# dict to use for hex vals greater than 9 (0-9 + A-F)
		# emulating do while loop with while true and an if inside for break condition
		while (True):
			div_rem = self.num_convert % 16
			div_result = self.num_convert // 16
			self.num_convert = div_result
			if (div_rem > 9):
				div_rem = hex_dict[div_rem]
				self.result = str(div_rem) + self.result
			else:
				self.result = str(div_rem) + self.result

			if (self.num_convert == 0):
				break

		return self.result

	def Base2toBase10(self):			# converts Base 2 to Base 10, returns result as an int
		self.num_convert = str(self.num_convert) 		# need num digits, easier to do w len(str)
		self.num_len = len(self.num_convert) - 1		# -1 bc bits from right to left start at index 0, so MSB bit placement val is 1 less than total num bits
		for digit in self.num_convert:
			self.dec_sum += (int(digit) * pow(2, self.num_len))
			self.num_len -= 1

		self. result = self.dec_sum

		return self.result

	def Base8toBase10(self):			# converts Base 8 to Base 10, returns result as an int
		self.num_convert = str(self.num_convert) 		# need num digits, easier to do w len(str)
		self.num_len = len(self.num_convert) - 1		# -1 bc bits from right to left start at index 0, so MSB bit placement val is 1 less than total num bits
		for digit in self.num_convert:
			self.dec_sum += (int(digit) * pow(8, self.num_len))
			self.num_len -= 1

		self. result = self.dec_sum

		return self.result

	def Base16toBase10(self):			# converts Base 16 to Base 10, returns result as an int
		hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15} 		# dict to use for hex vals greater than 9 (0-9 + A-F)
		self.num_convert = str(self.num_convert) 		# need num digits, easier to do w len(str)
		self.num_len = len(self.num_convert) - 1		# -1 bc bits from right to left start at index 0, so MSB bit placement val is 1 less than total num bits
		for digit in self.num_convert:
			if (digit in hex_dict):
				digit = hex_dict[digit]
			self.dec_sum += (int(digit) * pow(16, self.num_len))
			self.num_len -= 1

		self. result = self.dec_sum

		return self.result

	def ConversionChoiceToStr(self):				# takes numerical input for conversion type and makes self.conversion_str a useful str to describe what happened, makes output look good
		if (self.conversion == 0):
			self.conversion_str = 'decimal to binary conversion'
		elif (self.conversion == 1):
			self.conversion_str = 'binary to decimal conversion'
		elif (self.conversion == 2):
			self.conversion_str = 'decimal to octal conversion'
		elif (self.conversion == 3):
			self.conversion_str = 'octal to decimal conversion'
		elif (self.conversion == 4):
			self.conversion_str = 'decimal to hexadecimal conversion'
		elif (self.conversion == 5):
			self.conversion_str = 'hexadecimal to decimal conversion'

		return self.conversion_str

	def OutputResults(self):						# outputs results in a readable manner
		print(f'Using {self.conversion_str}, your number of {self.orig_num} has been converted to {self.result}.')

delimeter = '*'										# changes what line of chars appears in output

print(delimeter*210 + '\n')							# 210 was picked bc it is the max amount of chars to fit on a full screen terminal window without adding an extra line space, try w 211 you'll see what i mean
print('This program allows conversion of numbers between different bases.')
print('Currenlty Base Conversions are only supported with positive, whole numbers (i.e. no decimals/radix points).')
print('Currently Supported Base Conversions:\n\t-- Base 10 to Base 2\n\t-- Base 2 to Base 10')
print('Choose a number from the following list in order to select the base conversion of your choice:')
table_convs = '\t0: Base 10 to Base 2\n\t1: Base 2 to Base 10\n\t2: Base 10 to Base 8\n\t3: Base 8 to Base 10\n\t4: Base 10 to Base 16\n\t5: Base 16 to Base 10'
print(table_convs)

# do-while emulation so user can enter multiple numbers w out restarting program
while (True):
	starting_num = input('\nEnter the number you wish to convert: ')
	converter_choice = int(input('Enter the conversion you would like to complete (choose from the numbered list above): '))

	while (converter_choice not in range(0,6)): # since i only have 5 options now this prevents entering wrong number and causing error
		print('Sorry, please choose one of the numbers from the above base conversion options.')
		converter_choice = int(input('Enter the conversion you would like to complete (choose from the numbered list above): '))

	print('\n' + delimeter*210)

	output = BaseConversion(starting_num, converter_choice)

	again_num = input('Would you like to enter another number to convert (y/n)? ')

	if ((again_num == 'y') | (again_num == 'Y')):
		again_table =  input('Do you need to see the table of conversion choices again (y/n)? ')

		if ((again_table == 'y') | (again_table == 'Y')):
			print(table_convs)

	if not ((again_num == 'y') | (again_num == 'Y')):
		break

'''
upload to git?
make this first try

then fix it make it more streamlined
as in less funcs probs need more selction structs to determine what nums to use
pay attention with this ^^ will need starting and ending base form user
also pay attention to when converting input to int or str, can probs limit how much i did of that
also probs attempt to do try and except blocks for data validity probs also more while loop checks? unless try/except can limit/eliminate these
make this second try

then make it even better for a terminal interface
make this third try

then maybe make it a gui and/or put in C++?
make this fourth and/or fifth try
'''