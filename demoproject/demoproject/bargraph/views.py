from django.shortcuts import render
from django.http import HttpResponse

from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap

# Create your views here.
names = ['Kelly', 'Eric', 'Kylie', 'Sam']
pet_count = [2, 3, 1, 4]


def bargraph(request):
    plot = figure(range=names, plot_height=250, title="Pet Counts", toolbar_location=None, tools="")

    plot.vbar(x='x', top='counts', width=0.9, source=names, line_color="white")
    plot.y_range.start = 0
    plot.x_range.range_padding = 0.1
    plot.xaxis.major_label_orientation = 1
    plot.xgrid.grid_line_color = None

    script, div = components(plot)


   # return render(request, "index_bargraph.html", {"the_script": script, "the_div": div})
    return render(request, "index_bargraph.html", {"script": script, "div": div})
