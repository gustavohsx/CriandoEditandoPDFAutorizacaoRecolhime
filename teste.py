from template import Template

lista = [
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76GBISC RECH PIRACHE ', 'UUUUUUUUUU', 'ESTOQUE EM OBSERVAÇÃO'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'MERCADORIA AVARIADA NA ENTREGA'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'BISC RECH PIRACHE PRETTY 5X76G', 'UUUUUUUU', 'UUUUUUUUUUUUUU']
]

informacoes = {
    'numero':'021',
    'n_pedido': '373021447 / 9461000686 /',
    'data_carta': '18/15/2023',
    'cod_rca': '373 / 946 /',
    'nome_rca': 'AUDALIANO ',
    'n_nf': '2556818 / 2484222 /',
    'cod_cliente': '45687',
    'r_social': 'SONIA MARIA DOS SANTOS 88855414453',
    'fantasia': 'SUPERMERCADO SANTA ROSA',
    'endereco': 'AV PIO XII ',
    'bairro': 'PLANALTO',
    'praca': 'ARAP PLANALTO',
    'cidade': 'Arapiraca',
    'rota': '7 - Arapiraca'
}

for chave in informacoes:
    print(chave, len(informacoes[chave]))

pdf = Template('./imagens', 'teste_pdf')

pdf.desenharInformacoes(informacoes)
pdf.desenharProdutos(lista)

pdf.salvarPDF()