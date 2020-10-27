from PyQt5 import QtWidgets, uic



app = QtWidgets.QApplication([])
call = uic.loadUi("GUI.ui")

call.show()
app.exec()

