from tkinter import *

menu_principal = Tk()
menu_principal.title('CADASTRO IMC v2.0')
menu_principal.geometry('250x150')
menu_principal.resizable(False, False)



# ------------------- funções -----------------------------------------------------------------------


def base_de_dados():
    global nome_arquivo, arquivo
    nome_arquivo = t1.get()
    try:
        arquivo = open(nome_arquivo, 'r')
    except FileNotFoundError:
        print('Este arquivo não existe, será criado agora')
        arquivo = open(nome_arquivo, 'w')
    else:
        print('Arquivo já existente, iremos adicionar dados a ele!!')
    finally:
        arquivo.close()


def cadastro():
    global arquivo

    nome = t2.get()
    peso = t3.get()
    altura = t4.get()

    try:
        kg = float(peso)
        height = float(altura)
        imc = kg/(height*height)
        arquivo = open(nome_arquivo, 'at')
        arquivo.writelines(f'{nome}; {kg}kg; {height}m; IMC: {imc:.2f}\n')

    except FileNotFoundError:
        print('Tivemos um erro, o arquivo não foi encontrado')
    finally:
        print('Dados cadastrados com sucesso')
        arquivo.close()

# ----------------------------------------( WIDGETS )------------------------------------------------------


t1 = Entry(menu_principal)
t2 = Entry(menu_principal)
t3 = Entry(menu_principal)
t4 = Entry(menu_principal)

l1 = Label(menu_principal, text='Nome arquivo: ').grid(row=2, column=1, sticky=W)
l2 = Label(menu_principal, text='Nome: ').grid(row=4, column=1, sticky=W)
l3 = Label(menu_principal, text='Peso(kg): ').grid(row=5, column=1, sticky=W)
l4 = Label(menu_principal, text='Altura(m): ').grid(row=6, column=1, sticky=W)

database = Button(menu_principal, text='Criar/Abrir', command=base_de_dados)
cadastro_dados = Button(menu_principal, text='Cadastrar dados', command=cadastro)
# ---------------------------------------( LAYOUT )--------------------------------------------------------
t1.grid(row=2, column=2)
t2.grid(row=4, column=2)
t3.grid(row=5, column=2)
t4.grid(row=6, column=2)
database.grid(row=3, column=2)
cadastro_dados.grid(row=7, column=2)

menu_principal.mainloop()