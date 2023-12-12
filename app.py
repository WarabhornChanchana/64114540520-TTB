from flask import Flask , render_template, request, redirect , url_for

app = Flask(__name__)

courses = [
    {'code' : 'TH001', 'name': 'Thai'},
    {'code' : 'Eng002', 'name': 'English'},
    {'code' : 'IR003', 'name': 'IR'},
]

@app.route('/')
def index():
    return render_template('index.html', courses = courses)

@app.route('/search', methods=['GET','POST']) #B
def search():
    result = None
    
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        result = next((course for course in courses if course['code'] == course_code), None)
        
    return render_template('search.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)