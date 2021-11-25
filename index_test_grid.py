from pyecharts import options as opts
from pyecharts.charts import Grid, Line, Scatter
from pyecharts.faker import Faker
from pyecharts.charts import Bar, Page, Grid, Pie
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker

from pyecharts.charts import Gauge

def theme_infographic() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-infographic"))
    )
    return c



def theme_macarons() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-macarons"))
    )
    return c
def pie_rosetype() -> Pie:
    v = Faker.choose()
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    )
    return c


grid = (
    Grid()
    .add(theme_macarons(), grid_opts=opts.GridOpts(pos_left="55%"))
    .add(theme_infographic(), grid_opts=opts.GridOpts(pos_right="55%"))
    .render("grid_horizontal.html")
)