import os
import requests
import shutil

url = input("Inserisci url")

if len(url) == 0:
    exit()

url = url[:url.find('svg')+3] + '/'

i = 1
comando = 'pdftk '
os.mkdir('./tmp')

while True:
    try:
        r = requests.get(url + str(i))
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        break

    open('./tmp/' + str(i) + '.svg', 'wb').write(r.content)
    os.system('rsvg-convert -f pdf -o ./tmp/' + str(i) + '.pdf ./tmp/' + str(i) + '.svg')
    os.remove('./tmp/' + str(i) + '.svg')

    print("Pagina " + str(i) + " convertita")

    comando = comando + "./tmp/" + str(i) + ".pdf "
    i = i + 1

comando = comando + 'cat output mergedfile.pdf'
os.system(comando)
os.system('gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf mergedfile.pdf')
#os.remove('./mergedfile.pdf')
shutil.rmtree('./tmp')