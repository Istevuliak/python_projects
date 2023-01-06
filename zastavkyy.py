# import tkinter
# w = 600
# h = 100
# okno = tkinter.Tk()
# canvas = tkinter.Canvas(okno, width = w, height = h, bg = 'black')
# canvas.pack()
#
# def animacia():
#     global nazov
#     nazov = nazov[1:] + nazov[0]
#     canvas.delete('all')
#     canvas.create_text(w//2,h//2, text = nazov, fill = 'red')
#     canvas.after(250, animacia)
#
# def vypis(index, zastavky, konecna):
#     global nazov
#     nazov = zastavky[index] + ' '
#     if konecna:
#         nazov += ' - konecna zastavka, vystupovat!   '
#     nazov = nazov + ' ' * (20 - len(zastavky))
#
# def dalsia(event):
#     global aktualna, konecna
#     if not konecna:
#         aktualna += 1
#         if aktualna == len(zastavky) -1:
#             konecna = True
#         vypis(aktualna, zastavky, konecna)
#
#
#
# subor = open('zastavky', 'r')
# nazov = ''
# zastavky = []
# for zastavka in subor:
#     zastavky.append(zastavka.strip())
# aktualna = 0
# konecna = False
# vypis(aktualna,zastavky,konecna)
# animacia()
# canvas.bind_all('<Key>', dalsia)
# okno.mainloop()

import tkinter
w = 600
h = 100
okno = tkinter.Tk()
canvas = tkinter.Canvas(okno, width = w, height = h, bg ='black')
canvas.pack()

def animacia():
    global nazov
    nazov = nazov[1:] + nazov[0]
    canvas.delete('all')
    canvas.create_text(w//2,h//2, text = nazov, fill = 'red', font = ('freesansbold.ttf', 20))
    canvas.after(250,animacia)


def vypis(index,zastavky,konecna):
    global nazov
    nazov = zastavky[index] + ' '
    if konecna:
        nazov += ' - konecna, vystupovat!!! '
    nazov = nazov + ' '* (20 - len(zastavky))

def dalsia(event):
    global aktualna, konecna
    if not konecna:
        aktualna += 1
        if aktualna == len(zastavky) - 1:
            konecna = True
        vypis(aktualna,zastavky,konecna)


subor = open('zastavky', 'r')
nazov = ''
zastavky = []
for zastavka in subor:
    zastavky.append(zastavka.strip())
konecna = False
aktualna = 0
vypis(aktualna, zastavky, konecna)
animacia()
canvas.bind_all('<Key>', dalsia)
okno.mainloop()