


import parcial



class facturas:
    def __init__(self,valor_factura,periodo):
        self.valor_factura = valor_factura
        self.periodo = periodo

        
    @staticmethod
    def mostar_calculo(self):
        print(f'El valor total es  {self.valor_factura}')

class arriendo(facturas):
    def __init__(self):
        super().__init__()


class luz(facturas):
    def __init__(self,valor_luz,periodo):
        super().__init__(valor_luz,periodo)

    def valor_kwh(self,kw_h,valor_luz):
        self.kw_h=kw_h
        self.valor_luz=valor_luz
        y=self.valor_luz/self.kw_h
        return y


class inquilino:

    # Contructor
    def __init__(self,nombre_inquilino,num_dias):
        self.nombre_inquilino = nombre_inquilino
        self.num_dias = num_dias

    # Metodo de Instancia
    
    def pago (self,fac_arriendo,fac_luz,acum):
        self.fac_arriendo = fac_arriendo
        self.fac_luz = fac_luz
        self.acum = acum
        pagos=[]
        for i in range(0,len(self.num_dias)):
            a=int(self.num_dias[i])
            au=(a/(a+(self.acum-a)))
            pagos.append(float((au*self.fac_luz)+(self.fac_arriendo/len(self.num_dias))))
        return pagos



"""
if __name__ == '__main__':


    periodo = 'Junio 2020'
    a=parcial.Ingreso_nombres()
    b=parcial.Ingreso_dias(a)
    c=parcial.acum_dias(b)
    d = inquilino(a,b)
    valor_arriendo = parcial.validar_Dato('Por favor ingrese el valor del arriendo : ')
    valor_luz = parcial.validar_Dato('Por favor Ingrese el valor del recibo de la luz :')
    f= facturas(valor_arriendo,'periodo')
    g= facturas(valor_luz,periodo)
    h=d.pago(valor_arriendo,valor_luz,c)
    q=parcial.limites('Por ingrese el valor del kW/h : ',100,300)
    print(q)
    valor_kw=luz(valor_luz,periodo)
    valor_kw.valor_kwh(q)
    
"""

    
    
