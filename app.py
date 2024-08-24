from PyQt5.QtWidgets import QApplication, QWidget
import sys

def main():

    #Creation of the application
    app = QApplication(sys.argv)

    # Creation of the princinpal window
    window = QWidget()
    window.setWindowTitle('Title')
    window.setGeometry(100, 100, 800, 600) # x, y, width, height

    # Windiw display
    window.show()

    # Start the event loop
    sys.exit(app.exec_())