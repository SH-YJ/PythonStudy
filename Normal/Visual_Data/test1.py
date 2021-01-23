from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot

bar = Bar("我的第一个图表")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.add("鞋子",["衬", "羊衫", "纺衫", "裤", "高鞋", "袜"],[5, 20, 36, 10, 75, 90], is_more_utils=True)
bar.render('Source/2.html')

