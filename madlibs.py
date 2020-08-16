def main():
	# write your code here
	print('Mad lips where lips get mad. \nStart below:')
	time = input('Enter a number from 1 to 12: ')
	items = input('Enter a noun (plural): ')
	name = input('Enter a name: ')
	scream = input('Enter any sentence: ')
	action = input('Enter a verb: ')
	print("\n the story goes...")
	print()
	print('It was %s o\'clock when I heard a knock at the door.' % time)
	print('I opend the door and there was a box full of %s with a note saying "From Mr. %s."' % (items,name.title()))
	print('Just as I closed the door I heard a scream "%s."' % (scream.upper()))
	print('I froze in place and all I could do was %s' % (action))




if __name__ == '__main__':
	main()
