from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import mistune

from helpers.filesystem_helper import get_all_files_in_folder
from FileReader import FileReader

class PostRenderer(mistune.Renderer):
	"""docstring for PostRenderer"""
	def __init__(self):
		super(PostRenderer, self).__init__()
		self.highlight_renderer = HighlightRenderer()
		self.markdown = mistune.Markdown(renderer=self.highlight_renderer, escape=False)

	def render_posts_from(self, directory_path):
		markdown_extensions = ['markdown', 'md']
		file_list = get_all_files_in_folder(directory_path, file_extensions=markdown_extensions)

		file_reader = FileReader()
		html_contents = []

		for file_name in file_list:
			markdown_content = file_reader.read_file(directory_path + file_name)
			post_content = self.markdown(markdown_content)
			html_contents.append('<article>{post_content}</article><p class="post-separator">––––––––––––––––––––––––</p>'.format(post_content=post_content))

		complete_html_content = ''.join(html_contents)

		return complete_html_content

class HighlightRenderer(mistune.Renderer):
	def block_code(self, code, lang):
		if not lang:
			return '\n<pre><code>{code}</code></pre>\n'.format(
				code=mistune.escape(code)
			)
		lexer = get_lexer_by_name(lang, stripall=True)
		formatter = HtmlFormatter()
		return highlight(code, lexer, formatter)
