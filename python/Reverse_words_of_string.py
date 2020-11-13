# Function to reverse words of string 

def rev_sentence(sentence): 

	# first split the string into words 
	words = sentence.split(' ') 

	# then reverse the split string list and join using space 
	reverse_sentence = ' '.join(reversed(words)) 

	# finally return the joined string 
	return reverse_sentence 

if __name__ == "__main__": 
	input = 'geeks quiz practice code'
	print rev_sentence(input)
