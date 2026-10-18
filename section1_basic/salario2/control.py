# Screen control script: 10/09/2026.
from PyQt5 import uic, QtWidgets

#declarando a function principal,
def principal():
    salary = float( formulario.txtSalary.text())
    discounts = float(formulario.txtDiscounts.text())
    print(f'salario: {salary:.2f}')
    print(f'desconto: {discounts:.2f}')


# 1 - criando variáveis de controle de tela
app = QtWidgets.QApplication([])
# formulario = uic.loadUi('./section1_basic/salario2/tela2.ui')
formulario = uic.loadUi('./tela2.ui')
formulario.btnCalculate.clicked.connect(principal)


# 2 - renderizando a tela
formulario.show()
app.exec()