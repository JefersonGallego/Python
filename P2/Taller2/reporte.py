#import fpdf
from fpdf import FPDF
from numpy import true_divide
import parcial
import Apartamento
import entregable_parcial

class reporte_pdf(FPDF):
    pass   
     
    # def __init__(self,nombre_archivo):
     #  self.nombre_archivo = nombre_archivo

    def logo(self,name,x,y,w,h):
        self.image(name,x,y,w,h)

    def text(self,name):
        with open(name,'rb') as xy :
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,80.0)
        self.set_text_color(76.0,32.0,250.0)
        self.set_font('Arial','',12)
        self.multi_cell(0,10,txt)

    def titles(self,title):
        self.set_xy(70,10)
        self.set_font('Arial','B',20)
        self.set_text_color(220,50,50)
        self.cell(w=210.0, h=40.0,align='c', txt = title,border =0)

    def sub_titles(self,title):
        self.set_xy(100,0.0)
        self.set_font('Arial','B',20)
        self.set_text_color(0,50,50)
        self.cell(w=210.0, h=40.0,align='c', txt = title,border =0)


    def crear(self):
        pdf= reporte_pdf()
        pdf.add_page()
        pdf.logo('fac.png',0,0,50,60)
        pdf.titles("Cuenta del Apartamento")
        pdf.sub_titles('Periodo : Junio 2022')
        pdf.set_author('Los Maradonianos')
        pdf.output('Factura.pdf','F')









        
        


    