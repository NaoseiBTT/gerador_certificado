import os  # <--- Adicionado para ler as variáveis de ambiente
from flask import Flask, request, send_file
from flask_cors import CORS
from reportlab.pdfgen import canvas

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

    nome = dados["nome"]
    curso = dados["curso"]
    carga = dados["cargaHoraria"]

    arquivo = "certificado.pdf"

    pdf = canvas.Canvas(arquivo)

    # Tamanho A4
    largura, altura = 595, 842

    # Moldura
    pdf.setLineWidth(3)
    pdf.rect(
        40,
        40,
        largura - 80,
        altura - 80
    )

    # Título
    pdf.setFont("Helvetica-Bold", 30)
    pdf.drawCentredString(largura / 2, 700, "CERTIFICADO")

    # Linha decorativa
    pdf.line(150, 680, 450, 680)

    # Texto inicial
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(largura / 2, 610, "Certificamos que")

    # Nome do aluno
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(largura / 2, 560, nome)

    # Curso
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(largura / 2, 500, f"concluiu o curso de {curso}")

    # Carga horária
    pdf.drawCentredString(largura / 2, 460, f"Carga horária: {carga}")

    # Data
    pdf.drawCentredString(largura / 2, 400, "Emitido em 22/07/2026")

    # Assinatura
    pdf.line(180, 250, 400, 250)
    pdf.drawCentredString(largura / 2, 220, "Coordenação SENAI")

    # Rodapé
    pdf.setFont("Helvetica-Oblique", 12)

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