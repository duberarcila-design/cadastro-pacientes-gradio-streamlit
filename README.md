# Atividade Prática Aula 1 — Cadastro de Pacientes (Gradio x Streamlit)

Prof. Francisco Fambrini — Aplicações em Data Science.

A mesma aplicação de cadastro de pacientes (nome, idade, convênio, prioridade 1–5, motivo + data/hora) feita com duas bibliotecas:

| Pasta | Biblioteca | Execução | Persistência |
|---|---|---|---|
| `gradio_app/` | Gradio (`gr.Blocks`) | Local | `gradio_app/pacientes.csv` |
| `streamlit_app/` | Streamlit (`st.form` + `st.session_state`) | Streamlit Community Cloud | Sessão + botão **Baixar CSV** |

App publicado: streamlit.app>`](https://cadastro-pacientes-gradio-app-toovljfvqgngrt5cap9uya.streamlit.app/)

## Como executar localmente

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Gradio  -> http://127.0.0.1:7860
python gradio_app/app.py

# Streamlit -> http://localhost:8501
streamlit run streamlit_app/app.py
```

## Observações

- O sistema de arquivos do Streamlit Community Cloud é efêmero: o CSV gravado no servidor se perde ao reiniciar o app. Por isso há o botão **Baixar CSV**, que exporta os pacientes cadastrados na sessão.
- `gradio_app/pacientes.csv` é um arquivo de exemplo gerado durante os testes, com dados fictícios.
