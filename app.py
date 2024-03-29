from flask import Flask, render_template, request, redirect, url_for
from equipment import result
from classes import unit_classes
from unit import PlayerUnit, EnemyUnit
from base import Arena

app = Flask(__name__)

heroes = {
    "player": None,
    "enemy": None
} # этот словарь самый главный в него я помещаю все что ввожу
#
arena = Arena()  # TODO инициализируем класс арены


@app.route("/")
def menu_page():
    return render_template('index.html')


@app.route("/fight/", methods=['GET', 'POST'])
def start_fight():
    # TODO выполняем функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    # TODO рендерим экран боя (шаблон fight.html)
    if request.method == 'GET':
        arena.start_game(heroes['player'], heroes['enemy'])
        return render_template('fight.html', heroes=arena)



@app.route("/fight/hit")
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
    # weapon1 = result['weapons']["топорик"]
    # armor1 = result['armors']["кожаная броня"]
    # weapon = result['weapons']["ножик"]
    # armor = result['armors']["панцирь"]
    # heroes['player'] = PlayerUnit("Игрок 1", unit_classes["Воин"], weapon1, armor1)
    # heroes['enemy'] = EnemyUnit("Игрок 2", unit_classes["Вор"], weapon, armor)
    # arena.start_game(heroes['player'], heroes['enemy'])

    r = arena.player_hit()

    arena._stamina_regeneration()
    print(r)
    return render_template('fight.html', heroes=arena, result=r[0], battle_result=r[1])


@app.route("/fight/use-skill")
def use_skill():
    # TODO кнопка использования скилла
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    r = arena.player_use_skill()
    arena._stamina_regeneration()
    return render_template('fight.html', heroes=arena, result=r[0], battle_result=r[1])


@app.route("/fight/pass-turn")
def pass_turn():
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
    r = arena.next_turn()
    return render_template('fight.html', heroes=arena, battle_result=r)


@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    arena._end_game()
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    # TODO кнопка выбор героя. 2 метода GET и POST
    # TODO на GET отрисовываем форму.
    # TODO на POST отправляем форму и делаем редирект на эндпоинт choose enemy
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=result, u_classes=unit_classes)
    if request.method == 'POST':
        name = request.form['name']
        unit_class = request.form['unit_class']
        weapon = result['weapons'][request.form['weapon']]
        armor = result['armors'][request.form['armor']]
        heroes['player'] = PlayerUnit(name, unit_classes[unit_class], weapon, armor)
        return redirect(url_for('choose_enemy'))


@app.route("/choose_enemy", methods=['post', 'get'])
def choose_enemy():
    # TODO кнопка выбор соперников. 2 метода GET и POST
    # TODO также на GET отрисовываем форму.
    # TODO а на POST отправляем форму и делаем редирект на начало битвы
    if request.method == 'GET':
        return render_template('enemy_choosing.html', result=result, u_classes=unit_classes)
    if request.method == 'POST':
        name = request.form['name']
        unit_class = request.form['unit_class']
        weapon = result['weapons'][request.form['weapon']]
        armor = result['armors'][request.form['armor']]
        heroes['enemy'] = EnemyUnit(name, unit_classes[unit_class], weapon, armor)
        arena.start_game(heroes['player'], heroes['enemy'])
        return redirect(url_for('start_fight'))

if __name__ == "__main__":
    app.run()
