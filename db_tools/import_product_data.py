__author__ = 'Flynn'
__date__ = '2020/4/10 16:31'

import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + '../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MxShop1.settings')

import django

django.setup()

from goods.models import Goods, GoodsCategory, GoodsImage

from db_tools.data.product_data import row_data

for good in row_data:
    good_detail = Goods()
    good_detail.name = good['name']
    good_detail.market_price = float(good['market_price'].replace('￥', '').replace('元', ''))
    good_detail.sale_price = float(good['sale_price'].replace('￥', '').replace('元', ''))
    good_detail.goods_brief = good['desc'] if good['desc'] is not None else ''
    good_detail.goods_desc = good['goods_desc'] if good['goods_desc'] is not None else ''
    good_detail.goods_front_image = good['images'][0] if good['images'] else ''

    c_name = good['categorys'][-1]
    category = GoodsCategory.objects.filter(name=c_name)
    if category:
        good_detail.category = category[0]

    good_detail.save()

    for goods_image in good['images']:
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = good_detail
        goods_image_instance.save()
