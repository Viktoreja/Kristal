from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import datetime as dt


DATABASE = {
    'timeGomogen': 24,
    'timePlato': 0,
    'timePlatoToothUp': 12,
    'timePlatoToothBottom': 2,
    'speed': 0.21,
    'tempGomogen': 0.0,
    'countTooth': 1,
    'tempPlatoToothUp': 0,
    'tempPlatoToothBottom': 0,
    'tempExtract': 780,
    'tempCrit': 810,
    'timeCrit': 0,
    'timeExtract': 0
}


def calculation():

    time_at_start = dt.datetime.utcnow() + dt.timedelta(hours=3)
    houre = int(DATABASE['timePlato'] + DATABASE['timeGomogen'] +
               (DATABASE['timePlatoToothUp'] + DATABASE['timePlatoToothBottom']) * DATABASE['countTooth'])
    DATABASE['timeCrit'] = time_at_start + dt.timedelta(hours=houre)
    houre += (DATABASE['tempCrit'] - DATABASE['tempExtract']) / DATABASE['speed']
    DATABASE['timeExtract'] = time_at_start + dt.timedelta(hours=houre)


# ----------------------------------------------------------------------------------------------------------------------
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def coma_to_dot(in_str):
    out_str = ''
    for char in in_str:
        if char == ',':
            out_str += '.'
        else:
            out_str += char
    return out_str


# ----------------------------------------------------------------------------------------------------------------------
def check_data():
    for key in DATABASE:
        value = DATABASE[key]
        if isinstance(value, str):
            value = coma_to_dot(value)
            if is_float(value):
                if key == 'speed':
                    value = float(value)/60
                else:
                    value = float(value)
            else:
                return 1
        else:
            return 2
        DATABASE[key] = value


# ----------------------------------------------------------------------------------------------------------------------
def get_data(form):
    DATABASE['timeGomogen'] = form.timeGomogenEdit.text()
    DATABASE['timePlato'] = form.timeHoldPlatoEdit.text()
    DATABASE['timePlatoToothUp'] = form.timePlatoToothUpEdit.text()
    DATABASE['timePlatoToothBottom'] = form.timePlatoToothBottomEdit.text()
    DATABASE['speed'] = form.speedDropEdit.text()
    DATABASE['tempGomogen'] = form.tempGomogenEdit.text()
    DATABASE['countTooth'] = form.counToothEdit.text()
    DATABASE['tempPlatoToothUp'] = form.tempPlatoToothUpEdit.text()
    DATABASE['tempPlatoToothBottom'] = form.tempPlatoToothBottomEdit.text()
    DATABASE['tempExtract'] = form.tempExtractEdit.text()
    DATABASE['tempCrit'] = form.tempCritMomentEdit.text()


# ----------------------------------------------------------------------------------------------------------------------
def click_on_button_calculation():
    get_data(form)
    check = check_data()
    if check == 1:
        print('Введено не число!')
    elif check == 2:
        print('Ошибка ввода!')
    else:
        print(DATABASE.values())
    print('clik')


# ----------------------------------------------------------------------------------------------------------------------
Form, Window = uic.loadUiType("GUI.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.calculationButton.clicked.connect(click_on_button_calculation)

app.exec()
# ----------------------------------------------------------------------------------------------------------------------
