#
#   Big Blue Button presentation downloader
#   by Davide Pisanò - GNU GPLv3
#
#   (Python 3 required)
#   Instructions:
#   -pip install svglib
#   -pip install reportlab
#   -pip install requests
#   -join the bbb meeting
#   -drag the presentation page to another window
#   -you'll see a URL like https://*something*/bigbluebutton/presentation/*somethingsomething*/svg/*pagenumber*
#   -copy that URL and remove the the pagenumber, but leave the / before it
#   -paste it as the url var
#   -execute the script
#   -enjoy :)
#

import os
import requests
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

url = 'https://virtualclassroom28.polito.it/bigbluebutton/presentation/c82472806f50a688d8c8f60baab44bc7546dec2d-1588746678126/c82472806f50a688d8c8f60baab44bc7546dec2d-1588746678126/825f43c5ede6565a054c75b49712b27c5b98d39e-1588746732952/svg/'

i = 1
c = canvas.Canvas("out.pdf")

while True:
    try:
        r = requests.get(url + str(i))
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        break

    open('./' + str(i) + '.svg', 'wb').write(r.content)
    rlg = svg2rlg('./' + str(i) + '.svg')
    os.remove('./' + str(i) + '.svg')

    xL, yL, xH, yH = rlg.getBounds()
    c.setPageSize((xH-xL, yH-yL))

    renderPDF.draw(rlg, c, 0, 0)
    c.showPage()

    print("Pagina " + str(i) + " aggiunta")

    i = i + 1

c.save()