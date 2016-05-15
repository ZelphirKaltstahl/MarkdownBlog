from flask import Flask, render_template
import mistune
from FileReader import FileReader
from helpers.filesystem_helper import get_all_files_in_folder

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.j2', title='HEADER')

@app.route('/lf2/blog')
def lf2_blog():
	complete_html_content = render_posts_from('app/static/markdown/lf2/blog/')
	return render_template('lf2_blog.j2', title='LF2 Blog', content=complete_html_content)

@app.route('/lf2/intro')
def lf2_intro():
	complete_html_content = render_posts_from('app/static/markdown/lf2/intro/')
	return render_template('lf2_blog.j2', title='Little Fighter 2', content=complete_html_content)

@app.route('/chinese/blog')
def mandarin_blog():
	complete_html_content = render_posts_from('app/static/markdown/chinese/blog/')
	return render_template('chinese_blog.j2', title='Chinese Blog', content=complete_html_content)

def render_posts_from(directory_path):
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

if __name__ == '__main__':
	app.run(debug=True)
