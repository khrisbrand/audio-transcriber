from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle("Ejemplo PyQt")
label = QLabel("¡Hola desde PyQt!", parent=window)
label.move(50, 50)
window.resize(300, 200)
window.show()
app.exec()
