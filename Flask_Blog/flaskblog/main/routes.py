from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route('/')  #route decorators; routes are what we type in browsers to go to diff pages
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html',posts=posts, title='Blog 1')


@main.route('/about')  #route decorators; routes are what we type in browsers to go to diff pages
def about():
    return render_template('about.html')
