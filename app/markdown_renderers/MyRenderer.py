import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
from markdown_renderers.HanziSubRenderer import HanziSubRenderer

class HanziRenderer(mistune.Renderer):
	def block_code(self, code, lang):
		if not lang:
			return '\n<pre><code>{escaped_code}</code></pre>\n'.format(escaped_code=mistune.escape(code))
		
		elif lang == 'hanzi':
			hanzi_processor = HanziSubRenderer()
			code = hanzi_processor.render(code)
			return '\n<pre><code class="lang-hanzi">{content}</code></pre>\n'.format(content=code)

		else:
			lexer = get_lexer_by_name(lang, stripall=True)
			formatter = html.HtmlFormatter()
			return highlight(code, lexer, formatter)


# Usage:
# renderer = HighlightRenderer()
# markdown = mistune.Markdown(renderer=renderer)
# print(markdown('```python\nassert 1 == 1\n```'))