import streamlit as st
import time
from views import View

class AlterarMeusDadosUI:
    def main():
      if st.session_state["cliente_id"] == 1:
         senha = st.text_input("Informe a nova senha", type="password")
         if st.button("Atualizar"):
            View.cliente_atualizar(st.session_state["cliente_id"], "admin", "admin", 1234, senha)
            st.success("Dados atualizado com sucesso")
            time.sleep(2)
            st.rerun()
      else:
        st.header("Alterar sua senha")
        clientes = View.cliente_listar_id(st.session_state["cliente_id"])
        nome = st.text_input("Informe o novo nome", clientes.nome)
        email = st.text_input("Informe o novo e-mail", clientes.email)
        fone = st.text_input("Informe o novo fone", clientes.fone)
        senha = st.text_input("Informe a nova senha", clientes.senha, type="password")
        if st.button("Atualizar"):
            View.cliente_atualizar(clientes.id, nome, email, fone, senha)
            st.success("Dados atualizado com sucesso")
            time.sleep(2)
            st.rerun()
      
      '''nome = input("Novo nome (ou pressione Enter para manter o atual): ") or cliente.nome
      email = input("Novo email (ou pressione Enter para manter o atual): ") or cliente.email
      fone = input("Novo telefone (ou pressione Enter para manter o atual): ") or cliente.fone
      senha = input("Nova senha (ou pressione Enter para manter a atual): ") or cliente.senha
        
      # Cria um novo objeto Cliente com os dados atualizados
      cliente_atualizado = Cliente(cliente.id, nome, email, fone, senha)
      Clientes.atualizar(cliente_atualizado)  # Atualiza os dados
      print("Cliente atualizado com sucesso!")'''