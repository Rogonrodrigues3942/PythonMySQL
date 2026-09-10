# Tela de cálculo de salário líquido, construindo a estrutura

from PyQt5 import uic, QtWidgets

def principal():
    salary = float(form.txtSalary.text())
    discounts = float(form.txtDiscounts.text())
    print(salary)
    print(discounts)
    resultado = salary - discounts
    print(resultado)


# 1 - Declarando as váriáveis de controle da tela
app = QtWidgets.QApplication([])
form = uic.loadUi('./section1_basic/salario/tela.ui')
form.btnCalculate.clicked.connect(principal)

# 2 - Renderizando a tela para os usuários
form.show()
app.exec()