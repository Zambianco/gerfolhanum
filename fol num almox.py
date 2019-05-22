from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import time

import getpass

pdfmetrics.registerFont(TTFont('Calibri', 'calibri.ttf'))
pdfmetrics.registerFont(TTFont('Courier', 'cour.ttf'))
pdfmetrics.registerFont(TTFont('Times-Regular', 'times.ttf'))
pdfmetrics.registerFont(TTFont('Garamond-Negrito', 'garabd.ttf'))
pdfmetrics.registerFont(TTFont('Garamond-Italico', 'garait.ttf'))
pdfmetrics.registerFont(TTFont('Consola', 'consola.ttf'))

canvas = canvas.Canvas('arquivo.pdf', pagesize=A4)


def gerafolha(intmarg, extmarg, infmarg, supmarg):
    global numos
    canvas.setLineWidth(0.6 * mm)
    canvas.line(intmarg * mm, infmarg * mm, intmarg * mm, (297 - supmarg) * mm) # Desenhor da borda interna
    canvas.line(intmarg * mm, infmarg * mm, (210 - extmarg) * mm, infmarg * mm) # Desenhor da borda inferior
    canvas.line((210 - extmarg) * mm, infmarg * mm, (210 - extmarg) * mm, 287 * mm) # Desenhor da borda externa
    canvas.line((210 - extmarg) * mm, (297 - supmarg) * mm, intmarg * mm, (297 - supmarg) * mm) # Desenhor da borda superior

    canvas.line((210 - extmarg) * mm, 280 * mm, intmarg * mm, 280 * mm) # Linha inferir do cabeçalho
   

    for linha in range(1, 34):
        # Linhas para escrita
        altura = 280 - (8 * linha)
        canvas.setLineWidth(0.254 * mm)
        canvas.line(intmarg * mm, altura * mm, (210 - extmarg) * mm, altura * mm)

        if numos % 100 == 0:
            canvas.setFont('Garamond-Negrito',18)
        else:
            canvas.setFont('Garamond-Italico',18)
            
        canvas.drawCentredString((intmarg + 12.5) * mm, (altura + 2) * mm, str(numos))
        numos += 1
        canvas.setFont('Times-Regular',18)
        canvas.drawCentredString((intmarg + 157.5) * mm, (altura + 2) * mm, "/    /")

    canvas.setLineWidth(0.254 * mm)
    canvas.setDash(1,1)
    canvas.line((intmarg + 25) * mm, 16 * mm, (intmarg + 25) * mm, 287 * mm) # Borda direita Num. O.S.
    canvas.line((intmarg + 70) * mm, 16 * mm, (intmarg + 70) * mm, 287 * mm) # Borda direita Cliente
    canvas.line((intmarg + 115) * mm, 16 * mm, (intmarg + 110) * mm, 287 * mm) # Borda direita Motor
    canvas.line((intmarg + 145) * mm, 16 * mm, (intmarg + 145) * mm, 287 * mm) # Borda direita Montador
    canvas.line((intmarg + 170) * mm, 16 * mm, (intmarg + 170) * mm, 287 * mm) # Borda direita Data
    canvas.setDash(1,0)

    canvas.setFont('Times-Regular',18)
    canvas.drawCentredString((intmarg + 12.5) * mm, 281.5 * mm, "OS")
    canvas.drawCentredString((intmarg + 47.5) * mm, 281.5 * mm, "Cliente")
    canvas.drawCentredString((intmarg + 90) * mm, 281.5 * mm, "Motor")
    canvas.drawCentredString((intmarg + 127.5) * mm, 281.5 * mm, "Montador")
    canvas.drawCentredString((intmarg + 157.5) * mm, 281.5 * mm, "Data")
    canvas.drawCentredString((intmarg + 177.5) * mm, 281.5 * mm, "Ass.")
    canvas.setFont('Times-Regular',12)
    canvas.drawCentredString((intmarg + 85) * mm, 10 * mm, "Página _____")

    # ----------- IMPRESSÃO DO CARIMBO DE TEMPO E NOME DE USUÁRIO -----------
    canvas.setFont('Consola',8) 
    canvas.saveState()
    canvas.rotate(90)
    
    if intmarg > extmarg:
        canvas.drawString(infmarg * mm, -(intmarg - 5)  * mm, str("{} - {}".format(time.time(), getpass.getuser())))
    else:
        canvas.drawString(infmarg * mm, -(210 - extmarg + 5) * mm, str("{} - {}".format(time.time(), getpass.getuser())))
    canvas.restoreState()

    canvas.showPage() # Adiciona uma nova página




intmarg = 18 # Borda interna
extmarg = 7 # Borda inferior
infmarg = 16 # Borda externa
supmarg = 10 # Borda superior

numos = int(input("OS inicial: "))
numfol = int(input("Folhas: "))

for folha in range(0, numfol):
    canvas.line(5 * mm, 148.5 * mm, 15 * mm, 148.5 * mm) # Indicativo furação

    gerafolha(intmarg, extmarg, infmarg, supmarg)
    gerafolha(extmarg, intmarg, infmarg, supmarg)

canvas.save()
