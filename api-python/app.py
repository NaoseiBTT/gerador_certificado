import os
from datetime import datetime
from flask import Flask, request, send_file
from flask_cors import CORS
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {
        "Mensagem": "API Python funcionando!"
    }


@app.route("/certificado", methods=["POST"])
def certificado():
    dados = request.get_json()

    nome = dados.get("nome", "Nome do Aluno")
    curso = dados.get("curso", "Nome do Curso")
    carga = dados.get("cargaHoraria", "0h")

    arquivo = "certificado.pdf"

    # Define orientação Paisagem (A4 Deitado: 842px largura x 595px altura)
    largura, altura = landscape(A4)
    pdf = canvas.Canvas(arquivo, pagesize=(largura, altura))

    # --- DEFINIÇÃO DE CORES ---
    AZUL_ESCURO = HexColor("#1A365D")
    DOURADO = HexColor("#D69E2E")
    CINZA_TEXTO = HexColor("#2D3748")
    CINZA_SUAVE = HexColor("#718096")

    # --- MOLDURA DECORATIVA DUPLA ---
    # Borda Externa (Azul)
    pdf.setStrokeColor(AZUL_ESCURO)
    pdf.setLineWidth(5)
    pdf.rect(20, 20, largura - 40, altura - 40)

    # Borda Interna (Dourada)
    pdf.setStrokeColor(DOURADO)
    pdf.setLineWidth(1.5)
    pdf.rect(28, 28, largura - 56, altura - 56)

    # --- CABEÇALHO ---
    pdf.setFillColor(AZUL_ESCURO)
    pdf.setFont("Helvetica-Bold", 34)
    pdf.drawCentredString(largura / 2, altura - 90, "CERTIFICADO DE CONCLUSÃO")

    # Linha Decorativa Dourada Sob o Título
    pdf.setStrokeColor(DOURADO)
    pdf.setLineWidth(2)
    pdf.line(largura / 2 - 120, altura - 105, largura / 2 + 120, altura - 105)

    # --- CORPO DO TEXTO ---
    pdf.setFillColor(CINZA_TEXTO)
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(largura / 2, altura - 160, "Certificamos que")

    # Nome do Aluno
    pdf.setFillColor(AZUL_ESCURO)
    pdf.setFont("Helvetica-Bold", 28)
    pdf.drawCentredString(largura / 2, altura - 210, nome.upper())

    # Linha de destaque para o Nome
    pdf.setStrokeColor(AZUL_ESCURO)
    pdf.setLineWidth(0.8)
    pdf.line(largura / 2 - 200, altura - 220, largura / 2 + 200, altura - 220)

    # Descrição do Curso
    pdf.setFillColor(CINZA_TEXTO)
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(
        largura / 2,
        altura - 270,
        f"concluiu com êxito o curso de {curso}"
    )

    pdf.setFont("Helvetica-Bold", 15)
    pdf.drawCentredString(
        largura / 2,
        altura - 305,
        f"com carga horária total de {carga}."
    )

    # --- SELO DECORATIVO (Canto Inferior Esquerdo) ---
    pdf.setFillColor(DOURADO)
    pdf.circle(120, 110, 32, fill=1, stroke=0)
    pdf.setFillColor(AZUL_ESCURO)
    pdf.circle(120, 110, 26, fill=1, stroke=0)
    pdf.setFillColor(HexColor("#FFFFFF"))
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawCentredString(120, 114, "EXCELÊNCIA")
    pdf.drawCentredString(120, 102, "★ ★ ★")

    # --- DATA E ASSINATURA (Lado Direito e Centro) ---
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Data
    pdf.setFillColor(CINZA_SUAVE)
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(largura / 2 - 150, 130, f"Emitido em: {data_atual}")
    pdf.setStrokeColor(CINZA_SUAVE)
    pdf.setLineWidth(0.5)
    pdf.line(largura / 2 - 230, 145, largura / 2 - 70, 145)

    # Assinatura
    pdf.setFillColor(AZUL_ESCURO)
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawCentredString(largura / 2 + 150, 130, "Coordenação")
    pdf.setStrokeColor(AZUL_ESCURO)
    pdf.setLineWidth(1)
    pdf.line(largura / 2 + 50, 145, largura / 2 + 250, 145)

    # Rodapé institucional
    pdf.setFillColor(CINZA_SUAVE)
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawCentredString(largura / 2, 45, "Documento emitido eletronicamente")

    pdf.save()

    return send_file(
        arquivo,
        as_attachment=True,
        download_name="certificado.pdf"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port
    )