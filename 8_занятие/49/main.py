import json

FILE_NAME = 'phones.json'

SHOW_LIST_KEY = 1
SEARCH_CONTACT_KEY = 2
ADD_CONTACT_KEY = 3
DELETE_CONTACT_KEY = 4
UPDATE_CONTACT_KEY = 5
SAVE_LIST_KEY = 6
QUIT_KEY = 7

class ContactsDirectory(object):
	def __init__(self, fileName):
		self.fileName = fileName

	def mainLoop(self):
		self.contacts = self.loadData()
		key = 0

		while key != QUIT_KEY:
			self.printMainMenu()
			key = self.inputActionKey()

			if key == SHOW_LIST_KEY:
				self.printContacts(self.contacts)
			elif key == SEARCH_CONTACT_KEY:
				self.handleSearch()
			elif key == ADD_CONTACT_KEY:
				self.handleAddContact()
			elif key == DELETE_CONTACT_KEY:
				self.handleDelete()
			elif key == UPDATE_CONTACT_KEY:
				self.handleUpdate()
			elif key == SAVE_LIST_KEY:
				self.writeData()

	def loadData(self):
		with open(self.fileName, 'r', encoding='utf-8') as f:
			return json.load(f)
	
	def writeData(self):
		with open(self.fileName, 'w', encoding='utf-8') as f:
			f.write(json.dumps(self.contacts, ensure_ascii=False))

	def printMainMenu(self):
		
		print(
			'Вывести весь список (' + str(SHOW_LIST_KEY) + ') |',
			'Поиск (' + str(SEARCH_CONTACT_KEY) + ') |',
			'Добавить (' + str(ADD_CONTACT_KEY) + ') |',
			'Удалить (' + str(DELETE_CONTACT_KEY) + ') |',
			'Обновить (' + str(UPDATE_CONTACT_KEY) + ') |',
			'Сохранить(' + str(SAVE_LIST_KEY) + ') |',
			'Выйти(' + str(QUIT_KEY) + ')'
		)

	def inputActionKey(self):
		return int(input('Введите числовой идентификатор желаемого действия: '))

	def printContacts(self, contacts):
		if self.isContactsEmpty():
			self.printEmptyContactsMessage()

		for index, contact in enumerate(contacts):
			self.printIndexedContact(index, contact)

	def isContactsEmpty(self):
		return len(self.contacts) == 0

	def printEmptyContactsMessage(self):
		print('Записей не найдено')

	def printIndexedContact(self, index, contact):
		print(
			index, ' | '
			'Имя: ', contact.get('firstName'), ' | ',
			'Фамилия: ', contact.get('lastName'), ' | ',
			'Номер телефона: ', contact.get('phoneNumber')
		)

	def handleSearch(self):
		return self.printContacts(self.filterContactsBySearchString(self.inputSearchString()))
			
	def inputSearchString(self):
		return input('Введите строку для поиска: ')

	def filterContactsBySearchString(self, searchString):
		result = []
		for contact in self.contacts:
			if self.isSearchStringInContact(searchString, contact):
				result.append(contact)
		return result

	def isSearchStringInContact(self, searchString, contact):
		return (
			searchString in contact.get('firstName') or
			searchString in contact.get('lastName') or
			searchString in contact.get('phoneNumber')
		)

	def handleAddContact(self):
		self.contacts.append({
			"firstName": input('Введите имя: '),
			"lastName": input('Введите фамилию: '),
			"phoneNumber": input('Введите номер телефона: ')
		})

	def handleDelete(self):
		position = int(input('Введите порядковый номер записи которую хотите удалить: '))
		self.printIndexedContact(position, self.contacts[position])
		self.contacts.pop(position)
	
	def handleUpdate(self):
		position = int(input('Введите порядковый номер записи которую хотите обновить: '))
		self.printIndexedContact(position, self.contacts[position])
		self.contacts[position] = ({
			"firstName": input('Введите имя: '),
			"lastName": input('Введите фамилию: '),
			"phoneNumber": input('Введите номер телефона: ')
		})


dictionary = ContactsDirectory(FILE_NAME)
dictionary.mainLoop()