import tkinter as tk
from tkinter import filedialog
import folium
from folium.plugins import MarkerCluster
import pandas as pd

def carregar_arquivo():
    # Abrir a caixa de diálogo para selecionar o arquivo
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xls;*.xlsx")])

    if arquivo:
        entry_arquivo.delete(0, tk.END)  # Limpar o texto anterior
        entry_arquivo.insert(0, arquivo)  # Exibir o caminho do arquivo no Entry

def gerar_mapa():
    # Obter o caminho do arquivo a partir do Entry
    arquivo = entry_arquivo.get()

    if arquivo:
        # Ler o arquivo XLS
        df = pd.read_excel(arquivo)

        # Criar um mapa centrado em uma localização específica
        mapa = folium.Map(location=[-5.8803, -35.1602], zoom_start=10)

        # Adicionar um cluster de marcadores ao mapa
        marker_cluster = MarkerCluster().add_to(mapa)

        # Iterar sobre as linhas do DataFrame
        for index, row in df.iterrows():
            try:
                # Extrair as coordenadas da coluna 'Coordenadas'
                coord = tuple(map(float, row['Coordenadas'].split()))

                # Adicionar marcador ao cluster
                folium.Marker(location=coord).add_to(marker_cluster)
            except Exception as e:
                print(f"Erro ao processar linha {index}: {e}")

        # Salvar o mapa em um arquivo HTML
        mapa.save('mapa_com_enderecos.html')
        print("Mapa gerado com sucesso!")

# Configurar a interface gráfica com Tkinter
root = tk.Tk()
root.title("SISTEMA DE COORDENADAS - DRLD")
root.geometry("400x300")  # Ajustar tamanho da janela
root.configure(bg="#d9d9d9")  # Configurar cor de fundo

# Entry para exibir o caminho do arquivo
entry_arquivo = tk.Entry(root, width=40)
entry_arquivo.pack(pady=10)

# Botão para carregar o arquivo
btn_carregar = tk.Button(root, text="Carregar Arquivo", command=carregar_arquivo)
btn_carregar.pack(pady=10)

# Botão para gerar o mapa
btn_gerar_mapa = tk.Button(root, text="Gerar Mapa", command=gerar_mapa)
btn_gerar_mapa.pack(pady=20)

# Iniciar o loop principal
root.mainloop()


