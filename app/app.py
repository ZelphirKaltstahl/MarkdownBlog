from flask import Flask, render_template
from PostRenderer import PostRenderer
import os

app = Flask(__name__)
post_renderer = PostRenderer()

current_file_directory = os.path.dirname(__file__)

def static_file_path(relative_path):
	return os.path.join(current_file_directory, relative_path)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.j2', title='HEADER')

@app.route('/lf2/blog')
def lf2_blog():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/lf2/blog/')
	)
	return render_template(
		'lf2_blog.j2', title='LF2 Blog', content=complete_html_content
	)

@app.route('/lf2/intro')
def lf2_intro():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/lf2/intro/')
	)
	return render_template(
		'lf2_blog.j2', title='Little Fighter 2', content=complete_html_content
	)

@app.route('/chinese/blog')
def mandarin_blog():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/chinese/blog/')
	)
	return render_template(
		'chinese_blog.j2', title='Chinese Blog', content=complete_html_content
	)

@app.route('/coding/blog')
def coding_blog():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/coding/blog/')
	)
	return render_template(
		'coding_blog.j2', title='Coding Blog', content=complete_html_content
	)

@app.route('/coding/resources')
def coding_resources():
	return render_template(
		'coding_resources.j2', title='Coding Resources', content='Coding Resources (no resources here yet :)'
	)

if __name__ == '__main__':
	app.run(debug=True)
