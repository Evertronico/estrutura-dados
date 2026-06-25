# Script auxiliar que gera o relatório técnico em PDF (RELATORIO.pdf).
# Executar: python gerar_relatorio.py
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, ListFlowable, ListItem)

styles = getSampleStyleSheet()

titulo = ParagraphStyle("titulo", parent=styles["Title"], fontSize=20,
                        textColor=colors.HexColor("#0B5345"), spaceAfter=4)
subtitulo = ParagraphStyle("subtitulo", parent=styles["Normal"], fontSize=11,
                           alignment=TA_CENTER, textColor=colors.grey, spaceAfter=18)
h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=14,
                    textColor=colors.HexColor("#117A65"), spaceBefore=14, spaceAfter=6)
h3 = ParagraphStyle("h3", parent=styles["Heading3"], fontSize=12,
                    textColor=colors.HexColor("#1A5276"), spaceBefore=8, spaceAfter=4)
corpo = ParagraphStyle("corpo", parent=styles["Normal"], fontSize=10.5,
                       alignment=TA_JUSTIFY, leading=15, spaceAfter=6)
item = ParagraphStyle("item", parent=corpo, spaceAfter=2)


def bullets(textos):
    return ListFlowable(
        [ListItem(Paragraph(t, item), leftIndent=10) for t in textos],
        bulletType="bullet", start="•", leftIndent=14)


story = []
story.append(Paragraph("Relatório do projeto", titulo))
story.append(Paragraph("Sistema de Delivery — Projeto de Estrutura de Dados", subtitulo))

info = Table([
    ["Aluno", "Daniel Queiroz Soares"],
    ["Disciplina", "Estrutura de Dados"],
    ["Tema", "Sistema de Delivery"]
], colWidths=[4*cm, 11*cm])
info.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#D5F5E3")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#A9DFBF")),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(info)
story.append(Spacer(1, 14))

# 1. Descrição do sistema
story.append(Paragraph("1. Descrição do Sistema", h2))
story.append(Paragraph(
    "O sistema desenvolvido é um <b>gerenciador de delivery</b> (entrega de comida), "
    "que resolve um problema real enfrentado por restaurantes e lanchonetes: "
    "<b>organizar o cadastro de clientes, o cardápio de produtos, a ordem de preparo "
    "dos pedidos e o histórico de entregas</b> de forma justa e rastreável.", corpo))
story.append(Paragraph(
    "Na prática, quando um restaurante recebe vários pedidos ao mesmo tempo, precisa "
    "garantir que sejam preparados na ordem de chegada, acompanhar a evolução do status "
    "de cada pedido (e poder desfazer um status lançado por engano) e consultar pedidos "
    "antigos navegando para frente e para trás. Cada uma dessas necessidades foi mapeada "
    "para a estrutura de dados mais adequada, estudada nas aulas 1 a 9.", corpo))
story.append(Paragraph(
    "O projeto é totalmente <b>modularizado</b>: a pasta <font face='Courier'>modelos/</font> "
    "guarda as classes de dados (Cliente, Produto, Pedido); a pasta "
    "<font face='Courier'>estruturas/</font> contém as cinco estruturas de dados; a pasta "
    "<font face='Courier'>sistema/</font> reúne as regras de negócio; e o "
    "<font face='Courier'>main.py</font> apresenta o menu interativo.", corpo))

# 2. Estruturas utilizadas
story.append(Paragraph("2. Estruturas Utilizadas", h2))

story.append(Paragraph("Lista Sequencial — Cadastro de Clientes", h3))
story.append(Paragraph(
    "Os clientes são armazenados em uma <b>lista sequencial</b> "
    "(<font face='Courier'>ListaSequencialClientes</font>), em que os elementos ficam "
    "em posições contíguas. <b>Por quê:</b> o cadastro de clientes é majoritariamente "
    "acessado por consulta direta e percorrido por completo nas listagens; a lista "
    "sequencial é simples, ocupa pouca memória extra e oferece inserção rápida no final. "
    "A remoção foi implementada manualmente com o deslocamento dos elementos, "
    "demonstrando o funcionamento interno da estrutura.", corpo))

story.append(Paragraph("Lista Encadeada — Cardápio de Produtos", h3))
story.append(Paragraph(
    "O cardápio usa uma <b>lista encadeada simples</b> "
    "(<font face='Courier'>Cardapio</font> + classe <font face='Courier'>No</font>), na "
    "qual cada produto fica em um nó que aponta para o próximo. <b>Por quê:</b> o cardápio "
    "muda com frequência (itens entram e saem); na lista encadeada a inserção e a remoção "
    "não exigem deslocar todos os elementos como na lista sequencial — basta religar os "
    "ponteiros, tornando essas operações mais flexíveis.", corpo))

story.append(Paragraph("Lista Duplamente Encadeada — Histórico de Pedidos", h3))
story.append(Paragraph(
    "Os pedidos já entregues vão para o <b>histórico</b> "
    "(<font face='Courier'>HistoricoPedidos</font>), uma lista duplamente encadeada em que "
    "cada nó aponta para o próximo <b>e</b> para o anterior. <b>Por quê:</b> permite "
    "<b>navegar para frente e para trás</b> entre os pedidos (como botões "
    "“próximo/anterior”), algo impossível na lista simples, ideal para o operador revisar "
    "o histórico em qualquer direção.", corpo))

story.append(Paragraph("Pilha — Status do Pedido (desfazer)", h3))
story.append(Paragraph(
    "Cada pedido guarda seu histórico de status em uma <b>pilha</b> "
    "(<font face='Courier'>Pilha</font>, padrão LIFO). O topo é sempre o status atual. "
    "<b>Por quê:</b> a regra de “<b>desfazer o último status</b>” segue a lógica do último "
    "que entra ser o primeiro a sair: se um status foi lançado por engano, basta "
    "desempilhar para voltar ao anterior. As operações empilhar, desempilhar e topo "
    "modelam isso de forma natural.", corpo))

story.append(Paragraph("Fila — Pedidos em Preparo", h3))
story.append(Paragraph(
    "Os pedidos recebidos entram em uma <b>fila</b> (<font face='Courier'>Fila</font>, "
    "padrão FIFO). <b>Por quê:</b> em um delivery, o <b>primeiro pedido a chegar deve ser "
    "o primeiro a ser preparado</b>. A fila garante essa ordem justa de atendimento com "
    "as operações enfileirar, desenfileirar e consulta do primeiro elemento.", corpo))

# 3. Complexidade
story.append(Paragraph("3. Complexidade", h2))
story.append(Paragraph(
    "A notação Big-O abaixo descreve como o tempo de execução cresce conforme aumenta a "
    "quantidade <b>n</b> de elementos.", corpo))

tabela = Table([
    ["Operação", "Lista Sequencial", "Lista Encadeada", "Lista Dupla", "Pilha", "Fila"],
    ["Inserção", "O(1) no final", "O(n) no final*", "O(1) no final", "O(1)", "O(1)"],
    ["Busca", "O(n)", "O(n)", "O(n)", "O(n)", "O(n)"],
    ["Remoção", "O(n)", "O(n)", "O(1) nas pontas", "O(1) topo", "O(n) início**"],
], colWidths=[2.6*cm, 3.0*cm, 2.9*cm, 2.6*cm, 1.9*cm, 2.0*cm])
tabela.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#117A65")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#A9DFBF")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EAFAF1")]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(tabela)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<font size=8>* Na implementação, a inserção no final percorre a lista até o último nó. "
    "** A remoção no início da fila desloca os demais elementos.</font>", item))

story.append(Paragraph("Inserção", h3))
story.append(bullets([
    "<b>Lista sequencial:</b> inserir no final é O(1), pois apenas ocupa a próxima posição livre.",
    "<b>Lista encadeada / dupla:</b> criar o nó é O(1); como inserimos no final, percorrer até o "
    "último nó custa O(n) (na lista dupla usamos a referência <i>tail</i>, tornando-a O(1)).",
    "<b>Pilha e fila:</b> empilhar e enfileirar são O(1), pois sempre atuam em uma das pontas.",
]))

story.append(Paragraph("Busca", h3))
story.append(bullets([
    "Em todas as estruturas a busca é <b>sequencial</b>: percorre elemento por elemento "
    "comparando a chave (id/código), portanto O(n) no pior caso.",
    "Pilha e fila normalmente não são usadas para busca, mas consultar o topo/primeiro é O(1).",
]))

story.append(Paragraph("Remoção", h3))
story.append(bullets([
    "<b>Lista sequencial:</b> O(n) — após achar o elemento, é preciso deslocar os seguintes "
    "uma posição para trás.",
    "<b>Lista encadeada:</b> O(n) para localizar; religar o ponteiro é O(1).",
    "<b>Lista dupla:</b> com o nó em mãos, a remoção é O(1) (ajusta anterior/próximo); "
    "remover nas pontas é direto.",
    "<b>Pilha:</b> desempilhar (remover o topo) é O(1).",
    "<b>Fila:</b> desenfileirar remove o primeiro; nesta implementação custa O(n) pelo "
    "deslocamento, mantendo a ordem FIFO."
]))

doc = SimpleDocTemplate("RELATORIO.pdf", pagesize=A4,
                        leftMargin=2*cm, rightMargin=2*cm,
                        topMargin=2*cm, bottomMargin=2*cm,
                        title="Relatório Técnico - Sistema de Delivery",
                        author="Daniel Queiroz")
doc.build(story)
print("RELATORIO.pdf gerado com sucesso.")
