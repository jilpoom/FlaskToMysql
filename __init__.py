from flask import Flask, render_template, request
import mod_dbconn

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/insert')
def insert_info():
    return render_template('insert.html')

@app.route('/login')
def login():
   return render_template('login.html') 

# 여기부터 추가
@app.route('/db')
def select():
    db_class = mod_dbconn.Database()

    sql = "SELECT * FROM test.test_tb"
    row = db_class.executeAll(sql)

    print(row)

    return render_template('db.html', resultData=row[0])



@app.route('/db/insert', methods=['GET', 'POST'])
def insert():
    db_class = mod_dbconn.Database()
    
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        phone = request.form['phone']
        sql= "INSERT INTO test.test_tb VALUES({},{},{},{})".format(id, pw, phone, name)

        db_class.execute(sql)
        db_class.commit()

        return render_template('home.html')
   
    else:
        return "<h1>Fail</h1>"


@app.route('/db/login', methods=['GET', 'POST'])
def update():
    db_class = mod_dbconn.Database()

    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']

        sql = "SELECT * FROM test.test_tb WHERE id = '{}' AND pw = '{}'".format(id, pw)

        row = db_class.executeAll(sql)        
        
        print(row)

        if len(row) != 0:
            return render_template('home.html')
        else:
            return "<h1>LOGIN FAIL<h2>"


# 여기까지 추가



if __name__=='__main__':
    app.run(debug=True)