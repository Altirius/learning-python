import json

FILE_NAME = 'phones.json'

def mainLoop():
	contacts = loadData()
	key = 0

	while key != 5:
		printMainMenu()
		key = inputActionKey()

		if key == 1:
			printContacts(contacts)
		elif key == 2:
			handleSearch(contacts)
		elif key == 3:
			contacts.append(inputContact())

def loadData():
	with open(FILE_NAME, 'r', encoding='utf-8') as f:
		return json.load(f)
	
	
def printMainMenu():
	print('Вывести весь список (1) | Поиск по строке (2) | Добавить контакт (3) | Удалить контакт (4) | Выйти (5)')

def inputActionKey():
	return int(input('Введите числовой идентификатор желаемого действия: '))

def writeData(data):
	with open(FILE_NAME, 'w', encoding='utf-8') as f:
		f.write(json.dumps(data, ensure_ascii=False))

def printContacts(contacts):
	if isContactsEmpty(contacts):
		printEmptyContactsMessage()

	for contact in contacts:
		printContact(contact)

def isContactsEmpty(contacts):
	return len(contacts) == 0

def printEmptyContactsMessage():
	print('Записей не найдено')

def printContact(contact):
	print(
		'Имя: ', contact.get('firstName'), ' | ',
		'Фамилия: ', contact.get('lastName'), ' | ',
		'Номер телефона: ', contact.get('phoneNumber')
	)

def handleSearch(contacts):
	return printContacts(filterContactsBySearchString(contacts, inputSearchString()))
		
def inputSearchString():
	return input('Введите строку для поиска: ')

def filterContactsBySearchString(contacts, searchString):
	result = []
	for contact in contacts:
		if isSearchStringInContact(searchString, contact):
			result.append(contact)
	return result

def isSearchStringInContact(searchString, contact):
	return (
		searchString in contact.get('firstName') or
		searchString in contact.get('lastName') or
		searchString in contact.get('phoneNumber')
	)

def inputContact():
	return {
		"firstName": input('Введите имя: '),
		"lastName": input('Введите фамилию: '),
		"phoneNumber": input('Введите номер телефона: ')
	}

	


mainLoop()