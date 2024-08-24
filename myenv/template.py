from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
import sys

def on_button_click():
    label.setText('Bouton cliqué!')

def main():
    # Créer l'application
    app = QApplication(sys.argv)

    # Créer la fenêtre principale
    window = QWidget()
    window.setWindowTitle('ToDo List - Gestion App')
    window.setGeometry(100, 100, 800, 600)  # Position (x, y) et taille (largeur, hauteur)

    # Créer un label
    global label
    label = QLabel('')

    # Créer des widgets
    label = QLabel('Entrez quelque chose:')
    line_edit = QLineEdit()
    button = QPushButton('Cliquez-moi')

    # Créer un layout vertical
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(line_edit)
    layout.addWidget(button)
    button.clicked.connect(on_button_click)  # Connexion du signal au slot

    # Appliquer le layout à la fenêtre
    window.setLayout(layout)
    # Afficher la fenêtre
    window.show()

    # Lancer la boucle d'événements
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()