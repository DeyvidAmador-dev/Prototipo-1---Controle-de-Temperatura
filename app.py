import tkinter as tk


output_file = 'tanque_1.txt'


def executar_controle():
    try:
        with open('tanque_1.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if executar_controle.current_line < len(linhas):
                linha = linhas[executar_controle.current_line].strip()
                if 'temperatura' in linha:
                    temperatura_label.config(
                        text="Temperatura: " + linha.split(":")[1].strip())
                if 'velocidade do cooler' in linha:
                    velocidade_label.config(
                        text="Velocidade do cooler: " + linha.split(':')[1].strip())
                executar_controle.current_line += 1
            else:
                executar_controle.current_line = 0
    except Exception as e:
        resultado_label.config(text="Erro ao abrir arquivo: " + str(e))
    # Agende a próxima execução em 5 segundos
    janela.after(5000, executar_controle)


executar_controle.current_line = 0


janela = tk.Tk()
janela.title("Controle de Temperatura e estado do Cooler")

temperatura_label = tk.Label(janela, text="Temperatura: ")
temperatura_label.pack()
velocidade_label = tk.Label(janela, text="Velocidade do cooler: ")
velocidade_label.pack()

lmt_temp_label = tk.Label(janela, text="Temperatura ideal: 29 °C")
lmt_temp_label.pack()

botão = tk.Button(janela, text='Excutar Medição', command=executar_controle)
botão.pack()


resultado_label = tk.Label(janela, text='')
resultado_label.pack()


# Inicia a primeira chamada após 5 segundos
janela.after(5000, executar_controle)
janela.mainloop()
