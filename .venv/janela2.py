# Importar os controles (QtWidgets) para a biblioteca gráfica PyQt5.
# Neste exemplo estamos utilizando o comando import com a opção
# asterisco (*) quem importa todos os controles da biblioteca
from PyQt5.QtWidgets import *
# Importação da biblioteca de sistema para abrir e fechar a janela que será construída.
# Ao fechar a janela, também estaremos retirando-a da memória
import sys

# Criação da estrutura geral da nossa janela.
# A janela e seus controles estão sendo criados de forma agrupada dentro de uma classe.
# A classe Janela2 está herdando todas as configurações estruturais de uma tela normal
# classe Qwidget. Esta classe define os botões: minimizar, maximizar e fechar.
# Além de apresentar um título para a janela.
class Janela2(QWidget):
    # O comando def(definition->definição) define uma função. Neste caso, estamos definindo
    # a função de inicialização da classe init(__init__). Esta função realiza o start (coloca para
    # funcionar) a classe Janela2. Na função __init__ passamos como parâmetro o comando self que
    # indica a classe que teremos controles que devem ser usados por ela. Portanto, todo controle
    # que está com o prefixo self, faz referência à própria classe. Ex.: self.label_nome = QLabel :
    # isso indica que a Label pertence à classe Janela2, assim como os demais controles(label, 
    # line edit, setlayout).
    def __init__(self):
        super().__init__()
        # Adicionar um texto do título da janela
        self.setWindowTitle("Janela de cadastro")

        # Configurar tamanho e posição
        # O primeiro valor é a posição x medida em pixel
        # O segundo valor é a posição y medida em pixel
        # O terceiro valor é a largura (width) medida em pixel
        # O quarto valor é a altura (height) medida em pixel
        self.setGeometry(50,200,500,200)

        # Adicionar uma label à janela
        # Uma label (rótulo) é um texto que é apresentado em uma janela para indicar o que deve ser
        # feito à frente (geralmente uma caixa de texto). No exemplo abaixo, estamos criando uma label para
        # apresentar o texto "Nome Completo", isso indica ao usuário que ele deve escrever o nome em uma
        # caixa de texto à frente. Geralmente, uma label é usada em combinação com uma caixa de texto (QLineEdit).
        self.label_nome = QLabel("Nome completo:")
        # Para alterar o estilo do texto da label, usamos os 
        # comando de CSS (Cascade Style Sheet(Folha de estilo em cascata))
        # com as propriedades:
        # - color -> cor da letra (cor da fonte)
        # - font size -> tamanho da letra. Que pode ser medida em pt(pontos)
        # - font-weight -> peso da fonte (Negrito: bold)
        # - text-transform -> alterar a altura da caixa de texto(letra):
        # Uppercase -> Maiúscula
        # Lower case -> Minúscula
        # Captalize -> Primeira letra de cada palavra Maiúscula.
        self.label_nome.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")

        self.label_email = QLabel("E-mail:")
        self.label_email.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")

        self.label_cpf = QLabel("CPF:")
        self.label_cpf.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")

        self.label_sexo = QLabel("Sexo:")
        self.label_sexo.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")
        
        self.label_idade = QLabel("Idade:")
        self.label_idade.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")

        # Adicionar uma caixa de texto
        self.edit_nome = QLineEdit()
        # Aplicação do estilo para a caixa de texto:
        # background-color -> cor de fundo
        # padding -> margem interna, ou seja, dentro da caixa
        # border-radius -> arredondar as bordas da caixa de texto
        self.edit_nome.setStyleSheet("QLineEdit{background-color:#999; color:#000; padding:10px; border-radius:10px}")


        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("QLineEdit{background-color:#999; color:#000; padding:10px; border-radius:10px}")
        self.edit_cpf = QLineEdit()
        self.edit_cpf.setStyleSheet("QLineEdit{background-color:#999; color:#000; padding:10px; border-radius:10px}")

        # Adicionar combobox
        self.combo_sexo = QComboBox()
        self.combo_sexo.setStyleSheet("QComboBox{background-color:#999; color:#000; padding:10px; border-radius:10px}")

        self.combo_idade = QComboBox()
        self.combo_idade.setStyleSheet("QComboBox{background-color:#999; color:#000; padding:10px; border-radius:10px}")


        # Criar uma lista com 3 sexos
        lst_sexo = ["Masculino", "Feminino","Outros"]
        # Adicionar a lista a combo_sexo
        self.combo_sexo.addItems(lst_sexo)

        # Criar uma lista para o combo_idade que vai de 16 a 100 anos
        lst_idade = []
        # Para popular a caixa(combobox) da idade com valores de 16 até 100, estamos usando uma estrutura de repetição
        # que faz uma contagem de 16 a 101 com o comando "range". Durante a contagem, cada número é convertido para 
        # string, pois a combobox só aceita lista de valores em formato de texto (string)
        for i in range(16,101):
            lst_idade.append(str(i))
        self.combo_idade.addItems(lst_idade)

        # Adicionar layout para organizar os elementos
        # Estamos usando o gerenciador de layout vertical (QVBoxLayout)
        # Ele é utilizado para organizar os controles que irão aparecer na Janela2.
        # O QVBoxLayout foi utilizado para dispor os controles um abaixo do outro. Para exibir um ao lado do outro,
        # usamos o comando QHBoxLayout.
        layout = QVBoxLayout()

        # Para adicionar a label_nome e o edit_nome ao organizador (layout) vertical, usamos o comando
        # add (adicionar) Widget(controle). Assim os controles irão aparecer um abaixo do outro, pois este organizador
        # é do tipo vertical.
        layout.addWidget(self.label_nome)
        layout.addWidget(self.edit_nome)

        layout.addWidget(self.label_email)
        layout.addWidget(self.edit_email)

        layout.addWidget(self.label_cpf)
        layout.addWidget(self.edit_cpf)

        layout.addWidget(self.label_sexo)
        layout.addWidget(self.combo_sexo)

        layout.addWidget(self.label_idade)
        layout.addWidget(self.combo_idade)

        # Adicionar o layout à tela
        self.setLayout(layout)

# Criando um objeto chamado app do QApplication (Responsável por todo o comportamento da nossa aplicação). 
# O argumento sys.argv: informa ao sistema operacional que uma aplicação será carregada e estará presente em memória.
app = QApplication(sys.argv)
# Inicia a tela, ou seja, carrega a janela em memória.
jan = Janela2()
# Exibe a janela em tela.
jan.show()
# O comando app.exec_, executa todos os comandos acima e gerecia o botão de fechar para retirar a janela de memória quando for acionado.
app.exec_()