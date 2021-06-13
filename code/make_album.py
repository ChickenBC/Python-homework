def make_album(singer, album, number = ''):
	albums = {'singer': singer, 'album': album}
	if number:
		albums['number'] = number
	return albums

while True:
	print("\nEnter your favorite singer, his/her album and the number of songs.")
	print("Enter 'q' to quit.")

	singer = input("Enter singer:")
	if singer == 'q':
		break

	album = input("Enter album:")
	if album == 'q':
		break

	number = input("Enter number:")
	if number == 'q':
		break

	albums = make_album(singer, album, number)
	print(albums)