from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

timeGomogen = 0
timePlato = 0
timePlatoToothUp = 0
timePlatoToothBottom = 0
speed = 0.0
tempGomogen = 0
countTooth = 0
tempPlatoToothUp = 0
tempPlatoToothBottom = 0
tempExtract = 0
tempCrit = 0

Form, Window = uic.loadUiType("GUI.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def click_on_button_calculation():
    timeGomogen = form.timeGomogenEdit.text()
    timePlato = form.timeHoldPlatoEdit.text()
    timePlatoToothUp = form.timePlatoToothUpEdit.text()
    timePlatoToothBottom = form.timePlatoToothBottomEdit.text()
    speed = form.speedDropEdit.text()
    tempGomogen = form.tempGomogenEdit.text()
    countTooth = form.counToothEdit.text()
    tempPlatoToothUp = form.tempPlatoToothUpEdit.text()
    tempPlatoToothBottom = form.tempPlatoToothBottomEdit.text()
    tempExtract = form.tempExtractEdit.text()
    tempCrit = form.tempCritMomentEdit.text()
    print(timeGomogen, timePlato, timePlatoToothUp, timePlatoToothBottom, speed, tempGomogen, countTooth,
          tempPlatoToothUp, tempPlatoToothBottom, tempExtract, tempCrit)
    valid(timeGomogen)
    print('clik')


form.calculationButton.clicked.connect(click_on_button_calculation)
app.exec()


def valid():
    if timeGomogen.isnumeric():
        print('OK')
    else:
        print("Bad")

