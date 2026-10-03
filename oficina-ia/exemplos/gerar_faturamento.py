#!/usr/bin/env python3
"""Gera o PDF de exemplo do exercício 1 (slide `exercicio1`).

Todos os dados são inventados. Para mudar, edite LANCAMENTOS e rode:

    python3 gerar_faturamento.py

Precisa do reportlab (pip install reportlab).
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

SAIDA = Path(__file__).with_name("faturamento-laboratorio.pdf")

LABORATORIO = "Laboratório Vida Clara Análises Clínicas Ltda."
CNPJ = "00.000.000/0001-00"
ENDERECO = "Rua das Acácias, 123, Centro"
PERIODO = "01/09/2026 a 30/09/2026"
EMISSAO = "01/10/2026 08:14"

# (data, descrição, forma de pagamento, valor em reais, "C" entrada ou "D" saída)
LANCAMENTOS = [
    ("01/09", "Aluguel da sala comercial", "Boleto", 3200.00, "D"),
    ("02/09", "Exames particulares (balcão)", "Pix", 1845.00, "C"),
    ("03/09", "Reagentes de hematologia, Distrib. BioNorte", "Boleto", 4780.50, "D"),
    ("04/09", "Exames particulares (balcão)", "Cartão de crédito", 2310.00, "C"),
    ("05/09", "Repasse convênio Saúde Mais (ref. agosto)", "Transferência", 18450.75, "C"),
    ("05/09", "Folha de pagamento (6 funcionários)", "Transferência", 14920.00, "D"),
    ("08/09", "Coleta domiciliar", "Dinheiro", 480.00, "C"),
    ("09/09", "Energia elétrica", "Débito automático", 1136.42, "D"),
    ("10/09", "Repasse convênio Bem Viver (ref. agosto)", "Transferência", 9872.30, "C"),
    ("10/09", "Simples Nacional (DAS)", "Boleto", 3415.88, "D"),
    ("11/09", "Exames particulares (balcão)", "Pix", 2090.00, "C"),
    ("12/09", "Tubos, agulhas e material de coleta", "Cartão de crédito", 1264.90, "D"),
    ("15/09", "Exames ocupacionais, Metalúrgica Horizonte", "Boleto", 3600.00, "C"),
    ("15/09", "Coleta de resíduos de saúde", "Boleto", 690.00, "D"),
    ("16/09", "Exames particulares (balcão)", "Cartão de débito", 1575.00, "C"),
    ("17/09", "Manutenção do analisador bioquímico", "Pix", 2350.00, "D"),
    ("18/09", "Coleta domiciliar", "Pix", 640.00, "C"),
    ("19/09", "Internet e telefone", "Débito automático", 289.90, "D"),
    ("22/09", "Exames particulares (balcão)", "Cartão de crédito", 2745.00, "C"),
    ("22/09", "Sistema de laudos (mensalidade)", "Cartão de crédito", 459.00, "D"),
    ("23/09", "Reagentes de bioquímica, Distrib. BioNorte", "Boleto", 3925.40, "D"),
    ("24/09", "Exames particulares (balcão)", "Dinheiro", 930.00, "C"),
    ("25/09", "Repasse convênio Unividas (ref. agosto)", "Transferência", 12308.60, "C"),
    ("26/09", "Água e esgoto", "Débito automático", 214.37, "D"),
    ("29/09", "Exames particulares (balcão)", "Pix", 2205.00, "C"),
    ("30/09", "Contador (honorários)", "Pix", 850.00, "D"),
]

MARINHO = colors.HexColor("#1F2A44")
CINZA = colors.HexColor("#5A6478")
FAIXA = colors.HexColor("#F3F5F9")


def reais(centavos):
    inteiro, resto = divmod(centavos, 100)
    return f"{inteiro:,}".replace(",", ".") + f",{resto:02d}"


def gerar():
    largura, altura = A4
    margem = 16 * mm
    pdf = canvas.Canvas(str(SAIDA), pagesize=A4)
    pdf.setTitle("Relatório de movimentação financeira")
    pdf.setAuthor(LABORATORIO)

    # Cabeçalho
    y = altura - margem
    pdf.setFillColor(MARINHO)
    pdf.setFont("Helvetica-Bold", 15)
    pdf.drawString(margem, y - 12, LABORATORIO)
    pdf.setFillColor(CINZA)
    pdf.setFont("Helvetica", 9)
    pdf.drawString(margem, y - 26, f"CNPJ {CNPJ}   |   {ENDERECO}")
    pdf.drawRightString(largura - margem, y - 12, f"Emitido em {EMISSAO}")
    pdf.drawRightString(largura - margem, y - 26, "Página 1 de 1")
    pdf.setStrokeColor(MARINHO)
    pdf.setLineWidth(1.2)
    pdf.line(margem, y - 34, largura - margem, y - 34)

    pdf.setFillColor(MARINHO)
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(margem, y - 54, "Relatório de movimentação financeira")
    pdf.setFillColor(CINZA)
    pdf.setFont("Helvetica", 10)
    pdf.drawString(margem, y - 69, f"Período: {PERIODO}   |   C = crédito (entrada)   D = débito (saída)")

    # Tabela de lançamentos
    entradas = saidas = 0
    linhas = [["Data", "Descrição", "Forma de pagamento", "Valor (R$)", ""]]
    for data, descricao, forma, valor, tipo in LANCAMENTOS:
        centavos = round(valor * 100)
        if tipo == "C":
            entradas += centavos
        else:
            saidas += centavos
        linhas.append([data, descricao, forma, reais(centavos), tipo])

    util = largura - 2 * margem
    colunas = [16 * mm, 0, 40 * mm, 26 * mm, 8 * mm]
    colunas[1] = util - sum(colunas)
    tabela = Table(linhas, colWidths=colunas, rowHeights=19)
    tabela.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 9.5),
        ("FONT", (0, 1), (-1, -1), "Helvetica", 9.5),
        ("BACKGROUND", (0, 0), (-1, 0), MARINHO),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#1A1A1A")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, FAIXA]),
        ("ALIGN", (3, 0), (3, -1), "RIGHT"),
        ("ALIGN", (4, 0), (4, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, MARINHO),
    ]))
    _, altura_tabela = tabela.wrap(util, altura)
    topo_tabela = y - 82
    tabela.drawOn(pdf, margem, topo_tabela - altura_tabela)

    # Totais
    y = topo_tabela - altura_tabela - 22
    direita = largura - margem - colunas[4]
    for rotulo, valor, negrito in [
        ("Total de entradas (C)", reais(entradas), False),
        ("Total de saídas (D)", reais(saidas), False),
        ("Saldo do período", reais(entradas - saidas), True),
    ]:
        pdf.setFillColor(MARINHO)
        pdf.setFont("Helvetica-Bold" if negrito else "Helvetica", 11)
        pdf.drawRightString(direita - 34 * mm, y, rotulo)
        pdf.drawRightString(direita, y, "R$ " + valor)
        y -= 17

    # Rodapé
    pdf.setFillColor(CINZA)
    pdf.setFont("Helvetica-Oblique", 8)
    pdf.drawCentredString(
        largura / 2, margem - 4,
        "Documento fictício para demonstração. Empresa, convênios e valores inventados.",
    )

    pdf.showPage()
    pdf.save()
    print(f"{SAIDA.name}: {len(LANCAMENTOS)} lançamentos, "
          f"entradas R$ {reais(entradas)}, saídas R$ {reais(saidas)}, "
          f"saldo R$ {reais(entradas - saidas)}")


if __name__ == "__main__":
    gerar()
