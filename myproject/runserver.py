from  myapp import app

@app.route('/')
def hello_world():
    return '123'

if __name__ == '__main__':
    app.run('0.0.0.0')
