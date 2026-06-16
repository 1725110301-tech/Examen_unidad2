import web

urls=(
    '/','Index',
    '/imc','IMC'
)

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        
        return render.index()

class IMC:    
    def GET(self):
        kilos=0
        altura = 0
        imc1 = 0
        analisis1 = "analisis"
        return render.imc(kilos,altura,imc1,analisis1)
    def POST(self):
        formulario = web.input()
        kilos= float(formulario['kilos'])
        altura = float(formulario['altura'])
        calcular_imc_analisis = round(kilos/(altura ** 2),2)
        imc1=calcular_imc_analisis
        if imc1 > 18.5:
            texto1="Bajo de peso"
            analisis1 = texto1
        elif imc1 < 25:
            texto2 = "normal"
            analisis1 = texto2
        elif imc1 < 30:
            texto3 = "sobrepeso"
            analisis1 = texto3
        elif imc1 < 34:
            texto3 = "grado 2"
            analisis1 = texto3
        elif imc1 < 35:
            texto3 = "grado 2"
            analisis1 = texto3

        return render.imc(kilos,altura,imc1,analisis1)

        
if __name__ == '__main__':
    app.run()