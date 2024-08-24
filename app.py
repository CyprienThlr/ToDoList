from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

def add_task():
    # Créer un nouveau widget carré
    square = QWidget()
    square.setFixedSize(378, 60)  # Taille fixe pour le carré
    square.setStyleSheet("""
        QWidget {
            background-color: #E1F0DA;
            border-radius: 15px;  /* Coins arrondis */
            border: 1px solid #99BC85;
        }
    """)

    # Créer une étiquette pour le texte à l'intérieur du carré
    text_label = QLabel('New Task')
    font = QFont('Arial', 12)
    text_label.setFont(font)
    text_label.setAlignment(Qt.AlignCenter)  # Centrage horizontal du texte à l'intérieur du carré

    # Disposition pour centrer le texte à l'intérieur du carré
    square_layout = QVBoxLayout()
    square_layout.addWidget(text_label)
    square.setLayout(square_layout)

    # Ajouter le carré au layout des carrés, centré horizontalement
    squares_layout.addSpacing(10)  # Espacement de 10 pixels au-dessus des carrés
    squares_layout.addWidget(square, alignment=Qt.AlignHCenter)

def main():
    # Créer l'application
    app = QApplication(sys.argv)

    # Créer la fenêtre principale
    global window, squares_layout
    window = QWidget()
    window.setWindowTitle('Title')
    window.setGeometry(100, 100, 400, 600)  # x, y, width, height

    # Changer la couleur de fond
    window.setStyleSheet("background-color: #FFF8E3;")

    # Créer un layout vertical pour organiser les widgets principaux
    main_layout = QVBoxLayout()

    # Créer l'étiquette
    label = QLabel('To-Do List')
    font = QFont('Arial', 20)  # Police 'Arial', taille 20
    label.setStyleSheet("color: #99BC85;")
    label.setFont(font)
    label.setAlignment(Qt.AlignCenter)  # Centrage horizontal

    # Ajouter l'étiquette au layout
    main_layout.addWidget(label, alignment=Qt.AlignTop)  # Aligner en haut

    # Ajouter un espacement de 10 pixels sous l'étiquette
    main_layout.addSpacing(10)  # Espacement entre l'étiquette et la ligne

    # Créer une ligne de séparation avec une épaisseur personnalisée
    line = QFrame()
    line.setFrameShape(QFrame.HLine)  # Ligne horizontale
    line.setFrameShadow(QFrame.Sunken)  # Apparence enfoncée
    line.setStyleSheet("border: 2px solid #99BC85;")  # Définir l'épaisseur de la ligne

    main_layout.addWidget(line)

    # Ajouter un layout pour les carrés
    squares_layout = QVBoxLayout()
    main_layout.addLayout(squares_layout)
    main_layout.addStretch()  # Ajoute un espace extensible pour pousser le bouton vers le bas

    # Créer un layout horizontal pour le bouton en bas
    button_layout = QHBoxLayout()
    button_layout.addStretch()  # Ajoute un espace extensible pour pousser le bouton à droite

    # Créer le bouton "+"
    button = QPushButton('+')
    button.setFixedSize(55, 55)  # Taille fixe pour le bouton
    button.setStyleSheet("""
        QPushButton {
            background-color: #BFD8AF;  /* Couleur de fond */
            border-radius: 25px;  /* Coins arrondis */
            color: white;  /* Couleur du texte */
            font-size: 35px;  /* Taille de la police */
            border: 1px solid #99BC85;  /* Bordure du bouton */
            text-align: center;  /* Centrer le texte */
            padding-bottom: 5px;  /* Remplissage en bas */
        }
        QPushButton:hover {
            background-color: #99BC85;  /* Couleur de fond au survol */
        }
        QPushButton:pressed {
            background-color: #99BC85;  /* Couleur de fond lorsqu'il est pressé */
        }
    """)

    # Connecter le signal de clic du bouton à la fonction add_task
    button.clicked.connect(add_task)

    # Ajouter le bouton au layout du bas à droite
    button_layout.addWidget(button, alignment=Qt.AlignRight)

    # Ajouter le layout du bouton au layout principal
    main_layout.addLayout(button_layout)

    # Appliquer le layout principal à la fenêtre
    window.setLayout(main_layout)

    # Afficher la fenêtre
    window.show()

    # Démarrer la boucle d'événements
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
