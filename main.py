from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def index():
  name = None
  gender = None
  hobbies = None
  if request.method == 'POST':
      name = request.form['name']
      gender = request.form['gender']
      hobbies = ', '.join(request.form.getlist('hobbies'))
      hobbies_text = ''
      for hobby in hobbies:
        hobbies_text = hobbies_text + '' + hobby
      with open('data.txt', 'a') as file:
        file.write(name + '' + gender + hobbies + '\n')
  return render_template('index.html', name=name, gender=gender, hobbies=hobbies)
  
app.run(host='0.0.0.0', port=81)