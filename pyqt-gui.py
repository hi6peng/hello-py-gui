from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
  def __init__(self):
      super().__init__()

      self.setGeometry(200, 400, 400, 200)
      self.setWindowTitle("PyQt5 Window Example")
      self.show()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
