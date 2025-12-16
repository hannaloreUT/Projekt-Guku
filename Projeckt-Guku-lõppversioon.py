"""
Kivi-paber-käärid mäng

Autorid: Reelika Möller, Hannalore Menning

"""

from random import randint
import tkinter as tk
from pathlib import Path

kasutaja = 0
arvuti = 0

# Kujundus
taust = "deep sky blue"
kast = "dodger blue"
nupu_värv = "chartreuse2"
nupu_hover = "chartreuse4"
tekst = "snow"
suur_tekst = ("FreeMono", 20, "bold")
väike_tekst = ("FreeMono", 14, "bold")

aken = tk.Tk()
aken.title("Projekt Guku")
aken.configure(bg = taust)

kaust = Path(__file__).resolve().parent

põhiraam = tk.Frame(aken, bg = kast, padx = 30, pady = 30)
põhiraam.pack(padx = 20, pady = 20)

kirjeldus_label = tk.Label(põhiraam, text = "VALI: Kivi / Paber / Käärid", font = suur_tekst, bg = kast, fg = tekst)
kirjeldus_label.pack(pady = 15)

seis_label = tk.Label(põhiraam, text = "SEIS: 0 : 0", font = suur_tekst, bg = kast, fg = tekst)
seis_label.pack(pady = 15)

def uus_mäng():
    global kasutaja, arvuti
    kasutaja = 0
    arvuti = 0
    kirjeldus_label.config(text = "VALI: Kivi / Paber / Käärid")
    seis_label.config(text = "SEIS: 0 : 0")

def mängi(kasutaja_valik):
    global kasutaja, arvuti
    arvuti_valik = randint(1, 3)
    
    if kasutaja_valik == "Kivi":
        kasutaja_valik = 1
    elif kasutaja_valik == "Paber":
        kasutaja_valik = 2
    elif kasutaja_valik == "Käärid":
        kasutaja_valik = 3
    else:
        kirjeldus_label.config(text = "Vigane valik")
        return
    
    #Leiab, kumb roundi võitis
    if kasutaja_valik == 1 and arvuti_valik == 3:
        tulemus = "Kasutaja võit!"
        kasutaja += 1
    elif kasutaja_valik == 3 and arvuti_valik == 1:
        tulemus = "Arvuti võit!"
        arvuti += 1
    elif kasutaja_valik > arvuti_valik:
        tulemus = "Kasutaja võit!"
        kasutaja += 1
    elif kasutaja_valik < arvuti_valik:
        tulemus = "Arvuti võit"
        arvuti += 1
    elif kasutaja_valik == arvuti_valik:
        tulemus = "Viik"

    #Näitab vahepealset seisu
    if kasutaja > arvuti:
        seis = f"Kasutaja juhib {kasutaja}:{arvuti}"
    elif arvuti > kasutaja:
        seis = f"Arvuti juhib {arvuti}:{kasutaja}"
    else:
        seis = f"Viik {kasutaja}:{arvuti}"
    
    kirjeldus_label.config(text = tulemus)
    seis_label.config(text = seis)

pildi_raam = tk.Frame(põhiraam, bg=kast)
pildi_raam.pack(pady=(5, 0))

kivi_path = kaust / "kivi.png"
paber_path = kaust / "paber.png"
kaarid_path = kaust / "kaarid.png"

pildid_ok = kivi_path.exists() and paber_path.exists() and kaarid_path.exists()

if pildid_ok:
    # NB: kui pilt on “katki” või pole päris PNG, siis PhotoImage viskab errori
    kivi_img = tk.PhotoImage(file = str(kivi_path)).subsample(2, 2)
    paber_img = tk.PhotoImage(file = str(paber_path)).subsample(2, 2)
    kaarid_img = tk.PhotoImage(file = str(kaarid_path)).subsample(2, 2)

    # hoia viited alles
    aken.kivi_img = kivi_img
    aken.paber_img = paber_img
    aken.kaarid_img = kaarid_img

    tk.Label(pildi_raam, image = kivi_img, bg = kast).grid(row = 0, column = 0, padx = 10)
    tk.Label(pildi_raam, image = paber_img, bg = kast).grid(row = 0, column = 1, padx = 10)
    tk.Label(pildi_raam, image = kaarid_img, bg = kast).grid(row = 0, column = 2, padx = 10)

# kasutaja valikud
def loo_nupp(tekst, käsk, veerg):
    nupp = tk.Button(nupu_raam, text = tekst, command = käsk, font = väike_tekst, bg = nupu_värv, fg = "violet red", activebackground = nupu_hover, relief = "flat", width = 10)
    nupp.grid(row = 0, column = veerg, padx = 8)

nupu_raam = tk.Frame(põhiraam, bg = kast)
nupu_raam.pack(pady = 15)

loo_nupp("Kivi", lambda: mängi("Kivi"), 0)
loo_nupp("Paber", lambda: mängi("Paber"), 1)
loo_nupp("Käärid", lambda: mängi("Käärid"), 2)

# uue mängu alustamise nupp
tk.Button(aken, text = "Uus mäng", font = väike_tekst, bg = "light pink", fg = "violet red", relief = "flat", width = 15, activebackground = "hot pink", command = uus_mäng).pack(pady = 10)
# mängu lõpetamise nupp 
tk.Button(aken, text = "Lõpeta", font = väike_tekst, bg = "light pink", fg = "violet red", relief = "flat", width = 15, activebackground = "hot pink", command = aken.destroy).pack(pady = 10)

aken.mainloop()
