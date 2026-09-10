# Screen control script: 10/09/2026.
from PyQt5 import uic, QtWidgets

# 1 - criando variáveis de controle de tela
app = QtWidgets.QApplication([])
formulario = uic.loadUi('./section1_basic/salario/tela.ui')

# 2 - renderizando a tela
formulario.show()
app.exec()