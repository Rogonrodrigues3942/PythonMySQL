from PyQt5 import uic, QtWidgets #controlar a UI e recurso de tela (widget)

#! Tela de cálculo de salário líquido, construindo a estrutura

def principal():
    salary = float(form.txtSalary.text())
    discounts = float(form.txtDiscounts.text())
    print(salary)
    print(discounts)
    resultado = salary - (salary * (discounts / 100))
    print(resultado)
    monthlyFgts = salary / 100 * 8
    annualFgts = salary / 100 * 8 * 12

    #^lblResult --configurando o objeto etiqueta.
    form.lblResult.setText(str(f'{resultado:.2f}'))
    form.lblResultMonthlyFgts.setText(str(f'{monthlyFgts:.2f}'))
    form.lblResultAnnualFgts.setText(str(f'{annualFgts:.2f}'))


#*  1 - Declarando as váriáveis de controle da tela
app = QtWidgets.QApplication([])
form = uic.loadUi('./section1_basic/salario/tela.ui')
form.btnCalculate.clicked.connect(principal)    #TODO: invocando a função de cálculo de salário


#* 2 - Renderizando a tela para os usuários
form.show()
app.exec()