
import streamlit as st
from fpdf import FPDF
import datetime

# Define questions for each client type
questions = {
    "Jovens": [
        "Qual estilo de vida o cliente jovem possui?",
        "Quais tecnologias ele gostaria de integrar ao espaço?",
        "Quais são suas preferências de design moderno?",
        "Há interesse em soluções sustentáveis?"
    ],
    "Idosos": [
        "Quais são as necessidades de acessibilidade do cliente?",
        "Quais elementos de conforto são essenciais?",
        "Há preferência por soluções sustentáveis e de longo prazo?",
        "Quais cuidados especiais devem ser considerados?"
    ],
    "Solteiros": [
        "Quais hobbies e interesses o cliente gostaria de refletir no espaço?",
        "Quais ambientes multifuncionais são desejados?",
        "Há necessidade de espaços para home office?",
        "Quais elementos de personalização são importantes?"
    ],
    "Casados/Famílias": [
        "Quantas pessoas compõem a família?",
        "Quais espaços coletivos são importantes?",
        "Como equilibrar privacidade e convivência?",
        "Há crianças ou idosos na residência?"
    ],
    "Corporativos": [
        "Qual é o ramo de atuação da empresa?",
        "Quais são as necessidades de produtividade e eficiência?",
        "Como a arquitetura pode refletir a cultura empresarial?",
        "Há interesse em espaços flexíveis e tecnológicos?"
    ],
    "Comerciais": [
        "Qual é o público-alvo do estabelecimento?",
        "Quais elementos de design atraem o consumidor?",
        "Quais são os objetivos comerciais do espaço?",
        "Há necessidade de áreas funcionais específicas?"
    ]
}

# Streamlit App UI
st.set_page_config(page_title="Briefing de Clientes", layout="centered")
st.title("📋 Aplicativo de Briefing para Arquitetos e Designers")
st.markdown("Este aplicativo ajuda arquitetos, designers de interiores e decoradores a coletar informações detalhadas sobre seus clientes com base no perfil descrito no eBook.")

# Input fields
client_name = st.text_input("Nome do Cliente")
professional_name = st.text_input("Nome do Profissional")
client_type = st.selectbox("Selecione o tipo de cliente", list(questions.keys()))

# Display questions based on client type
st.subheader(f"Perguntas para o perfil: {client_type}")
responses = {}
for q in questions[client_type]:
    responses[q] = st.text_area(q)

# Button to generate PDF
if st.button("📄 Gerar PDF do Briefing"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Briefing de Cliente", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Data: {datetime.date.today().strftime('%d/%m/%Y')}", ln=True)
    pdf.cell(200, 10, txt=f"Cliente: {client_name}", ln=True)
    pdf.cell(200, 10, txt=f"Profissional: {professional_name}", ln=True)
    pdf.cell(200, 10, txt=f"Perfil do Cliente: {client_type}", ln=True)
    pdf.ln(10)

    for question, answer in responses.items():
        pdf.multi_cell(0, 10, txt=f"{question}\nResposta: {answer}\n")
Resposta: {answer}
")

    filename = f"briefing_{client_name.replace(' ', '_')}.pdf"
    pdf.output(filename)

    with open(filename, "rb") as f:
        st.download_button("📥 Baixar PDF do Briefing", f, file_name=filename)
