import os

def get_all_files_in_folder(file_path, file_extensions=None):
	"""
	This function returns all files in a given directory.
	If file_extension is specified, only files with that file extension will be returned.
	"""
	if not file_extensions:
		return [file for file in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, file))]
	else:
		file_names = []

		for item in os.listdir(file_path):
			if os.path.isfile(os.path.join(file_path, item)):
				file_name_no_ext, file_extension = os.path.splitext(item)
				# print('FILE EXTENSION FOUND:', file_extension)
				if file_extension[1:] in file_extensions:
					file_names.append(item)
		return sorted(file_names, reverse=True)
