from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge(init_opts = opts.InitOpts(width = '800px',height = '400px'))  #设置GAUGE的大小
    .add(
            "这是仪表盘上方中间的标题",[("仪表里标题-完成率",88.88)],radius = "80%",  #radius 设置半径大小
            split_number = 20,  #设置仪表盘的刻度有多少，这里设置分成20份，每份是5%
            title_label_opts = opts.LabelOpts(
                    font_size = 15, color = 'red',font_family = "Microsoft YaHei" ),  #给仪表盘里的标题设置颜色大小
            axisline_opts = opts.AxisLineOpts(
                    linestyle_opts= opts.LineStyleOpts(
                            color = [(0.3, "#ffb6b9"), (0.7, "#fae3d9"), (1, "#bbded6")], width=30) 
                                    #设置仪表盘的颜色，分别是30%,70%,和100%的，分成三段！圆环的宽度！
            ),)
    .set_global_opts(
         title_opts = opts.TitleOpts(title = "这是左上方的大标题"),
         toolbox_opts = opts.ToolboxOpts(),  #显示右上角的工具栏
         legend_opts = opts.LegendOpts(is_show = True), #如果这里选False的话，那么"这是仪表盘上方中间的标题"就不显示了
         tooltip_opts = opts.TooltipOpts(is_show = True, formatter ="{a} <br/>{b} : {c}%" ),
         )
    #这里可以调整仪表盘的颜色和粗细！！
#    .set_series_opts(  
#            axisline_opts=opts.AxisLineOpts(
#                    linestyle_opts =opts.LineStyleOpts(
#                            color = [[0.2,'#00dffc'],[0.8,'#008c9e'],[1,'#005f6b']],width = 35)))
    .render(r'gauge_base2.html')
)