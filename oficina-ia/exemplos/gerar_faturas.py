#!/usr/bin/env python3
"""Gera o segundo PDF de exemplo do exercício 1 (slide `exercicio1-faturas`).

Uma fatura por página, 25 páginas, cada uma de um cliente inventado.
Para mudar, edite CLIENTES ou EXAMES e rode:

    python3 gerar_faturas.py

Os itens de cada fatura são sorteados com semente fixa: rodar de novo dá o
mesmo PDF. Precisa do reportlab (pip install reportlab).
"""
import random
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

SAIDA = Path(__file__).with_name("faturas-clientes.pdf")

LABORATORIO = "Laboratório Vida Clara Análises Clínicas Veterinárias Ltda."
CNPJ = "00.000.000/0001-00"
ENDERECO = "Rua das Acácias, 123, Centro"
RODAPE = "Documento fictício para demonstração. Empresa, clientes e valores inventados."

# (cliente, documento, cidade)
CLIENTES = [
    ("Clínica Veterinária Patas Felizes", "CNPJ 11.111.111/0001-11", "Campinas/SP"),
    ("Mariana Albuquerque Teles", "CPF ***.482.917-**", "Campinas/SP"),
    ("Pet Shop Bicho Mimado", "CNPJ 22.222.222/0001-22", "Valinhos/SP"),
    ("Rogério Siqueira Pontes", "CPF ***.105.336-**", "Campinas/SP"),
    ("Hospital Veterinário São Lázaro", "CNPJ 33.333.333/0001-33", "Sumaré/SP"),
    ("Helena Duarte Figueiró", "CPF ***.774.208-**", "Vinhedo/SP"),
    ("Clínica Vet Quatro Patas", "CNPJ 44.444.444/0001-44", "Hortolândia/SP"),
    ("Tiago Bernardes Lacerda", "CPF ***.960.451-**", "Campinas/SP"),
    ("Consultório Veterinário Dra. Íris Camargo", "CNPJ 55.555.555/0001-55", "Paulínia/SP"),
    ("Sueli Monteiro Prado", "CPF ***.318.642-**", "Valinhos/SP"),
    ("Canil Recanto dos Pastores", "CNPJ 66.666.666/0001-66", "Indaiatuba/SP"),
    ("Fábio Coutinho Arantes", "CPF ***.527.089-**", "Sumaré/SP"),
    ("Clínica Veterinária Amigo Fiel", "CNPJ 77.777.777/0001-77", "Campinas/SP"),
    ("Beatriz Nogueira Salles", "CPF ***.641.193-**", "Campinas/SP"),
    ("Gatil Bigodes de Ouro", "CNPJ 88.888.888/0001-88", "Vinhedo/SP"),
    ("Otávio Rezende Cardim", "CPF ***.209.875-**", "Paulínia/SP"),
    ("Pet Center Mundo Animal", "CNPJ 99.999.999/0001-99", "Hortolândia/SP"),
    ("Luciana Farias Bittencourt", "CPF ***.853.460-**", "Indaiatuba/SP"),
    ("Clínica Veterinária Focinho Gelado", "CNPJ 12.121.212/0001-12", "Campinas/SP"),
    ("Wagner Tavares Meireles", "CPF ***.436.721-**", "Valinhos/SP"),
    ("ONG Lar dos Peludos", "CNPJ 23.232.323/0001-23", "Sumaré/SP"),
    ("Cecília Antunes Brandão", "CPF ***.792.158-**", "Campinas/SP"),
    ("Centro Veterinário Vida Animal", "CNPJ 34.343.434/0001-34", "Paulínia/SP"),
    ("Edson Vasconcelos Lima", "CPF ***.064.983-**", "Hortolândia/SP"),
    ("Clínica Veterinária Bem-Te-Vi", "CNPJ 45.454.545/0001-45", "Vinhedo/SP"),
]

# (exame, preço unitário em reais)
EXAMES = [
    ("Hemograma completo", 45.00),
    ("Perfil bioquímico renal", 68.00),
    ("Perfil bioquímico hepático", 72.00),
    ("Urinálise", 38.00),
    ("Parasitológico de fezes", 32.00),
    ("Citologia de pele", 55.00),
    ("Cultura e antibiograma", 120.00),
    ("Glicemia", 22.00),
    ("Teste rápido de cinomose", 85.00),
    ("Teste rápido FIV/FeLV", 110.00),
    ("Sorologia para leishmaniose", 135.00),
    ("Histopatológico", 180.00),
    ("Pesquisa de hemoparasitas", 48.00),
    ("T4 total", 95.00),
]

FORMAS = ["Pix", "Boleto", "Cartão de crédito", "Cartão de débito", "Transferência", "Dinheiro"]

MARINHO = colors.HexColor("#1F2A44")
CINZA = colors.HexColor("#5A6478")
FAIXA = colors.HexColor("#F3F5F9")
PRETO = colors.HexColor("#1A1A1A")


def reais(centavos):
    inteiro, resto = divmod(centavos, 100)
    return f"{inteiro:,}".replace(",", ".") + f",{resto:02d}"


def montar_faturas():
    sorteio = random.Random(2026)
    faturas = []
    for i, (cliente, documento, cidade) in enumerate(CLIENTES):
        empresa = documento.startswith("CNPJ")
        dia = 1 + (i * 29) // len(CLIENTES)
        vencimento = dia + 10
        itens = []
        for exame, preco in sorteio.sample(EXAMES, sorteio.randint(2, 5)):
            qtd = sorteio.randint(2, 12) if empresa else 1
            itens.append((exame, qtd, round(preco * 100)))
        faturas.append({
            "numero": f"2026-{901 + i:04d}",
            "emissao": f"{dia:02d}/09/2026",
            "vencimento": f"{vencimento:02d}/09/2026" if vencimento <= 30 else f"{vencimento - 30:02d}/10/2026",
            "cliente": cliente,
            "documento": documento,
            "cidade": cidade,
            "telefone": f"(19) 90000-{sorteio.randint(0, 9999):04d}",
            "itens": itens,
            "total": sum(qtd * preco for _, qtd, preco in itens),
            "forma": sorteio.choice(FORMAS),
            # Quem não pagou: vencida se o vencimento caiu em setembro, senão em aberto.
            "situacao": "Paga" if sorteio.random() < 0.65 else ("Vencida" if vencimento <= 30 else "Em aberto"),
        })
    return faturas


def desenhar(pdf, fatura, pagina, paginas):
    largura, altura = A4
    margem = 18 * mm
    util = largura - 2 * margem
    y = altura - margem

    # Cabeçalho do laboratório
    pdf.setFillColor(MARINHO)
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(margem, y - 12, LABORATORIO)
    pdf.setFillColor(CINZA)
    pdf.setFont("Helvetica", 9)
    pdf.drawString(margem, y - 26, f"CNPJ {CNPJ}   |   {ENDERECO}")
    pdf.setStrokeColor(MARINHO)
    pdf.setLineWidth(1.2)
    pdf.line(margem, y - 34, largura - margem, y - 34)

    # Título e datas
    pdf.setFillColor(MARINHO)
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(margem, y - 66, f"Fatura nº {fatura['numero']}")
    pdf.setFont("Helvetica", 11)
    pdf.setFillColor(PRETO)
    pdf.drawRightString(largura - margem, y - 56, f"Emissão: {fatura['emissao']}")
    pdf.drawRightString(largura - margem, y - 72, f"Vencimento: {fatura['vencimento']}")

    # Dados do cliente
    topo = y - 92
    pdf.setFillColor(FAIXA)
    pdf.roundRect(margem, topo - 74, util, 74, 6, stroke=0, fill=1)
    pdf.setFillColor(CINZA)
    pdf.setFont("Helvetica-Bold", 8.5)
    pdf.drawString(margem + 12, topo - 17, "CLIENTE")
    pdf.setFillColor(PRETO)
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(margem + 12, topo - 35, fatura["cliente"])
    pdf.setFont("Helvetica", 10.5)
    pdf.drawString(margem + 12, topo - 51, fatura["documento"])
    pdf.drawString(margem + 12, topo - 65, f"{fatura['cidade']}   |   Telefone: {fatura['telefone']}")

    # Itens
    linhas = [["Exame", "Qtd.", "Valor unit. (R$)", "Subtotal (R$)"]]
    for exame, qtd, preco in fatura["itens"]:
        linhas.append([exame, str(qtd), reais(preco), reais(qtd * preco)])
    colunas = [0, 18 * mm, 36 * mm, 36 * mm]
    colunas[0] = util - sum(colunas)
    tabela = Table(linhas, colWidths=colunas, rowHeights=24)
    tabela.setStyle(TableStyle([
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 10.5),
        ("FONT", (0, 1), (-1, -1), "Helvetica", 11),
        ("BACKGROUND", (0, 0), (-1, 0), MARINHO),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("TEXTCOLOR", (0, 1), (-1, -1), PRETO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, FAIXA]),
        ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, MARINHO),
    ]))
    _, altura_tabela = tabela.wrap(util, altura)
    topo_tabela = topo - 96
    tabela.drawOn(pdf, margem, topo_tabela - altura_tabela)

    # Total e pagamento
    y = topo_tabela - altura_tabela - 30
    pdf.setFillColor(MARINHO)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawRightString(largura - margem - 40 * mm, y, "Total da fatura")
    pdf.drawRightString(largura - margem - 6, y, "R$ " + reais(fatura["total"]))
    pdf.setFillColor(PRETO)
    pdf.setFont("Helvetica", 11)
    pdf.drawString(margem, y - 36, f"Forma de pagamento: {fatura['forma']}")
    pdf.drawString(margem, y - 53, f"Situação: {fatura['situacao']}")

    # Rodapé
    pdf.setFillColor(CINZA)
    pdf.setFont("Helvetica-Oblique", 8)
    pdf.drawString(margem, margem - 4, RODAPE)
    pdf.drawRightString(largura - margem, margem - 4, f"Página {pagina} de {paginas}")
    pdf.showPage()


def gerar():
    faturas = montar_faturas()
    pdf = canvas.Canvas(str(SAIDA), pagesize=A4)
    pdf.setTitle("Faturas de clientes, setembro de 2026")
    pdf.setAuthor(LABORATORIO)
    for pagina, fatura in enumerate(faturas, start=1):
        desenhar(pdf, fatura, pagina, len(faturas))
    pdf.save()
    total = sum(f["total"] for f in faturas)
    itens = sum(len(f["itens"]) for f in faturas)
    print(f"{SAIDA.name}: {len(faturas)} faturas, {itens} itens, soma dos totais R$ {reais(total)}")


if __name__ == "__main__":
    gerar()
