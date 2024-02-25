import tkinter as tk

historico_contas = []

def adicionar_numero(numero):
    entrada_numero = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, entrada_numero + str(numero))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    expressao = entrada.get()
    try:
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        historico_contas.append(expressao + " = " + str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def mostrar_historico():
    historico_window = tk.Toplevel(root)
    historico_window.title("Histórico de Contas")
    historico_window.geometry("300x200")

    historico_listbox = tk.Listbox(historico_window, font=('Arial', 12))
    for item in historico_contas:
        historico_listbox.insert(tk.END, item)
    historico_listbox.pack(padx=10, pady=10)

root = tk.Tk()
root.title("Calculadora")
root.configure(bg='black')

# Entrada
entrada = tk.Entry(root, font=('Arial', 20), bd=5, justify='right', bg='gray', fg='white')
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

# Botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Histórico', 1, 4)
]

for (text, row, column) in botoes:
    if text == 'C':
        botao = tk.Button(root, text=text, font=('Arial', 14), bg='orange', padx=20, pady=20, command=limpar)
    elif text == '=':
        botao = tk.Button(root, text=text, font=('Arial', 14), bg='green', padx=20, pady=20, command=calcular)
    elif text == 'Histórico':
        botao = tk.Button(root, text=text, font=('Arial', 14), padx=20, pady=20, bg='blue', fg='white', command=mostrar_historico)
    else:
        botao = tk.Button(root, text=text, font=('Arial', 14), padx=20, pady=20, command=lambda t=text: adicionar_numero(t))
    botao.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

# Configurar peso das linhas e colunas para permitir redimensionamento
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
