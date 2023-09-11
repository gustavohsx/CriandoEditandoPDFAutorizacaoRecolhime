from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Template:
        
    def __init__(self, local_salvamento, nome_arquivo):
        self.pdf = canvas.Canvas(f"{local_salvamento}/{nome_arquivo}.pdf", pagesize=A4)
        self.pdf.setTitle(nome_arquivo)
        self._desenharItensPadrao()

    def desenharInformacoes(self, informacoes):
        limite_esquerdo = 34
        limite_direito = 24
        quebra_linha_limite = 9

        if len(informacoes['numero']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 660, informacoes['numero'][:limite_esquerdo])
            self.pdf.drawString(107, 660-quebra_linha_limite, informacoes['numero'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 660, informacoes['numero'])

        if len(informacoes['data_carta']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 660, informacoes['data_carta'][:limite_direito])
            self.pdf.drawString(403, 660-quebra_linha_limite, informacoes['data_carta'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 660, informacoes['data_carta'])

        if len(informacoes['n_pedido']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 640, informacoes['n_pedido'][:limite_esquerdo])
            self.pdf.drawString(107, 640-quebra_linha_limite, informacoes['n_pedido'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 640, informacoes['n_pedido'])

        if len(informacoes['n_nf']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 640, informacoes['n_nf'][:limite_direito])
            self.pdf.drawString(403, 640-quebra_linha_limite, informacoes['n_nf'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 640, informacoes['n_nf'])
        
        if len(informacoes['cod_rca']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 615, informacoes['cod_rca'][:limite_esquerdo])
            self.pdf.drawString(107, 615-quebra_linha_limite, informacoes['cod_rca'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 615, informacoes['cod_rca'])
        
        if len(informacoes['nome_rca']) > limite_direito*2:
            # partes = []
            y = 615
            self.pdf.setFont('Helvetica-Bold', 10)
            limite_direito += 2
            for i in range(0, len(informacoes['nome_rca']), limite_direito):
                # partes.append(informacoes['nome_rca'][i:i+limite_direito])
                self.pdf.drawString(403, y, informacoes['nome_rca'][i:i+limite_direito])
                y -= quebra_linha_limite
        elif len(informacoes['nome_rca']) > limite_direito:
            limite_direito += 2
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 615, informacoes['nome_rca'][:limite_direito])
            self.pdf.drawString(403, 615-quebra_linha_limite, informacoes['nome_rca'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 615, informacoes['nome_rca'])
        
        if len(informacoes['cod_cliente']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 590, informacoes['cod_cliente'][:limite_esquerdo])
            self.pdf.drawString(107, 590-quebra_linha_limite, informacoes['cod_cliente'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 590, informacoes['cod_cliente'])
        
        if len(informacoes['r_social']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 565, informacoes['r_social'][:limite_esquerdo])
            self.pdf.drawString(107, 565-quebra_linha_limite, informacoes['r_social'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 565, informacoes['r_social'])

        if len(informacoes['fantasia']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 540, informacoes['fantasia'][:limite_esquerdo])
            self.pdf.drawString(107, 540-quebra_linha_limite, informacoes['fantasia'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 540, informacoes['fantasia'])

        if len(informacoes['endereco']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 515, informacoes['endereco'][:limite_esquerdo])
            self.pdf.drawString(107, 515-quebra_linha_limite, informacoes['endereco'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 515, informacoes['endereco'])

        if len(informacoes['bairro']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 490, informacoes['bairro'][:limite_esquerdo])
            self.pdf.drawString(107, 490-quebra_linha_limite, informacoes['bairro'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 490, informacoes['bairro'])

        if len(informacoes['cidade']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 490, informacoes['cidade'][:limite_direito])
            self.pdf.drawString(403, 490-quebra_linha_limite, informacoes['cidade'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 490, informacoes['cidade'])

        if len(informacoes['praca']) > limite_esquerdo:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(107, 470, informacoes['praca'][:limite_esquerdo])
            self.pdf.drawString(107, 470-quebra_linha_limite, informacoes['praca'][limite_esquerdo:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(107, 470, informacoes['praca'])
        
        if len(informacoes['rota']) > limite_direito:
            self.pdf.setFont('Helvetica-Bold', 10)
            self.pdf.drawString(403, 470, informacoes['rota'][:limite_direito])
            self.pdf.drawString(403, 470-quebra_linha_limite, informacoes['rota'][limite_direito:])
        else:
            self.pdf.setFont('Helvetica-Bold', 11)
            self.pdf.drawString(403, 470, informacoes['rota'])
    
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
        self.pdf.setFont('Helvetica-Bold', 8)
        for produto in lista_produtos:
            if len(produto[0]) > 11:
                self.pdf.drawString(x[0], y, f'{produto[0][:11]}')
                self.pdf.drawString(x[0], y-10, f'{produto[0][11:]}')
            else:
                self.pdf.drawString(x[0], y, f'{produto[0]}')
            if len(produto[1]) > 49:
                self.pdf.drawString(x[1], y, f'{produto[1][:49]}')
                self.pdf.drawString(x[1], y-10, f'{produto[1][49:]}')
            else:
                self.pdf.drawString(x[1], y, f'{produto[1]}')
            if len(produto[2]) > 9:
                self.pdf.drawString(x[2], y, f'{produto[2][:9]}')
                self.pdf.drawString(x[2], y-10, f'{produto[2][9:]}')
            else:
                self.pdf.drawString(x[2], y, f'{produto[2]}')
            if len(produto[3]) > 19:
                self.pdf.drawString(x[3], y, f'{produto[3][:19]}')
                self.pdf.drawString(x[3], y-10, f'{produto[3][19:]}')
            else:
                self.pdf.drawString(x[3], y, f'{produto[3]}')
            y -= 25
    
    def _desenharItensPadrao(self):
        # linhas = [(40, 420, 555, 420),
        #         (40, 395, 555, 395),
        #         (40, 370, 555, 370),
        #         (40, 355, 555, 355),
        #         (40, 330, 555, 330),
        #         (40, 305, 555, 305),
        #         (40, 280, 555, 280),
        #         (40, 255, 555, 255),
        #         (40, 230, 555, 230),
        #         (40, 205, 555, 205),
        #         (40, 180, 555, 180),
        #         (40, 155, 555, 155),
        #         (40, 420, 40, 155),
        #         (80, 420, 80, 155),
        #         (150, 420, 150, 155),
        #         (390, 420, 390, 155),
        #         (450, 420, 450, 155),
        #         (555, 420, 555, 155)]

        self.pdf.drawImage('./imagens/logo.jpeg', 35, 730, 100, 100)

        self.pdf.setFont('Helvetica-Bold', 18)
        self.pdf.drawString(140, 700, 'AUTORIZAÇÃO DE RECOLHIMENTO')
        self.pdf.line(140, 697, 452, 697)

        self.pdf.setFont('Helvetica', 10)
        self.pdf.drawString(35, 660, 'NÚMERO: ')
        self.pdf.drawString(35, 640, 'N° PEDIDO: ')
        self.pdf.drawString(35, 615, 'COD RCA: ')
        self.pdf.drawString(35, 590, 'COD CLIENTE: ')
        self.pdf.drawString(35, 565, 'R. SOCIAL: ')
        self.pdf.drawString(35, 540, 'FANTASIA: ')
        self.pdf.drawString(35, 515, 'ENDEREÇO: ')
        self.pdf.drawString(35, 490, 'BAIRRO: ')
        self.pdf.drawString(35, 470, 'PRAÇA: ')
        self.pdf.drawString(335, 660, 'DATA CARTA: ')
        self.pdf.drawString(372, 640, 'N° NF: ')
        self.pdf.drawString(345, 615, 'NOME RCA: ')
        self.pdf.drawString(362, 490, 'CIDADE: ')
        self.pdf.drawString(372, 470, 'ROTA: ')

        self.pdf.setFont('Helvetica-Bold', 12)
        self.pdf.drawString(35, 440, 'O CLIENTE ALEGA TER EM SEU ESTABELECIMENTO OS ITENS ABAIXO RELACIONADOS:')

        self.pdf.drawString(53, 405, 'ID')
        self.pdf.drawString(93, 405, 'CÓDIGO')
        self.pdf.drawString(240, 405, 'DESCRIÇÃO')
        self.pdf.drawString(415, 405, 'QT')
        self.pdf.drawString(480, 405, 'MOTIVO')

        self.pdf.setFont('Helvetica', 11)
        self.pdf.drawString(56, 380, '1')
        self.pdf.drawString(56, 355, '2')
        self.pdf.drawString(56, 330, '3')
        self.pdf.drawString(56, 305, '4')
        self.pdf.drawString(56, 280, '5')
        self.pdf.drawString(56, 255, '6')
        self.pdf.drawString(56, 230, '7')
        self.pdf.drawString(56, 205, '8')
        self.pdf.drawString(56, 180, '9')
        self.pdf.drawString(53, 155, '10')

        # self.pdf.lines(linhas)
        self._desenharTabela()

        self.pdf.line(60, 90, 255, 90)
        self.pdf.drawString(120, 75, 'Ass. Motorista')
        self.pdf.line(340, 90, 540, 90)
        self.pdf.drawString(405, 75, 'Ass. Cliente')
    
    def _desenharTabela(self):
        quant_linhas = 11
        valores = (40, 420, 555, 120)
        distancia_entre_linhas = 25
        posicao_colunas = [(40, 40), (80, 80),(150, 150),(390, 390),(450, 450),(555, 555)]
        
        # Desenhar linhas da tabela
        x_inicial = valores[0]
        x_final = valores[2]
        y = valores[1]
        y_final = 0
        for i in range(quant_linhas + 1):
            self.pdf.line(x_inicial, y, x_final, y)
            y -= distancia_entre_linhas
            y_final = y + distancia_entre_linhas
        
        # Desenha colunas da tabela
        y_inicial = valores[1]
        for pos_coluna in posicao_colunas:
            self.pdf.line(pos_coluna[0], y_inicial, pos_coluna[1], y_final)

    def salvarPDF(self):
        self.pdf.save()