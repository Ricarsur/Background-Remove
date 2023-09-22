import tkinter as tk
from tkinter import filedialog

from rembg import remove

ventana = tk.Tk()
ventana.withdraw()

file = filedialog.askopenfilename(title = "Seleccione una imagen")

if file:
      input_path = file
      output_path= 'resutado.png'

      with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
      print(f"La imagen se ha procesado y guardado en {output_path}")
else:
    print("Ninguna imagen seleccionada")