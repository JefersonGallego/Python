

from zmq import PROTOCOL_ERROR_ZAP_INVALID_STATUS_CODE
import parcial
import Apartamento
import reporte

if __name__ == '__main__':

    periodo = 'Junio 2022'
    a = parcial.Ingreso_nombres()
    b = parcial.Ingreso_dias(a)
    c = parcial.acum_dias(b)
    d = Apartamento.inquilino(a,b)
    valor_arriendo = parcial.validar_Dato('Por favor ingrese el valor del arriendo : ')
    valor_luz = parcial.validar_Dato('Por favor Ingrese el valor del recibo de la luz :')
    h=d.pago(valor_arriendo,valor_luz,c)
    q=parcial.limites('Por ingrese el valor del kW/h : ',100,300)
    print(q)
    valor_kw=Apartamento.luz(valor_luz,periodo)
    valor_kw=valor_kw.valor_kwh(q,valor_luz)
    parcial.mostrar_pant(a,h,valor_luz,valor_arriendo,valor_kw)

    pdf=reporte.reporte_pdf()
    pdf.crear()