from flask import Flask, render_template
from PostRenderer import PostRenderer

app = Flask(__name__)
post_renderer = PostRenderer()

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.j2', title='HEADER')

@app.route('/lf2/blog')
def lf2_blog():
	complete_html_content = post_renderer.render_posts_from('app/static/markdown/lf2/blog/')
	return render_template('lf2_blog.j2', title='LF2 Blog', content=complete_html_content)

@app.route('/lf2/intro')
def lf2_intro():
	complete_html_content = post_renderer.render_posts_from('app/static/markdown/lf2/intro/')
	return render_template('lf2_blog.j2', title='Little Fighter 2', content=complete_html_content)

@app.route('/chinese/blog')
def mandarin_blog():
	complete_html_content = post_renderer.render_posts_from('app/static/markdown/chinese/blog/')
	return render_template('chinese_blog.j2', title='Chinese Blog', content=complete_html_content)

if __name__ == '__main__':
	app.run(debug=True)
