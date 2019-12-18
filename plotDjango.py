from django.http import HttpResponse
from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import StringIO
from kal_sar import main as kal_sar


def index(request):
    return render(request, 'calc/index.html')

data_set = kal_sar()

print(data_set[0], data_set[1])

header = data_set[0]
body_set =data_set[1]

def showimage(request):
    t = arange(0.0, 2.0 , 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)

    xlabel('time (s)')
    ylable('voltage (mv)')
    title('About as simploe as it gets, folks')
    pylab.show()

    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_pilImage.save(buffer, "PNG"))
    pylab.close()
    return HttpResponse(buffer.getvalue(), content_type="image/png")

