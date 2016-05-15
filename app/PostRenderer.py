from helpers.filesystem_helper import get_all_files_in_folder
import mistune
from FileReader import FileReader

class PostRenderer:
	"""docstring for PostRenderer"""
	def __init__(self):
		super(PostRenderer, self).__init__()

	def render_posts_from(self, directory_path):
		markdown_extensions = ['markdown', 'md']
		file_list = get_all_files_in_folder(directory_path, file_extensions=markdown_extensions)

		file_reader = FileReader()
		html_contents = []

		for file_name in file_list:
			markdown_content = file_reader.read_file(directory_path + file_name)
			post_content = mistune.markdown(markdown_content, escape=False)
			html_contents.append('<article>{post_content}</article><p class="post-separator">––––––––––––––––––––––––</p>'.format(post_content=post_content))

		complete_html_content = ''.join(html_contents)

		return complete_html_content
