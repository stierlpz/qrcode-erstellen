# -*- coding: utf-8 -*-
"""qrcode_erstellen.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dGjMZK1i1tGo6kNlFac-VRrS2XmEA4Yh

# Setup
"""

import os #Erstellen Ornder

if not os.path.exists('out/images/png'):
    os.makedirs('out/images/png')

if not os.path.exists('out/images/jpg'):
    os.makedirs('out/images/jpg')    

if not os.path.exists('out/images/gif'):
    os.makedirs('out/images/gif')

if not os.path.exists('out/audio/mp3'):
    os.makedirs('out/audio/mp3')

if not os.path.exists('out/audio/wav'):
    os.makedirs('out/audio/wav')

if not os.path.exists('out/audio/ogg'):
    os.makedirs('out/audio/ogg')    

if not os.path.exists('out/text/txt'):
    os.makedirs('out/text/txt')    

if not os.path.exists('out/text/odt'):
    os.makedirs('out/text/odt')        

if not os.path.exists('out/text/pdf'):
    os.makedirs('out/text/pdf')

pip install pillow #Erstellen Bildverarbeitung

pip install qrcode #Erstellen QR-Code

import qrcode #Import QR-Code

pip install gTTS #Erstellen Text too Spech (Audio)

from gtts import gTTS #Import Text too Spech (Audio)
import os
from io import BytesIO

pip install fpdf #Erstellen PDF

from fpdf import FPDF #Import PDF

"""#QR-Code erstellen

Die fertigen Codes liegen im Ordner 'out/images'.
"""

text=(input('Eingabe: '))

input_data = text

dn=(input('Name der Datei (OHNE DATEITYP!):  '))

print('-------------------------------------------------------------')
print(text,'wird als ',dn,'_qr gespeichert.')
print('-------------------------------------------------------------')

qr = qrcode.QRCode(
        version=5,
        box_size=5,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save('out/images/png/'+dn+'_qr.png')
img.save('out/images/jpg/'+dn+'_qr.jpg')
img.save('out/images/gif/'+dn+'_qr.gif')

print('-------------------------------------------------------------')
print('Images gespeichert als: ')
print('out/images/png/'+dn+'_qr.png')
print('out/images/jpg/'+dn+'_qr.jpg')
print('out/images/gif/'+dn+'_qr.gif')
print('-------------------------------------------------------------')

"""

# Audio
Die fertigen Audios liegen im Ordner 'out/audio'."""

language='de'

tts = gTTS(text,
          lang=language,
          slow=False,
          lang_check=True,

          )
tts.save('out/audio/mp3/'+dn+'_qr.mp3')
tts.save('out/audio/wav/'+dn+'_qr.wav')
tts.save('out/audio/ogg/'+dn+'_qr.ogg')

print('-------------------------------------------------------------')
print('Audios gespeichert als: ')
print('out/audio/mp3/'+dn+'_qr.mp3')
print('out/audio/wav/'+dn+'_qr.wav')
print('out/audio/ogg/'+dn+'_qr.ogg')
print('-------------------------------------------------------------')

"""# Text
Die fertigen Texte liegen im Ordner 'out/text'.
"""

file = open('out/text/txt/'+dn+'.txt','w+')
file.write('Inhalt des QR-Code: '+text)
file.close()

file = open('out/text/odt/'+dn+'.odt','w+')
file.write('Inhalt des QR-Code: '+text)
file.close()
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
pdf.cell(200, 10, txt = 'Inhalt des Qr-Codes '+dn+':', 
         ln = 1, align = 'C')
pdf.cell(200, 10, txt = text,
         ln = 2, align = 'C')
pdf.output('out/text/pdf/'+dn+'_qr.pdf')

print('-------------------------------------------------------------')
print('Text gespeichert als: ')
print('out/text/txt/'+dn+'_qr.txt')
print('out/text/odt/'+dn+'_qr.odt')
print('-------------------------------------------------------------')
print('PDF gespeichert als: ')
print('out/text/pdf/'+dn+'_qr.pdf')
print('-------------------------------------------------------------')