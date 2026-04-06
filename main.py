from flask import flask,render_template
app=flask(__name__)
@app.route('/')
def home():
  @ render_templete automatically looks in the /templetes folder
  return render_template('index.html',title='Home page')
if __name__='__main__':
app.run(host='127.0.0.1',port=8080 ,debug =True)
