from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_a = StringField('id астронавта', validators=[DataRequired()])
    password_a = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_c = StringField('id капитана', validators=[DataRequired()])
    password_c = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {'title': 'Анкета', 
              'surname': 'Wathy',
              'name': 'Mark',
              'education': 'high',
              'profession': 'климатолог',
              'sex': 'male',
              'motivation': 'I want to break free',
              'ready': True}
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')