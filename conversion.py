import tkinter as tk
from tkinter import messagebox

def celsius_para_fahrenheit():
    try:
        celsius = float(entry_temperatura.get())
        fahrenheit = (celsius * 9/5) + 32
        label_resultado['text'] = f'{fahrenheit:.2f} °F'
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

def fahrenheit_para_celsius():
    try:
        fahrenheit = float(entry_temperatura.get())
        celsius = (fahrenheit - 32) * 5/9
        label_resultado['text'] = f'{celsius:.2f} °C'
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

janela = tk.Tk()
janela.title("Conversor de Temperatura")

label_entrada = tk.Label(janela, text="Insira a temperatura:")
label_entrada.grid(row=0, column=0, padx=10, pady=10)

entry_temperatura = tk.Entry(janela)
entry_temperatura.grid(row=0, column=1, padx=10, pady=10)

botao_c_para_f = tk.Button(janela, text="Celsius para Fahrenheit", command=celsius_para_fahrenheit)
botao_c_para_f.grid(row=1, column=0, padx=10, pady=10)

botao_f_para_c = tk.Button(janela, text="Fahrenheit para Celsius", command=fahrenheit_para_celsius)
botao_f_para_c.grid(row=1, column=1, padx=10, pady=10)

label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()