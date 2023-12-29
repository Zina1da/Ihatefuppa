from flask import Flask, render_template, request

app = Flask(__name__)
no_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    global no_count
    print("Form Data:", request.form)
    answer = request.form.get('answer')
    if answer == 'yes':
        return render_template('response.html', message='YEEAAAAAYYYY')
    elif answer == 'no':
        no_count += 1
        if no_count >= 8:
            return render_template('response.html', message='иди нахуй', show_gif=True)
    else:
        return 'Что-то пошло не так.'

@app.route('/new-page')
def new_page():
    return render_template('new_page.html')

if __name__ == '__main__':
    app.run(debug=True)
