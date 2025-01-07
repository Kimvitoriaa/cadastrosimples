import tkinter as tk
from tkinter import messagebox

class ProductManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        self.root.geometry("400x400")

      
        self.products = []

        self.create_widgets()

    def create_widgets(self):
     
        self.label_name = tk.Label(self.root, text="Nome do Produto:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

       
        self.label_desc = tk.Label(self.root, text="Descrição do Produto:")
        self.label_desc.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_desc = tk.Entry(self.root)
        self.entry_desc.grid(row=1, column=1, padx=10, pady=5)

        self.label_price = tk.Label(self.root, text="Preço do Produto:")
        self.label_price.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_price = tk.Entry(self.root)
        self.entry_price.grid(row=2, column=1, padx=10, pady=5)

        self.label_avail = tk.Label(self.root, text="Disponível para Venda:")
        self.label_avail.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_avail = tk.StringVar(value="Sim")
        self.option_avail = tk.OptionMenu(self.root, self.entry_avail, "Sim", "Não")
        self.option_avail.grid(row=3, column=1, padx=10, pady=5)

  
        self.button_add = tk.Button(self.root, text="Cadastrar Produto", command=self.add_product)
        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)

       
        self.list_label = tk.Label(self.root, text="Produtos Cadastrados:")
        self.list_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.root, height=6, width=35)
        self.listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

      
        self.button_show = tk.Button(self.root, text="Mostrar Lista", command=self.show_list)
        self.button_show.grid(row=7, column=0, columnspan=2, pady=5)

    def add_product(self):
        """Função para adicionar o produto à lista"""
        name = self.entry_name.get()
        desc = self.entry_desc.get()
        try:
            price = float(self.entry_price.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido! Informe um número.")
            return
        avail = self.entry_avail.get()

        
        if name and desc and price > 0:
            product = {"name": name, "desc": desc, "price": price, "avail": avail}
            self.products.append(product)
            self.show_list()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente!")

    def show_list(self):
        """Função para exibir a lista de produtos cadastrados"""
        self.listbox.delete(0, tk.END)  # Limpar a lista atual

        if self.products:
            for product in self.products:
                self.listbox.insert(tk.END, f"{product['name']} - R${product['price']:.2f}")
        else:
            self.listbox.insert(tk.END, "Nenhum produto cadastrado.")

if __name__ == "__main__":
  
    root = tk.Tk()
    app = ProductManagerApp(root)
    root.mainloop()

       

