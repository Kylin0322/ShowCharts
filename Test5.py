# 柱状图
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

# V1 版本开始支持链式调用
# 你所看到的格式其实是 `black` 格式化以后的效果
# 可以执行 `pip install black` 下载使用

# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )
# bar.render()


bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
bar.render()

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("每小时产量", Faker.days_values, color=Faker.rand_color())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),
        datazoom_opts=opts.DataZoomOpts(type_="inside"),
    )
    # .render("bar_datazoom_inside.html")
    .render("bar_datazoom_inside.html")
)
