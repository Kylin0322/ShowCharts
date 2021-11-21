# 柱状图
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


import pyecharts.options as opts
from pyecharts.charts import Gauge

(
    Gauge(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(series_name="FPY", data_pair=[["", 55.5]])
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )
    .render("gauge.html")
)


class show_chart():

    def __init__(self) -> None:
        self.c1 = 1
        pass

    def init(self):
        self.FPY = 0.95
        self.Efficiency = 0.65
        self.UPH_Name = ['W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'w2q13-60001', '', '', 'T6B59-60001', 'T6B59-60001', 'g3q63-60001',
                         'g3q63-60001']['W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'w2q13-60001', '', '', 'T6B59-60001', 'T6B59-60001', 'g3q63-60001', 'g3q63-60001']
        self.UPH = [423, 311, 266, 291, 277, 154, 192, 279, 253, 368,
                    366, 184, 301, 275, 343, 214, 259, 32, 0, 0, 0, 0, 0, 0]
        self.Hour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
