from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class IndexView(View):
    def get(self,request):
        # return HttpResponse("Zde bude titulní strana.")
        # return HttpResponse("<a href='http://localhost:8000/katalog/seznam/'>Katalog</a>")
        return HttpResponse("""<h1>Autopůjčovna HappyDrive</h1>
        <h2>S naším autem se spolehlivě přepravíte!</h2>
        <p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
        <p> Máme auta značky: </p>
         <ul>
           <li>BMW</li>
           <li>Citroën</li>
           <li>Škoda</li>
         </ul>
        
        <br> Odkaz na nabídku: <br/>
        <a href='http://localhost:8000/katalog/seznam/'>Naše auta</a><br>
        """)

class SeznamView(View):
    def get(self,request):
        return HttpResponse("Zde bude seznam aut.")
