#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 柱状图
# from pyecharts import options as opts
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

from pyecharts.charts import Gauge
from pyecharts.options.global_options import VisualMapOpts
from pyecharts.types import BarBackground


class show_chart():

    def __init__(self) -> None:
        self.c1 = 1
        pass

    def init(self):
        self.FPY = 95.1
        self.Efficiency = 65.1
        self.UPH_Name = ['W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'W2Q12-60001', 'w2q13-60001', '', '', 'T6B59-60001', 'T6B59-60001', 'g3q63-60001',
                         'g3q63-60001']
        self.UPH = [423, 311, 266, 291, 277, 154, 192, 279, 253, 368,
                    366, 184, 301, 275, 343, 214, 259, 32, 0, 0, 0, 0, 0, 0]
        self.Hour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        self.UPH_max = max(self.UPH)

    def add_gauge_FPY(self):
        self.chart_gauge_FPY = (
            Gauge(init_opts=opts.InitOpts(width="300px",
                                          height="300px",
                                          page_title="HP TE DashBoard",
                                          chart_id="FPY"))

            .add(series_name="FPY", data_pair=[["FPY", self.FPY]],
                 axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(
                     color=[(0.90, "#Df384f"), (0.90, "yellow"), (1, "green")], width=30
                 )
                 ),
                 # radius="100%"
                 )

            .set_global_opts(
                legend_opts=opts.LegendOpts(is_show=False),
                tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
                # title_opts=opts.TitleOpts(title="HP TE DashBoard"),
            )
        )

    def add_gauge_efficiency(self):
        self.chart_gauge_efficiency = (
            Gauge(init_opts=opts.InitOpts(width="300px",
                                          height="300px",
                                          page_title="HP TE DashBoard",
                                          chart_id="efficiency"))
            .add(series_name="Efficiency", data_pair=[["Efficiency.", self.Efficiency]],
                 axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(
                     color=[(0.30, "#Df384f"), (0.50, "#B2B200"), (1, "green")], width=30
                 )
                 ),
                 # .add(radius="10%")
                 )
            .set_global_opts(
                legend_opts=opts.LegendOpts(is_show=False),
                tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
            )
        )

    def add_bar_UPH(self):
        self.chart_bar_UPH = Bar(init_opts=opts.InitOpts(width="600px", height="300px", chart_id="UPH"))
        self.chart_bar_UPH = Bar(init_opts=opts.InitOpts(chart_id="UPH"))
        self.chart_bar_UPH = Bar(init_opts=opts.InitOpts(page_title="HP TE DashBoard"))

        self.chart_bar_UPH.add_xaxis(self.Hour)
        self.chart_bar_UPH.add_yaxis("UPH", self.UPH)
        self.chart_bar_UPH.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                type_="color",
                min_=0,
                max_=self.UPH_max,
                range_color=["#FF0000", "#B7B700", "#009B42"]
            )
        )
        # self.chart_bar_UPH.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))

    def show(self):
        self.chart_gauge_FPY.render("FPY.html")
        self.chart_bar_UPH.render("UPH.html")
        self.chart_gauge_efficiency.render("Efficiency.html")


if __name__ == '__main__':
    chart1 = show_chart()
    chart1.init()
    chart1.add_gauge_FPY()
    chart1.add_bar_UPH()
    chart1.add_gauge_efficiency()
    chart1.show()
