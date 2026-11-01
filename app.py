import os
from datetime import datetime

import gradio as gr
import pandas as pd

ARQUIVO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pacientes.csv")
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]
CONVENIOS = ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"]


def ultimos_pacientes(n=5):
    if not os.path.exists(ARQUIVO_CSV):
        return pd.DataFrame(columns=COLUNAS)
    return pd.read_csv(ARQUIVO_CSV, encoding="utf-8-sig").tail(n)


def cadastrar_paciente(nome, idade, convenio, prioridade, motivo):
    nome = (nome or "").strip()
    erros = []
    if not nome:
        erros.append("informe o nome do paciente")
    if idade is None or idade < 0 or idade > 120:
        erros.append("informe uma idade entre 0 e 120")
    if not convenio:
        erros.append("selecione o convênio")
    if erros:
        manter = gr.update()
        return ("Erro: " + "; ".join(erros) + ".", ultimos_pacientes(),
                manter, manter, manter, manter, manter)

    linha = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": nome,
        "idade": int(idade),
        "convenio": convenio,
        "prioridade": int(prioridade),
        "motivo": (motivo or "").strip(),
    }
    novo = pd.DataFrame([linha], columns=COLUNAS)
    if os.path.exists(ARQUIVO_CSV):
        novo.to_csv(ARQUIVO_CSV, mode="a", header=False, index=False, encoding="utf-8-sig")
    else:
        novo.to_csv(ARQUIVO_CSV, mode="w", header=True, index=False, encoding="utf-8-sig")

    return (f"Paciente {nome} cadastrado com sucesso!", ultimos_pacientes(),
            "", None, None, 3, "")


with gr.Blocks(title="Cadastro de Pacientes") as demo:
    gr.Markdown("## Cadastro de Pacientes\nRecepção do consultório — preencha e clique em **Cadastrar**.")

    nome = gr.Textbox(label="Nome do paciente", placeholder="Ex.: Maria da Silva", max_lines=1)
    idade = gr.Number(label="Idade", minimum=0, maximum=120, precision=0)
    convenio = gr.Dropdown(CONVENIOS, label="Convênio")
    prioridade = gr.Slider(1, 5, value=3, step=1, label="Prioridade do atendimento (5 = urgente)")
    motivo = gr.Textbox(label="Motivo da consulta / observações", lines=3)
    botao = gr.Button("Cadastrar", variant="primary")

    saida_msg = gr.Textbox(label="Status", interactive=False)
    tabela = gr.Dataframe(label="Últimos pacientes cadastrados", interactive=False)

    botao.click(
        cadastrar_paciente,
        [nome, idade, convenio, prioridade, motivo],
        [saida_msg, tabela, nome, idade, convenio, prioridade, motivo],
    )
    demo.load(ultimos_pacientes, None, tabela)

if __name__ == "__main__":
    demo.launch()
