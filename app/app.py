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
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/home/')
	)
	return render_template('index.j2', title='Zelphir\'s Blog', content=complete_html_content)

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

@app.route('/lf2/tools')
def lf2_tools():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/lf2/tools/')
	)
	return render_template(
		'lf2_blog.j2', title='Little Fighter 2 Tools', content=complete_html_content
	)

@app.route('/lf2/recordings')
def lf2_recordings():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/lf2/recordings/')
	)
	return render_template(
		'lf2_blog.j2', title='Little Fighter 2 Recordings', content=complete_html_content
	)

@app.route('/lf2/resources')
def lf2_resources():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/lf2/resources/')
	)
	return render_template(
		'lf2_blog.j2', title='Little Fighter 2 Resources', content=complete_html_content
	)

@app.route('/chinese/blog')
def chinese_blog():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/chinese/blog/')
	)
	return render_template(
		'chinese_blog.j2', title='Chinese Blog', content=complete_html_content
	)

@app.route('/chinese/hanzi')
def chinese_hanzi():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/chinese/hanzi/')
	)
	return render_template(
		'chinese_hanzi.j2', title='Hanzi', content=complete_html_content
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
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/coding/resources/')
	)
	return render_template(
		'coding_blog.j2', title='Coding Blog', content=complete_html_content
	)

@app.route('/about')
def about():
	complete_html_content = post_renderer.render_posts_from(
		static_file_path('static/markdown/about/')
	)
	return render_template(
		'about.j2', title='About', content=complete_html_content
	)

if __name__ == '__main__':
	app.run(debug=True)
