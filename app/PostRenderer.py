import re

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import mistune
from mistune import Renderer, InlineGrammar, InlineLexer, BlockGrammar, BlockLexer

from helpers.filesystem_helper import get_all_files_in_folder
from FileReader import FileReader

class PostRenderer:
	def __init__(self):
		super(PostRenderer, self).__init__()
		self.highlight_renderer = HighlightRenderer()
		self.meta_data_inline_lexer = MetaDataInlineLexer(self.highlight_renderer)  # the lexer needs to know the renderer to call its meta_data function
		self.meta_data_inline_lexer.enable_meta_data()  # don't forget to enable it!
		self.markdown = mistune.Markdown(
			renderer=self.highlight_renderer,
			inline=self.meta_data_inline_lexer,
			escape=False
		)

	def render_posts_from(self, directory_path):
		markdown_extensions = ['markdown', 'md', 'mdown']
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
		formatter = HtmlFormatter(
			linenos='table',
			linenospecial=4,
			lineseparator='<br>',
			lineanchors='code-line-link',
			linespans='code-line-span',
			anchorlinenos='lineno-line'
		)
		return highlight(code, lexer, formatter)

	def meta_data(self, attribute, value):
		if attribute.lower() == 'title':
			return '<h1 class="post-title">{title}</h1>'.format(title=value)
		elif attribute.lower() == 'author':
			return '<p class="post-author"><em>Author: {author}</em></p>'.format(author=value)
		elif attribute.lower() == 'date':
			return '<p class="post-date"><em>Date: {date}</em></p>'.format(date=value)
		else:
			return '<p class="post-meta-data"><em>{attribute}: {value}</em></p>'.format(attribute=attribute, value=value)

class MetaDataInlineLexer(InlineLexer):
	def enable_meta_data(self):
		self.rules.meta_data = re.compile(
			r'(%\s*)'
			r'(?P<attribute>.*)'
			r'(\s*:\s*)'
			r'(?P<value>.*)'
			r'(\s*)'
		)
		self.default_rules.insert(3, 'meta_data')

	def output_meta_data(self, match):
		match_dict = match.groupdict()
		attribute = match_dict['attribute']
		value = match_dict['value']
		print('FOUND ATTRIBUTE:', attribute)
		print('FOUND VALUE:', value)
		return self.renderer.meta_data(attribute, value)
