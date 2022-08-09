from flask import Flask, render_template
import mod_dbconn

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# 여기부터 추가
@app.route('/db')
def select():
    db_class = mod_dbconn.Database()

    sql = "SELECT * FROM test.test_tb"
    row = db_class.executeAll(sql)

    print(row)

    return render_template('db.html', resultData=row[0])

# 여기까지 추가



if __name__=='__main__':
    app.run(debug=True)