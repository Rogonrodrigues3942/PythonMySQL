# Screen control script: 10/09/2026.
from PyQt5 import uic, QtWidgets

#*declarando a function principal,
def principal():
    salary = float( formulario.txtSalary.text())
    discounts = float(formulario.txtDiscounts.text())
    print(f'salario: {salary:.2f}')
    print(f'desconto: {discounts:.2f}')
    result = salary - discounts
    print(f'resultado: {result:.2f}')
    formulario.lblResult.setText(str(f'{result:.2f}'))



#*1 - criando variáveis de controle de tela
app = QtWidgets.QApplication([])    #^Cria o objeto responsável por gerenciar a aplicação gráfica.

# formulario = uic.loadUi('./section1_basic/salario2/tela2.ui') #^ permite acessar os componentes da tela.
formulario = uic.loadUi('./tela2.ui') #^Carrega a interface gráfica.
formulario.btnCalculate.clicked.connect(principal) #^ Botão acionado por clique e invocar a def principal().


#* 2 - renderizando a tela ##  Exibi a interface
formulario.show()

#* Executando a aplicação. Permitindo a interação do usuário.
app.exec()