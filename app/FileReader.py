class FileReader:
	"""docstring for FileReader"""
	def __init__(self):
		super(FileReader, self).__init__()
	
	def read_file(self, file_path):
		with open(file_path) as opened_file:
			return opened_file.read()
		