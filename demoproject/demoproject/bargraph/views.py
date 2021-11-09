from django.shortcuts import render
from django.http import HttpResponse

from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure

# Create your views here.
names = ['Kelly', 'Eric', 'Kylie', 'Sam']


def bargraph(request):
    plot = figure(x_range=names, title = "Pet Counts")
    plot.vbar(x=names, top=[2, 3, 1, 4], width=0.9)
    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0
    script, div = components(plot, CDN)

    return render(request, "index_bargraph.html", {"the_script": script, "the_div": div})
