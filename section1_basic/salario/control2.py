# Tela de cálculo de salário líquido, construindo a estrutura

from PyQt5 import uic, QtWidgets #controlar a UI e recurso de tela (widget)

def principal():
    salary = float(form.txtSalary.text())
    discounts = float(form.txtDiscounts.text())
    print(salary)
    print(discounts)
    resultado = salary - discounts
    print(resultado)
    # lblResult --configurando o objeto etiqueta.
    form.lblResult.setText(str(f'{resultado:.2f}'))


# 1 - Declarando as váriáveis de controle da tela
app = QtWidgets.QApplication([])
form = uic.loadUi('./section1_basic/salario/tela.ui')
form.btnCalculate.clicked.connect(principal)    #invocando a função de cálculo de salário


# 2 - Renderizando a tela para os usuários
form.show()
app.exec()