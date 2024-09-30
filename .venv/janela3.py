from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class Janela3(QWidget):
    def __init__(self):
        super().__init__()
    
        # definir o texto que irá aparecer no título da janela
        self.setWindowTitle("Cadastrar Usuário")
        # definir posição e tamanho da tela
        self.setGeometry(100,100,500,400)
        # criar as labels para o nome de usuário, email, senha e nível de acesso
        self.label_nome_usuario = QLabel ("Nome de usuário:")
        self.label_nome_usuario.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")

        self.label_email = QLabel ("E-mail:")
        self.label_email.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")

        self.label_senha = QLabel ("Senha:")
        self.label_senha.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")

        self.label_nivel_acesso = QLabel ("Acesso:")
        self.label_nivel_acesso.setStyleSheet("QLabel{color:#ff0000;font-size:12pt;font-weight:bold;text-transform:upperCase}")  


        # Criação das LineEdits
        self.edit_nome_usuario = QLineEdit()
        self.edit_nome_usuario.setStyleSheet("QLineEdit{background-color:#999; color:#000; padding:10px; border-radius:10px}")

        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("QLineEdit{background-color:#999; color:#000; padding:10px; border-radius:10px}")
        
        self.edit_senha = QLineEdit()
        self.edit_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.edit_senha.setStyleSheet("QLineEdit{background-color:#999; color:#000; padding:10px; border-radius:10px}")
        
        self.edit_nivel_acesso = QLineEdit()
        self.edit_nivel_acesso.setStyleSheet("QLineEdit{background-color:#999; color:#000; padding:10px; border-radius:10px}")

        # Criar o botão
        self.button_cadastrar = QPushButton("Cadastrar")
        self.button_cadastrar.clicked.connect(self.mensagem)

        # Criar o layout vertical para organizar os controles
        layout = QVBoxLayout()
        # Adicionar os controles aos layout
        layout.addWidget(self.label_nome_usuario)
        layout.addWidget(self.edit_nome_usuario)

        layout.addWidget(self.label_email)
        layout.addWidget(self.edit_email)

        layout.addWidget(self.label_senha)
        layout.addWidget(self.edit_senha)

        layout.addWidget(self.label_nivel_acesso)
        layout.addWidget(self.edit_nivel_acesso)

        layout.addWidget(self.button_cadastrar)

        self.setLayout(layout)

    def mensagem(self):
        print(self.edit_nome_usuario.text())
        print(self.edit_email.text())
        print(self.edit_senha.text())
        print(self.edit_nivel_acesso.text())


app = QApplication(sys.argv)
janela = Janela3()
janela.show()
app.exec_()