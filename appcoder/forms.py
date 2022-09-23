from django import forms

class usuarioFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    edad= forms.IntegerField()

class domicilioFormulario(forms.Form):
    tipo= forms.CharField()
    pais= forms.CharField()
    ciudad= forms.CharField()

class mascotaFormulario(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()
    animal= forms.CharField()


