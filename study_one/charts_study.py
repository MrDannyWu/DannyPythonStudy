import os
from pyecharts import Bar,Pie,Line

def get_charts(x,y,label,type1):
    if type1 == 1:
        c = Pie("Pie")
    elif type1 == 2:
        c = Bar("Bar")
    elif type1 == 3:
        c = Line("Line")
    c.add(label,x,y,is_more_utils=True)
    c.show_config()
    c.render("line.html")
    os.system("start line.html")
x = ["Danny","Jenny","Tom","Zach","Tony","Merry"]
y = ["2351","1987","2045","3241","2859","1972"]
label = "Sallery"
type1 = 3
get_charts(x,y,label,type1)



