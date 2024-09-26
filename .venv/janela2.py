# Importar os controles(QtWidgets) para biblioteca gráfica
# Pyqt5. Neste exemplo estamos utilizandoo comando import
# com a opção asterisco(*) que importa todos os controles
# da biblioteca
from PyQt5.QtWidgets import *
# A importação da biblioteca de sistema para abrir e fechar a
# janela que será construida. Ao fechar a janela, também
# estaremos retirando-a da memória
import sys

# Criação da estrutura geral da nossa janela.
# A janela e seus controles estão sendo
# criadas de forma agrupada dentro de uma classe.
# A classe a Janela2 está herdando todas as 
# configurações estruturais de uma tela normal
# classeQwiget. Esta classe define os botões:^
# minimizar, e fechar. Além de apresentar um título para a janela.
class Janela2(QWidget):
    # O comando def(definion->definição) define uma função. Neste caso, estamos definindo 
    # a função de inicialização de classe init(__init__). Esta função realiza o start (coloca para
    # funcionar) a classe Janela2. Na função __init__ passamos como 
    # parâmetro o comando self que indica a classe que teremos
    # controle que está com prefixo self, faz a referência a própria
    # classe. Ex.: self.label_nome = QLabel: isso indica que a Label pertence à classe
    # Janela2, assim como os demais controles(label, line edit, setlayout).

    def __init__(self):
        super().__init__()
        # Adicionar um texto do título da janela
        self.setWindowTitle("Janela de cadastro")

        # Configurar posição e tamanho
        # O primeiro valor é a posição y medida em pixel
        # O segundo valor é a posição y medida em pixel
        # O terceiro valor é a largura(width) medida em pixel
        # O quarto valor é a altura(height) medida em pixel
        
        self.setGeometry(50,200,500,200)

        # Adicionar uma label à janela
        # Uma label(rótulo) é um texto que é apresentado
        # em uma janela para indicar o que deve ser feito a
        # frente (geralmente uma caixa de texto). No exemplo abaixo
        # estamos criando uma Label para apresentar o texto 
        # Nome Completo, isso indica ao usuário que ele deve escrever o nome em uma
        # caixa de texto a frente.
        # Geralmente, uma label é usada em combinação uma caixa
        # de texto(QlineEdit)

        self.label_nome = QLabel("Nome completo: ")

        # adicionar uma caixa de texto 
        self.edit_nome = QLineEdit()

        # Adicionar Layout para organizar os elementos
        # Estamos usando o gerenciador de layout vertical (QvBoxLayout)
        # ele é utilizado para organizar os controles que irão aparecer
        # na Janela2. O QvBoxLayout foi utilizado para dsispor os 
        # controles um abaixo do outro. Para exibir um ao lado do outro
        # usamos o comando QHBoxLayout.
        layout = QVBoxLayout()

        # Para adicionar a label_nome e o edit_nome ao
        # organizador(Layout) vertical, usamos o comando 
        # add (adicionar) Widget->(controle). Assim, os controles
        # irão aparecer um abaixo do outro, pois este organizador
        # é do tipo vertical.
        layout.addWidget(self.label_nome)
        layout.addWidget(self.edit_nome)
        
        # Adicionar o layout a tela
        #       
        self.setLayout(layout)

app = QApplication(sys.argv)
jan = Janela2()
jan.show()
app.exec_()
