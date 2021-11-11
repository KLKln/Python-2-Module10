from django.shortcuts import render
from django.http import HttpResponse

from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure, show
import math

def piechart(request, div=None):
    graph = figure(title = "fuel for new cars")

    sectors = ["gas", "diesel", "electric"]

    percentages = [57.3, 34.9, 7.8]

    radians = [math.radians((percent / 100) * 360) for percent in percentages]

    start_angle = [math.radians(0)]
    prev = start_angle[0]
    for i in radians[:-1]:
        start_angle.append(i + prev)
        prev = i + prev

    end_angle = start_angle[1:] + [math.radians(0)]

    x = 0
    y = 0

    radius = 1

    color = ["yellow", "red", "lightblue"]

    for i in range(len(sectors)):
        graph.wedge(x, y, radius,
                    start_angle=start_angle[i],
                    end_angle=end_angle[i],
                    color=color[i],
                    legend_label=sectors[i])

    #show(graph)
    return render(request, "piechart_index.html", {"the_script": show(graph), "the_div": div})

