import os
import streamlit as st
from src.swot.crew import SwotCrew

# Title for the Streamlit app
st.title('Análise SWOT com LLM & AI Agents - by CrewAI')

# Input field for the site URL
site_url = st.text_input("Digite a URL do site para análise, incluindo o https:// ")

# Initialize session state for analysis status and generated Markdown files
if "analise_realizada" not in st.session_state:
    st.session_state.analise_realizada = False
    st.session_state.arquivos_md = []

# Button to initiate analysis
if st.button("Iniciar Análise") and site_url:
    # Run the analysis process
    inputs = {'site_url': site_url}
    crew_instance = SwotCrew().crew()

    # Execute tasks to generate reports
    crew_instance.kickoff(inputs=inputs)

    # Assuming the tasks generate Markdown files as output
    output_files = [
        'pesquisar_solucoes_ia.md',
        'analise_swot.md',
        'financiamento_estrategico.md',
        'analisar_recomendar_swot.md'
    ]
    # Check if files exist and add them to session state
    st.session_state.arquivos_md = [
        file for file in output_files if os.path.exists(file)
    ]
    st.session_state.analise_realizada = True

# Display download links if analysis is completed and files are available
if st.session_state.analise_realizada and st.session_state.arquivos_md:
    st.write("### Resultados da Análise")
    for file in st.session_state.arquivos_md:
        with open(file, "rb") as f:
            st.download_button(
                label=f"Baixar {file}",
                data=f,
                file_name=file,
                mime="text/markdown"
            )