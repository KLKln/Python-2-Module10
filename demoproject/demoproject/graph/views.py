from django.shortcuts import render
from django.http import HttpResponse
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure


# Create your views here.
def graph(request):
    plot = figure()
    x1 = [1, 2, 3, 4, 5]
    y1 = [2, 3, 4, 5, 6]
    plot.line(x1, y1)

    script, div = components(plot, CDN)

    return render(request, "graph_index.html", {"the_script": script, "the_div": div})
