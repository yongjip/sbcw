from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'

db = SQLAlchemy(app)

class Post(db.Model):
   __tablename__ = 'posts'
   id = db.Column(db.Integer, primary_key=True)
   subject = db.Column(db.String)
   body = db.Column(db.String)


@app.route('/')
def index():
   context = {'title': 'this is a title from context',
               'body': 'This is a body from body'}
   return render_template('index.html', **context)

@app.route('/test')
def test():
   return 'test'

@app.route('/posts', methods=['POST'])
def new_post():
   subject = request.form['subject']
   body = request.form['body']

   post = Post(
       subject=subject,
       body=body
   )
   db.session.add(post)
   db.session.commit()
   return f'{subject}, {body}'

if __name__=='__main__':
   app.run(port=8000, debug=True)
   # db.create_all()


"""
curl -i -XPOST --data "subject=Test&body=body1234" localhost:8000/posts

sqlite3 webapp.db
select * from posts;

"""