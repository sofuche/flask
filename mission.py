from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренировка', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    lst = ['инженер-исследователь',
           'пилот',
           'строитель',
           'экзобиолог',
           'врач',
           'инженер по терраформированию',
           'климатолог',
           'специалист по радиационной защите',
           'астрогеолог',
           'гляциолог',
           'инженер жизнеобеспечения',
           'метеоролог',
           'оператор марсохода',
           'киберинженер',
           'штурман']
    return render_template('list.html', title='Список профессий', list=list, lst=lst)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')