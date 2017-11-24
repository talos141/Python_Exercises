# # need to import at least 3 things to make your
# # bokeh plots work
# from bokeh.plotting import figure, show, output_file
#
# # we specify an HTML file where the output will go
# output_file("plot.html")
#
# # load our x and y data
# x = [10, 20, 30]
# y = [4, 5, 6]
#
# # create a figure
# p = figure()
#
# # create  a histogram
# p.vbar(x=x, top=y, width=0.5)
#
# # render (show) the plot
# show(p)
from builtins import print

from bokeh.plotting import figure, show, output_file
import json

with open("birthday_dict.json", "r") as f:
    birthday_dict = json.load(f)


output_file("plot.html")
x_categories = x = list(birthday_dict.keys())
x = list(birthday_dict.keys())
l = list(birthday_dict.values())
n = l
y = []

for k in n:
    y.append(k.split("/")[1])

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.3)

show(p)


