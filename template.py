from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Template:
        
    def __init__(self, local_salvamento, nome_arquivo):
        self.pdf = canvas.Canvas(f"{local_salvamento}/{nome_arquivo}.pdf", pagesize=A4)
        self.pdf.setTitle(nome_arquivo)
        self._desenharItensPadrao()

    def desenharInformacoes(self, informacoes):
        self.pdf.setFont('Helvetica-Bold', 11)
        self.pdf.drawString(122, 660, informacoes['numero'])
        self.pdf.drawString(412, 660, informacoes['data_carta'])
        self.pdf.drawString(122, 640, informacoes['n_pedido'])
        self.pdf.drawString(412, 640, informacoes['n_nf'])
        self.pdf.drawString(122, 620, informacoes['cod_rca'])
        self.pdf.drawString(412, 620, informacoes['nome_rca'])
        self.pdf.drawString(122, 600, informacoes['cod_cliente'])
        self.pdf.drawString(122, 580, informacoes['r_social'])
        self.pdf.drawString(122, 560, informacoes['fantasia'])
        self.pdf.drawString(122, 540, informacoes['endereco'])
        self.pdf.drawString(122, 520, informacoes['bairro'])
        self.pdf.drawString(412, 520, informacoes['cidade'])
        self.pdf.drawString(122, 500, informacoes['praca'])
        self.pdf.drawString(412, 500, informacoes['rota'])
    
    def desenharProdutos(self, lista_produtos):
        """
            Quantidade de Caracteres por coluna com fonte tamanho 10 negrito maiusculo:
            Codigo: 9
            Descricao: 33
            QT: 8
            Motivo: 14

            Quantidade de Caracteres por coluna com fonte tamanho 9 negrito maiusculo:
            Codigo: 10
            Descricao: 36
            QT: 9
            Motivo: 16
        """
        x = [82, 152, 392, 452]
        y = 385
        self.pdf.setFont('Helvetica-Bold', 10)
        for produto in lista_produtos:
            self.pdf.drawString(x[0], y, f'{produto[0]}')
            self.pdf.drawString(x[1], y, f'{produto[1]}')
            self.pdf.drawString(x[2], y, f'{produto[2]}')
            self.pdf.drawString(x[3], y, f'{produto[3]}')
            y -= 20
    
    def _desenharItensPadrao(self):
        linhas = [(40, 420, 555, 420),
                (40, 400, 555, 400),
                (40, 380, 555, 380),
                (40, 360, 555, 360),
                (40, 340, 555, 340),
                (40, 320, 555, 320),
                (40, 300, 555, 300),
                (40, 280, 555, 280),
                (40, 260, 555, 260),
                (40, 240, 555, 240),
                (40, 220, 555, 220),
                (40, 200, 555, 200),
                (40, 420, 40, 200),
                (80, 420, 80, 200),
                (150, 420, 150, 200),
                (390, 420, 390, 200),
                (450, 420, 450, 200),
                (555, 420, 555, 200)]

        self.pdf.drawImage('./imagens/logo.jpeg', 35, 730, 100, 100)

        self.pdf.setFont('Helvetica-Bold', 18)
        self.pdf.drawString(140, 700, 'AUTORIZAÇÃO DE RECOLHIMENTO')
        self.pdf.line(140, 697, 452, 697)

        self.pdf.setFont('Helvetica', 12)
        self.pdf.drawString(35, 660, 'NÚMERO: ')
        self.pdf.drawString(35, 640, 'N° PEDIDO: ')
        self.pdf.drawString(35, 620, 'COD RCA: ')
        self.pdf.drawString(35, 600, 'COD CLIENTE: ')
        self.pdf.drawString(35, 580, 'R. SOCIAL: ')
        self.pdf.drawString(35, 560, 'FANTASIA: ')
        self.pdf.drawString(35, 540, 'ENDEREÇO: ')
        self.pdf.drawString(35, 520, 'BAIRRO: ')
        self.pdf.drawString(35, 500, 'PRAÇA: ')
        self.pdf.drawString(330, 660, 'DATA CARTA: ')
        self.pdf.drawString(372, 640, 'N° NF: ')
        self.pdf.drawString(340, 620, 'NOME RCA: ')
        self.pdf.drawString(360, 520, 'CIDADE: ')
        self.pdf.drawString(372, 500, 'ROTA: ')

        self.pdf.setFont('Helvetica-Bold', 12)
        self.pdf.drawString(35, 440, 'O CLIENTE ALEGA TER EM SEU ESTABELECIMENTO OS ITENS ABAIXO RELACIONADOS:')

        self.pdf.drawString(53, 405, 'ID')
        self.pdf.drawString(93, 405, 'CÓDIGO')
        self.pdf.drawString(240, 405, 'DESCRIÇÃO')
        self.pdf.drawString(415, 405, 'QT')
        self.pdf.drawString(480, 405, 'MOTIVO')

        self.pdf.setFont('Helvetica', 12)
        self.pdf.drawString(56, 385, '1')
        self.pdf.drawString(56, 365, '2')
        self.pdf.drawString(56, 345, '3')
        self.pdf.drawString(56, 325, '4')
        self.pdf.drawString(56, 305, '5')
        self.pdf.drawString(56, 285, '6')
        self.pdf.drawString(56, 265, '7')
        self.pdf.drawString(56, 245, '8')
        self.pdf.drawString(56, 225, '9')
        self.pdf.drawString(53, 205, '10')

        self.pdf.lines(linhas)

        self.pdf.line(60, 120, 255, 120)
        self.pdf.drawString(120, 100, 'Ass. Motorista')
        self.pdf.line(340, 120, 535, 120)
        self.pdf.drawString(405, 100, 'Ass. Cliente')

    def salvarPDF(self):
        self.pdf.save()