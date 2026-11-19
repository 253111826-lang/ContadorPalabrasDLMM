import sys 
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #Carga de nuestra vista
        uic.loadUi("ContadorPalabras.ui",self)
        self.btnContar.clicked.connect((self.ContarPalabras))
        
    def ContarPalabras(self):
        # Recuperar el texto ✔✔✔
        texto = self.edtCaracteres.text()


        # Separar las palabras
        textoSeparado = texto.split()
        print(textoSeparado)


        # Contar las palabras
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Palabras:{cantidadPalabras}")
        
        # Contar los caracteres
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")
        #condicionar la alerta
        if cantidadPalabras >= 20: 
         self.tvCaracteres.setStyleSheet("background-color: ; color: #ff0000;")
        else:
            self.tvCaracteres.setStyleSheet("background-color: ; color: #00000;")
        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("background-color: ; color: #ff0000;")

        
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())
        
    