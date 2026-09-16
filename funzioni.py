#Esercizio 1
def quadrato(x):
    return x*x
print(quadrato(5))
print(quadrato(12))
#Esercizio 2
def saluta(nome,saluto="Ciao"):
    print(f"{saluto},{nome}")
saluta("Luca")
saluta("Anna","Buongiorno")
#Esercizio 3
def somma(*args):
    return sum(args)
print(somma(1,2,3))
print(somma(10,20,30,40))
#Esercizio 4
def media(numero):
    medianumeri=sum(numero)/len(numero)
    return medianumeri
n=[2,4,6]
print(media(n))
#Esercizio 5 Contatto

rubrica=[]

def aggiungi_contatto(nome,numero,email):
    contatto={"nome":nome,"numero":numero,"email":email}
    rubrica.append(contatto)
    print(f"Contatto {nome} aggiunto")
    

def modifica_contatto(nome,nuovo_numero=None,nuova_email=None):
    for c in rubrica:
        if c["nome"].lower()==nome.lower():
            if nuovo_numero:
                c["numero"]=nuovo_numero
            if nuova_email:
                c["email"]=nuova_email
            print(f"Contatto {nome} modificato")
            return
    print("Contatto non trovato")

def elimina_contatto(nome):
    for c in rubrica:
        if c["nome"].lower()==nome.lower():
            rubrica.remove(c)
            print(f"Contatto {nome} eliminato")
            return
    print("Contatto non trovato")

def cerca_contatto(nome):
    for c in rubrica:
        if c["nome"].lower()==nome.lower():
            print("Contatto trovato",c)
            return
    print("Contatto non trovato")

def mostra_contatti():
    if not rubrica:
        print("Rubrica vuota")
        return
    ordinati=sorted(rubrica,key=lambda x:x["nome"].lower())
    for c in ordinati:
        print(f"{c['nome']}-{c['numero']}-{c['email']}")

aggiungi_contatto("Luca","32423423432432","Luca@email.com")
aggiungi_contatto("Paola","5433453","Paola@email.com")
mostra_contatti()

modifica_contatto("Luca",nuova_email="Lucanuovoemail@email.com")
cerca_contatto("Paola")
elimina_contatto("Paola")
mostra_contatti()