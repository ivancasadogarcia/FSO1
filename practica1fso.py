#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from ScrolledText import *
from subprocess import *

"""
Importem les llibreries que necesitarem.
"""
import tkFileDialog
import tkMessageBox
import os
import subprocess

#MAIN
"""
Inicialitzem la variable finestra i els frames que contindran els botons, els label, els entry i tot el que necesitem.
Utilitzarem Frames per tal que tot ens quedi ben colocat.
"""
finestra=Tk()
F1=Frame(finestra)
F2=Frame(finestra)
F3=Frame(finestra)
F4=Frame(finestra)
F5=Frame(finestra)
F6=Frame(finestra)
F7=Frame(finestra)
F8=Frame(finestra)
F9=Frame(finestra)
finestra.title("prova script grafic")
finestra.minsize(800,400)
"""
descripcio,parametres d'entrada,resultats obtinguts, feina a realitzar i casos d'excepcions
Inicialitzem les variables codis i arxiu_path com a StringVars.
""" 
path=StringVar()
path.set(os.getcwd())

"""
obrirdirectori(): 
La seva funció es obrir una finestra de selecció per a que nosaltres poguem escollir un arxiu, un cop sapiguem quin arxiu es, actualitzarem el path.
No li passarem cap paràmetre d'entrada. Tampoc controlem cap cas d'excepció.
"""
def obrirdirectori():
    global path
    nom=tkFileDialog.askdirectory()
    if nom:
	path.set(nom)
    else:
	return

"""
Inicialitzem el primer botó utilitzant el primer frame F1 i després utilitzarem la funció pack per a que així ens quedi posicionat a l'esquerra, aquest botó cridarà la comanda obrirdirectori.
"""
escollird=Button(F1,text='Escollir directori de treball',command=obrirdirectori)
escollird.pack(side=LEFT,anchor=W)
"""
Inicialitzarem una label, que serà el que utilitzarem per mostrar el path actual després de ser seleccionat per l'usuari, el colocarem al frame 1.
"""
entrypath= Label(F1, textvariable=path,bg="white", fg="black")
entrypath.pack(side=LEFT,anchor=W, expand=TRUE,fill=X)
"""
Establirem que el primer frame es posicioni a la part de dalt utilitzant tot l'eix x.
"""
F1.pack(side=TOP,anchor=W,fill=X)
"""
Definim la variable ev com una StringVar i nom_script com una variable global.
"""
nom_script=StringVar()

"""
obrirscript():
Aquesta funció crida una finestra que utilitzarem per coneixer l'arxiu que volem obrir, un cop l'usuari l'ha escollit, mostrarà el seu contingut en la StringVar ev per fer-ho utilitzarem la funció read().
"""

def obrirscript():
    global path
    global nom
    nom=tkFileDialog.askopenfile(filetypes=[('Script file','.sh')],title="Open",defaultextension='.sh',initialdir=path.get())
    if not nom:
        return
    else:
	nom_script.set(nom.name)
	editarea.delete(1.0,END)
	editarea.insert(END,nom.read())
"""
Inicialitzem el segon botó utilitzant el segon frame F2 i després utilitzarem la funció pack per a que així ens quedi posicionat a l'esquerra, aquest botó cridarà a la comanda obrirscript.
"""
obrirs=Button(F2,text='Obrir Script', command=obrirscript)
obrirs.pack(side=LEFT,anchor=W)
"""
Inicialitzem el primer Label utilitzant el segon frame F2 i després utilitzarem la funció pack per a que així ens quedi posicionat a l'esquerra.
"""
pentry= Label(F2, width=15,bg="white",textvariable=nom_script)
pentry.pack(side=LEFT,anchor=W, expand=TRUE,fill=X)


def guardarscriptcom():
	global path
	global nom_script
	arxiu_guardat=tkFileDialog.asksaveasfilename(filetypes=[('Script file','.sh')],title="Save as",defaultextension='.sh',initialdir=path.get())
	
	if (not arxiu_guardat ):
		return
	else:	
		file=open(arxiu_guardat,'w')
		x=editarea.get("1.0",END)
		file.write(x)
		file.close()
		permis="chmod u+x "+arxiu_guardat
		os.system(permis)
		nom_script.set(arxiu_guardat)
		tkMessageBox.showinfo("Guardar", "Fitxer guardat correctament")

def guardarscript():	
	global nom_script	
	if (not nom_script.get()):
		guardarscriptcom()
	else:
		file=open(nom.name,'w')
		x=editarea.get("1.0",END)
		file.write(x)
		file.close()
		tkMessageBox.showinfo("Guardar", "Fitxer guardat correctament")

"""
Inicialitzarem el tercer botó que serà guardar script, estarà situat al frame 2 utilitzant la funció pack per a que així ens quedi posicionat a l'esquerra. Cridarem la comanda tkFileDialog.asksaveasfile per a guardar el script que tinguem a l'Entry text.
"""
guardars=Button(F2,text='Guardar Script',command=guardarscript)
guardars.pack(side=LEFT,anchor=W)
"""
Establirem que el segon frame es posicioni a la part de dalt utilitzant tot l'eix x.
"""
F2.pack(side=TOP,anchor=W,fill=X)

"""
Inicialitzarem el quart botó que serà guardar un nou script, estarà situat a la finestra ja que serà l'únic element que hi haurà a la fila, el colocarem a la part superior esquerra.
"""
guardarns=Button(finestra,text='Guardar nou script', command=guardarscriptcom)
guardarns.pack(side=TOP,anchor=W)

"""
Inicialitzarem un text, que serà el que utilitzarem per mostrar el codi dels scripts que obrim. El colocarem a la part superior utilitzant tot l'eix x.
"""
editarea=Text(finestra)
editarea.pack(side=TOP,fill=BOTH,expand=TRUE)

"""
Inicialitzarem un label amb el nom "Arguments d'entrada", el colocarem al frame 3.
"""
titolarguments=Label(F3,text="Arguments d'entrada:")
titolarguments.pack(side=LEFT, anchor=W)

"""
Inicialitzarem un entry que utilitzarem per a que l'usuari pugui afegir codi al script que està a l'entry text, el colocarem al frame 3.
"""
argumentse= Entry(F3, width=15,bg="white")
argumentse.pack(side=LEFT,anchor=W, expand=TRUE,fill=X)

"""
Inicialitzem les dues variables gen_out i gen_err.
"""
gen_out=0
gen_err=0

"""
comanda_stdout():
Aquesta funció .
"""
def comanda_stdout():
    global gen_out
    gen_out=gen_out+1

"""
comanda_stdout():
Aquesta funció .
"""
def comanda_stderr():
    global gen_err
    gen_err=gen_err+1

"""
Inicialitzem els Checkbutton out i err els quals cridaran les comandes comanda_stdout i comanda_stderr respectivament.
"""
out=Checkbutton(F3,text="Generar stdout",command=comanda_stdout)
err=Checkbutton(F3,text="Generar stderr",command=comanda_stderr)
out.pack(side=LEFT,anchor=E)
err.pack(side=LEFT,anchor=E)

"""
veure_stdout():
Aquesta funció ens obrirà una nova finestra per tal de veure el text editat.

"""
def veure_stdout():
	try:
		arxiu_out=nom_script.get()[:-2]+"out"
		file=open(arxiu_out,'r')
		fout=Tk()
		fout.title("Resultat stdout")
		fout.minsize(400,200)
		sout=Button(fout,text='Sortir',command=fout.destroy)
		sout.pack(side=BOTTOM,anchor=W)
		edit_out=Text(fout)
		edit_out.pack(side=TOP,fill=BOTH,expand=TRUE)
		edit_out.delete(1.0,END)
		edit_out.insert(END,file.read())
		file.close()

	except IOError:
		tkMessageBox.showwarning("Error stdout", "No hi ha fitxer de de sortida")

"""
veure_stderr():
Aquesta funció ens obrirà una finestra d'error que ens infromarà que no ha trobat cap fitxer.
"""
def veure_stderr():
	try:
		arxiu_err=nom_script.get()[:-2]+"err"
		file=open(arxiu_err,'r')
		ferr=Tk()
		ferr.title("Resultat stderr")
		ferr.minsize(400,200)
		serr=Button(ferr,text='Sortir',command=ferr.destroy)
		serr.pack(side=BOTTOM,anchor=W)
		edit_err=Text(ferr)
		edit_err.pack(side=TOP,fill=BOTH,expand=TRUE)
		edit_err.delete(1.0,END)
		edit_err.insert(END,file.read())
		file.close()
	except IOError:
		tkMessageBox.showwarning("Error stderr", "No hi ha fitxer de d'error")

"""
Inicialitzem el cinquè i sisè botó bout i berr que criden respectivament les comandes veure_stdout i veure_stderr. les posarem al frame 4 al costat dret.
"""
bout=Button(F4,text="Veure stdout",command=veure_stdout)
berr=Button(F4,text="Veure stderr",command=veure_stderr)
berr.pack(side=RIGHT)
bout.pack(side=RIGHT)



"""
Aquesta funció cridarà el script inmediatament després de clicar el botó.
No li passem cap variable d'entrada ni retorna cap variable.
"""
def run():
	global gen_out
	global gen_err
	global nom_script

	if not nom_script.get():
		tkMessageBox.showwarning("Error", "No hi ha script per executar")
		return
	else:
		arxiu_out=nom_script.get()[:-2]+"out"
		arxiu_err=nom_script.get()[:-2]+"err"
		arxiu_exec=nom_script.get()+" "+argumentse.get()	
		if (gen_out%2!=0):
			if(gen_err%2!=0):
				arxiu_exec=arxiu_exec+" > "+arxiu_out+" 2> "+arxiu_err
				result=os.system(arxiu_exec)
			else:
				arxiu_exec=arxiu_exec+">"+arxiu_out
				result=os.system(arxiu_exec)

		elif (gen_err%2!=0):
			arxiu_exec=arxiu_exec+" 2>"+arxiu_err
			result=os.system(arxiu_exec)
		
		else:
			result=os.system(arxiu_exec)
"""
Funcio que gracies la comanda at programa una execucio d'un script a una hora concreta, que ens passen per parametre
"""
contador=0
def runAt():
	global nom_script
	global contador 

	if not (e2hora.get()):
		tkMessageBox.showwarning("Error", "Primer indica l'hora")
		return
	
	if not nom_script.get():
		tkMessageBox.showwarning("Error", "No hi ha script per executar")
		return
	else:	
		contador=contador+1
		fitxerPar="nou"+str(contador)
		f=open(fitxerPar,"w")
		inici="#! /bin/bash \n\n"+"\n"+nom_script.get()+" "+argumentse.get()

		os.system('chmod +x '+fitxerPar)
		sortida=nom_script.get()[:-2]+"out"
		error=nom_script.get()[:-2]+"err"
		script="at "+e2hora.get()+" -f ./"+fitxerPar
		if (gen_out%2!=0):
			if(gen_err%2!=0):
				f.write(inici+" > "+sortida+" 2> "+error+"\nrm "+fitxerPar)
			else:
				f.write(inici+" > "+sortida+"\nrm "+fitxerPar)

		elif (gen_err%2!=0):
			f.write(inici+" 2> "+error+"\nrm "+fitxerPar)
		
		f.close()
		if(os.system(script)==0):
			tkMessageBox.showinfo("Programat","A les "+e2hora.get()+" s'executara "+nom_script.get())

"""
Funcio que gracies la comanda at programa una execucio d'un script en uns segons, que ens passen per parametre
"""
def runAtSegons():
	global gen_out
	global gen_err
	global nom_script

	if not nom_script.get():
		tkMessageBox.showwarning("Error", "No hi ha script per executar")
		return
	elif not e1segon.get():
		tkMessageBox.showwarning("Error", "Posa els segons primer!")
		return	
	else:	
		temps=e1segon.get()
		arxiu_out=nom_script.get()[:-2]+"out"
		arxiu_err=nom_script.get()[:-2]+"err"
		arxiu_exec=nom_script.get()+" "+argumentse.get()	
		if (gen_out%2!=0):
			if(gen_err%2!=0):
				arxiu_exec=arxiu_exec+" > "+arxiu_out+" 2> "+arxiu_err
			else:
				arxiu_exec=arxiu_exec+">"+arxiu_out

		elif (gen_err%2!=0):
			arxiu_exec=arxiu_exec+" 2>"+arxiu_err
		
		pr=subprocess.Popen("sleep "+temps+";"+arxiu_exec,shell=True)
		if (pr):
			tkMessageBox.showinfo("Programat","Ens esperarem "+e1segon.get()+" segons")
		
			

			


"""
Funcio que gracies la comanda crontab programa una execucio d'un script a una hora concreta, cada 24 hores, que ens passen per parametre
"""
def runCron():
	global nom_script

	if not nom_script.get():
		tkMessageBox.showwarning("Error", "No hi ha script per executar")
		return
	else:	
		arxiu_out=nom_script.get()[:-2]+"out"
		arxiu_err=nom_script.get()[:-2]+"err"
		if not e3mm.get():minuts='*'
		else: minuts=e3mm.get()
		if not e3hh.get():hores='*'
		else: hores=e3hh.get()
		if not e3dM.get():dia='*'
		else: dia=e3dM.get()
		if not e3Mes.get():mes='*'
		else: mes=e3Mes.get()
		if not e3dS.get():diasetmana='*'
		else: diasetmana=e3dS.get()
		comanda=minuts+" "+hores+" "+dia+" "+mes+" "+diasetmana+" "+nom_script.get()+" "+argumentse.get()
		exe=comanda
		if (gen_out%2!=0):
			if(gen_err%2!=0):
				exe=comanda+" > "+arxiu_out+" 2> "+arxiu_err 
			else:
				exe=comanda+" > "+arxiu_out
		elif (gen_err%2!=0):
			exe=comanda+" 2> "+arxiu_err
			
		result=os.system('(crontab -l; echo "'+exe+'") | crontab -')
		
		if(result==0):
			tkMessageBox.showinfo("Programat","A les "+hores+":"+ minuts+" el dia "+ dia+" el mes "+ mes+" el dia de la setmana "+ diasetmana+" executarem  "+nom_script.get())

"""
Inicialitzem el setè botó que cridarà la comanda run. El situarem al cinquè frame situat a la dreta.
"""
exctb=Button(F5,text="Run",command=run)
exctb.pack(side=RIGHT)

"""
Inicialitzem el label amb el titol "Executa inmediatament" al frame 5 i el situem a la dreta.
"""
exct=Label(F5,text="Exececuta inmediatament")
exct.pack(side=RIGHT)

exc1=Label(F6,text="Exececuta d'aqui a")
e1segon=Entry(F6,width=3)
exc1segons=Label(F6,text="segons")
exc1b=Button(F6,text="Run",command=runAtSegons)

exc1b.pack(side=RIGHT)
exc1segons.pack(side=RIGHT)
e1segon.pack(side=RIGHT)
exc1.pack(side=RIGHT)

exc2=Label(F7,text="Executa un cop amb format(HH:MM)")
e2hora=Entry(F7,width=6)
exc2strings=Label(F7,text="de at")
exc2b=Button(F7,text="Run",command=runAt)

exc2b.pack(side=RIGHT)
exc2strings.pack(side=RIGHT)
e2hora.pack(side=RIGHT)
exc2.pack(side=RIGHT)



exc3=Label(F8,text="Programa cada dia amb format")
e3mm=Entry(F8,width=3)
e3hh=Entry(F8,width=3)
e3dM=Entry(F8,width=3)
e3Mes=Entry(F8,width=3)
e3dS=Entry(F8,width=3)
exc3string=Label(F8,text="crontab")
exc3run=Button(F8,text="Run",command=runCron)

exc3run.pack(side=RIGHT)
exc3string.pack(side=RIGHT)
exc3run.pack(side=RIGHT)

e3dS.pack(side=RIGHT)

e3Mes.pack(side=RIGHT)

e3dM.pack(side=RIGHT)

e3hh.pack(side=RIGHT)

e3mm.pack(side=RIGHT)

exc3.pack(side=RIGHT)


mmhhdMMesdS=Label(F9,text="mm   hh   dM   Mes   dS                          ")
mmhhdMMesdS.pack(side=RIGHT)

s=Button(finestra,text='Sortir',command=finestra.quit)
s.pack(side=BOTTOM,anchor=W)
F9.pack(side=BOTTOM, anchor=E)
F8.pack(side=BOTTOM, anchor=E)
F7.pack(side=BOTTOM, anchor=E)
F6.pack(side=BOTTOM, anchor=E)
F5.pack(side=BOTTOM, anchor=E)
F4.pack(side=BOTTOM, anchor=E)
F3.pack(side=BOTTOM,fill=X)

finestra.mainloop()
