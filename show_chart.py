#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 柱状图
from pyecharts import options as opts
from pyecharts.charts import Bar, Page
from pyecharts.globals import ThemeType
from pyecharts.charts import Gauge



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
        chart_gauge_FPY = (
            Gauge(init_opts=opts.InitOpts(theme=ThemeType.DARK,
                                          width="300px",
                                          height="300px",
                                          page_title="HP TE DashBoard",
                                          chart_id="FPY"))

            .add(series_name="FPY",
                 data_pair=[["FPY", self.FPY]],
                 title_label_opts=opts.GaugeTitleOpts(font_size=19, offset_center=[
                                                      0, "65%"]),  # title size and location
                 detail_label_opts=opts.GaugeDetailOpts(font_size=17, offset_center=[
                                                        0, "40%"]),  # data size and location
                 axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(
                     color=[(0.90, "#Df384f"), (0.90, "yellow"), (1, "green")], width=30)),
                 # radius="100%"
                 )

            .set_global_opts(
                legend_opts=opts.LegendOpts(pos_left="20%"),
                tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%")
                # title_opts=opts.TitleOpts(title="HP TE DashBoard"),
            )
        )
        return chart_gauge_FPY

    def add_gauge_efficiency(self):
        chart_gauge_efficiency = (
            Gauge(init_opts=opts.InitOpts(theme=ThemeType.DARK,
                                          width="300px",
                                          height="300px",
                                          page_title="HP TE DashBoard",
                                          chart_id="efficiency"))
            .add(series_name="Efficiency",
                 data_pair=[["Efficiency", self.Efficiency]],
                 title_label_opts=opts.GaugeTitleOpts(font_size=19,
                                                      offset_center=[0, "70%"]),  # 给仪表盘里的标题设置颜色大小
                 detail_label_opts=opts.GaugeDetailOpts(font_size=17, offset_center=[0, "40%"]),
                 axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(
                     color=[(0.30, "#Df384f"), (0.50, "#B2B200"), (1, "green")], width=30))
                 # .add(radius="10%")
                 )

            .set_global_opts(
                legend_opts=opts.LegendOpts(pos_right="20%"),
                tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%")
            )
        )
        title_label_opts = opts.LabelOpts(font_size=15, color='red', font_family="Microsoft YaHei"),  # 给仪表盘里的标题设置颜色大小
        return chart_gauge_efficiency

    def add_bar_UPH(self):
        chart_bar_UPH = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK,
                                                         width="600px",
                                                         height="300px",
                                                         chart_id="UPH",
                                                         page_title="HP TE DashBoard"))

        chart_bar_UPH.add_xaxis(self.Hour)
        chart_bar_UPH.add_yaxis("UPH", self.UPH)
        chart_bar_UPH.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                type_="color",
                min_=0,
                max_=self.UPH_max,
                range_color=["#FF0000", "#B7B700", "#009B42"]
            ),
            legend_opts=opts.LegendOpts(pos_bottom="5%")
        )
        return chart_bar_UPH
        # self.chart_bar_UPH.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))

    def show(self):
        # self.chart_gauge_FPY.render("FPY.html")
        # self.chart_bar_UPH.render("UPH.html")
        # self.chart_gauge_efficiency.render("Efficiency.html")
        #page = Page()
        #自适应配置模式
        page = Page(layout=Page.DraggablePageLayout)
        #grid = Grid()
        # grid.add(self.add_gauge_FPY(), grid_opts=opts.GridOpts(pos_bottom="0.1%"))
        # grid.add(self.add_gauge_efficiency(), grid_opts=opts.GridOpts(pos_right="100%"))
        page.add(
            self.add_gauge_FPY(),
            self.add_gauge_efficiency(),
            self.add_bar_UPH()
        )
        page.page_title = "ShowChart"
        #生成html页面
        page.render("page_default_layout.html")
        #通过json配置重载html页面
        Page.save_resize_html("page_default_layout.html", cfg_file="chart_config.json", dest="Show_charts.html")


if __name__ == '__main__':
    chart1 = show_chart()
    chart1.init()
    # chart1.add_gauge_FPY()
    # chart1.add_bar_UPH()
    # chart1.add_gauge_efficiency()
    chart1.show()
