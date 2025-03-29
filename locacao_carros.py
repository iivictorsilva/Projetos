import tkinter as tk
from tkinter import messagebox

# Classe para representar um veículo
class Veiculo:
    def __init__(self, marca, modelo, ano, diaria, status="Disponível"):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.diaria = diaria
        self.status = status

# Lista para armazenar os veículos
veiculos = []

# Função para adicionar um veículo
def adicionar_veiculo():
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    ano = entry_ano.get()
    diaria = entry_diaria.get()

    if not marca or not modelo or not ano or not diaria:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")
        return

    try:
        ano = int(ano)
        diaria = float(diaria)
    except ValueError:
        messagebox.showwarning("Erro", "Ano e diária devem ser números válidos!")
        return

    veiculo = Veiculo(marca, modelo, ano, diaria)
    veiculos.append(veiculo)
    messagebox.showinfo("Sucesso", "Veículo adicionado com sucesso!")
    limpar_campos()
    listar_veiculos()

# Função para listar veículos
def listar_veiculos():
    lista_veiculos.delete(0, tk.END)
    for i, veiculo in enumerate(veiculos, start=1):
        lista_veiculos.insert(tk.END, f"{i}. {veiculo.marca} {veiculo.modelo} ({veiculo.ano}) - R$ {veiculo.diaria:.2f} - {veiculo.status}")

# Função para alugar um veículo
def alugar_veiculo():
    selecionado = lista_veiculos.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um veículo para alugar!")
        return

    index = selecionado[0]
    veiculo = veiculos[index]

    if veiculo.status == "Alugado":
        messagebox.showwarning("Erro", "Este veículo já está alugado!")
        return

    veiculo.status = "Alugado"
    messagebox.showinfo("Sucesso", f"Veículo {veiculo.marca} {veiculo.modelo} alugado com sucesso!")
    listar_veiculos()

# Função para devolver um veículo
def devolver_veiculo():
    selecionado = lista_veiculos.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um veículo para devolver!")
        return

    index = selecionado[0]
    veiculo = veiculos[index]

    if veiculo.status == "Disponível":
        messagebox.showwarning("Erro", "Este veículo já está disponível!")
        return

    veiculo.status = "Disponível"
    messagebox.showinfo("Sucesso", f"Veículo {veiculo.marca} {veiculo.modelo} devolvido com sucesso!")
    listar_veiculos()

# Função para editar um veículo
def editar_veiculo():
    selecionado = lista_veiculos.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um veículo para editar!")
        return

    index = selecionado[0]
    veiculo = veiculos[index]

    # Janela de edição
    janela_edicao = tk.Toplevel(root)
    janela_edicao.title("Editar Veículo")

    # Campos de edição
    tk.Label(janela_edicao, text="Marca:").grid(row=0, column=0, padx=10, pady=5)
    entry_marca_edicao = tk.Entry(janela_edicao)
    entry_marca_edicao.insert(0, veiculo.marca)
    entry_marca_edicao.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(janela_edicao, text="Modelo:").grid(row=1, column=0, padx=10, pady=5)
    entry_modelo_edicao = tk.Entry(janela_edicao)
    entry_modelo_edicao.insert(0, veiculo.modelo)
    entry_modelo_edicao.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela_edicao, text="Ano:").grid(row=2, column=0, padx=10, pady=5)
    entry_ano_edicao = tk.Entry(janela_edicao)
    entry_ano_edicao.insert(0, veiculo.ano)
    entry_ano_edicao.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(janela_edicao, text="Diária (R$):").grid(row=3, column=0, padx=10, pady=5)
    entry_diaria_edicao = tk.Entry(janela_edicao)
    entry_diaria_edicao.insert(0, veiculo.diaria)
    entry_diaria_edicao.grid(row=3, column=1, padx=10, pady=5)

    # Função para salvar as alterações
    def salvar_edicao():
        veiculo.marca = entry_marca_edicao.get()
        veiculo.modelo = entry_modelo_edicao.get()
        veiculo.ano = int(entry_ano_edicao.get())
        veiculo.diaria = float(entry_diaria_edicao.get())
        messagebox.showinfo("Sucesso", "Veículo editado com sucesso!")
        janela_edicao.destroy()
        listar_veiculos()

    # Botão para salvar
    tk.Button(janela_edicao, text="Salvar", command=salvar_edicao).grid(row=4, column=0, columnspan=2, pady=10)

# Função para excluir um veículo
def excluir_veiculo():
    selecionado = lista_veiculos.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um veículo para excluir!")
        return

    index = selecionado[0]
    veiculo = veiculos.pop(index)
    messagebox.showinfo("Sucesso", f"Veículo {veiculo.marca} {veiculo.modelo} excluído com sucesso!")
    listar_veiculos()

# Função para limpar os campos de entrada
def limpar_campos():
    entry_marca.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)
    entry_ano.delete(0, tk.END)
    entry_diaria.delete(0, tk.END)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Sistema de Locação de Carros")

# Labels e campos de entrada
tk.Label(root, text="Marca:").grid(row=0, column=0, padx=10, pady=5)
entry_marca = tk.Entry(root)
entry_marca.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Modelo:").grid(row=1, column=0, padx=10, pady=5)
entry_modelo = tk.Entry(root)
entry_modelo.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Ano:").grid(row=2, column=0, padx=10, pady=5)
entry_ano = tk.Entry(root)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Diária (R$):").grid(row=3, column=0, padx=10, pady=5)
entry_diaria = tk.Entry(root)
entry_diaria.grid(row=3, column=1, padx=10, pady=5)

# Botões
tk.Button(root, text="Adicionar Veículo", command=adicionar_veiculo).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Alugar Veículo", command=alugar_veiculo).grid(row=5, column=0, pady=5)
tk.Button(root, text="Devolver Veículo", command=devolver_veiculo).grid(row=5, column=1, pady=5)
tk.Button(root, text="Editar Veículo", command=editar_veiculo).grid(row=6, column=0, pady=5)
tk.Button(root, text="Excluir Veículo", command=excluir_veiculo).grid(row=6, column=1, pady=5)

# Lista de veículos
lista_veiculos = tk.Listbox(root, width=50, height=10)
lista_veiculos.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Iniciar a interface
root.mainloop()
