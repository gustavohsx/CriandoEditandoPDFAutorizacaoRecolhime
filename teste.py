from template import Template

lista = [
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU'],
    ['UUUUUUUUU', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'UUUUUUUU', 'UUUUUUUUUUUUUU']
]
print(len(lista[0][0]))
print(len(lista[0][1]))
print(len(lista[0][2]))
print(len(lista[0][3]))
informacoes = {
    'numero':'021',
    'n_pedido': '98745126 / 54879546',
    'data_carta': '18/15/2023',
    'cod_rca': '125',
    'nome_rca': 'Jose Maluquinho / Jose Maluquinho',
    'n_nf': '548796',
    'cod_cliente': '45687',
    'r_social': 'Jose da Silva',
    'fantasia': 'Mercado da Maria',
    'endereco': 'Rua Angelo Tavares Manoel , 143',
    'bairro': 'baixao',
    'praca': 'Praca',
    'cidade': 'Arapiraca',
    'rota': '7 - Arapiraca'
}

pdf = Template('./imagens', 'teste_pdf')

pdf.desenharInformacoes(informacoes)
pdf.desenharProdutos(lista)

pdf.salvarPDF()