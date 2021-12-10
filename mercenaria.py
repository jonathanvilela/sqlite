import sqlite3
import mysql.connector
from tkinter import*
import mysql.connector
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from datetime import datetime


banco= sqlite3.connect('banco_mercearia2.db')

cursor = banco.cursor()

now=datetime.now()

ano=str(now.year)
dia=str(now.day)
mes=str(now.month)

data=dia+"/"+mes+"/"+ano

hora=str(now.hour)
minutos=str(now.minute)
segundos=str(now.second)

horario=hora+":"+minutos+":"+segundos

opcao=0

sair='sair'

while opcao!=sair:

    print("Seja bem vindo, o que deseja?\n")
    print("Cadastrar Produtos?\n")
    print("Buscar Produtos?\n")
    print("Sair.\n")
    opcao=str(input("Qual opcao Deseja?"))

    if opcao=='cadastrar':
        opcao2=str(input("produto é legume ou fruta ou vegetal?:"))
        if opcao2=='fruta':
            fruta=str(input("Digite o nome do produto para cadastro"))
            print(fruta,"cadastrado")

            #-1-CRIA TABELA
            cursor.execute("CREATE TABLE IF NOT EXISTS tbl_frutas(fruta text,data text, horario text)")

            dados='\''+fruta+'\',\''+data+'\',\''+horario+'\')'
            #-2-inserir as informaçoes na tabela
            declaracao=""" INSERT INTO tbl_frutas VALUES("""+dados

            cursor.execute(declaracao)

            banco.commit()

        elif opcao2=='legume':
            legume=str(input("Digite o nome do legume para cadastro:"))
            print(legume,"cadastrado.")
            
            
            cursor.execute("CREATE TABLE IF NOT EXISTS tbl_legumes(legume text,data text, horario text)")

            dados='\''+legume+'\',\''+data+'\',\''+horario+'\')'
            #-2-inserir as informaçoes na tabela
            declaracao=""" INSERT INTO tbl_legumes VALUES("""+dados

            cursor.execute(declaracao)

            banco.commit()

        elif opcao2=='vegetal':
            vegetal=str(input("Digite o nome do vegetal para cadastro:"))
            print(vegetal,"cadastrado")
            
            cursor.execute("CREATE TABLE IF NOT EXISTS tbl_vegetais(vegetal text,data text, horario text)")

            dados='\''+vegetal+'\',\''+data+'\',\''+horario+'\')'
            #-2-inserir as informaçoes na tabela
            declaracao=""" INSERT INTO tbl_vegetais VALUES("""+dados

            cursor.execute(declaracao)

            banco.commit()

    elif opcao=='buscar':
        #print("\n*** Essa busca está em andamento. ***\n")

        tipo_busca=str(input("Qual tipo de busca? Geral ou Especifica?"))
                       
        if tipo_busca=='especifica':
                       
            classe_busca=str(input("Digite a classificação do Produto ex:fruta/legume/vegetal:"))

            if classe_busca=='fruta':
                busca_fruta=str(input("Digite o nome do produto"))
                busca= 'fruta'
                condicao = f"{busca}= \'{busca_fruta}\'"
                procurar="SELECT * FROM tbl_frutas where " +condicao
                cursor.execute(procurar)
                print("Busca efetuada:",cursor.fetchall())
                print("\n")
                       
        elif tipo_busca=='geral':
            opcao_busca=str(input("Qual tabela ? ex:fruta/legume/vegetal"))
            if opcao_busca=='fruta':
                cursor.execute("Select * from tbl_frutas")
                print("\n",cursor.fetchall())
                print("\n")
                
            elif opcao_busca=='legume':
                cursor.execute("Select * from tbl_legumes")
                print("\n",cursor.fetchall())
                print("\n")
                
            elif opcao_busca=='vegetal':
                cursor.execute("Select * from tbl_vegetais")
                print("\n",cursor.fetchall())
                print("\n")

            else:
                print("opcao invalida")
                
                

    elif opcao=='sair':
        print("\n**** Tenha um bom dia.****")
    
        
          



































    




