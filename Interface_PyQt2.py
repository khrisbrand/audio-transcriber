from PySide6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle("Ejemplo PySide6")
label = QLabel("¡Hola desde PySide6!", parent=window)
label.move(50, 50)
window.resize(300, 200)
window.show()
app.exec()

