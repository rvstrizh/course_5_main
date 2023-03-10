from flask import Flask, render_template, request, redirect, url_for
from equipment import Equipment
from classes import unit_classes
app = Flask(__name__)

# heroes = {
#     "player": BaseUnit,
#     "enemy": BaseUnit
# }
#
# arena =  ... # TODO инициализируем класс арены


@app.route("/")
def menu_page():
    return render_template('index.html')


@app.route("/fight/")
def start_fight():
    # TODO выполняем функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    # TODO рендерим экран боя (шаблон fight.html)

    return render_template('fight.html')

#
# @app.route("/fight/hit")
# def hit():
#     # TODO кнопка нанесения удара
#     # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
#     # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
#     # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
#     pass
#
#
# @app.route("/fight/use-skill")
# def use_skill():
#     # TODO кнопка использования скилла
#     # TODO логика пркатикчески идентична предыдущему эндпоинту
#     pass
#
#
# @app.route("/fight/pass-turn")
# def pass_turn():
#     # TODO кнопка пропус хода
#     # TODO логика пркатикчески идентична предыдущему эндпоинту
#     # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
#     pass
#
#
# @app.route("/fight/end-fight")
# def end_fight():
#     # TODO кнопка завершить игру - переход в главное меню
#     return render_template("index.html", heroes=heroes)
#
#
@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    # TODO кнопка выбор героя. 2 метода GET и POST
    # TODO на GET отрисовываем форму.
    # TODO на POST отправляем форму и делаем редирект на эндпоинт choose enemy
    if request.method == 'GET':
        result = Equipment()._get_equipment_data()
        u_classes = unit_classes
        # print(type(u_classes['Вор']))
        # print(u_classes['Вор'])
        return render_template('hero_choosing.html', result=result, unit_classes=u_classes)
    if request.method == 'POST':
        print(request.form['unit_class'])
        print(request.form['weapon'])

        return redirect(url_for('choose_enemy'))


@app.route("/choose_enemy", methods=['post', 'get'])
def choose_enemy():
    # TODO кнопка выбор соперников. 2 метода GET и POST
    # TODO также на GET отрисовываем форму.
    # TODO а на POST отправляем форму и делаем редирект на начало битвы
    if request.method == 'GET':
        result = Equipment()._get_equipment_data()
        classes = unit_classes
        return render_template('enemy_choosing.html', result=result, classes=classes)
    if request.method == 'POST':

        return redirect(url_for('start_fight'))

if __name__ == "__main__":
    app.run()
