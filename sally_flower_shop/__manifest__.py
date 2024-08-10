#-*- coding:utf-8 -*-
{
    'name': 'Sally Flower Shop',
    'installable': True,
    'depends': [
        'base',
        'product',
        'sale',
        'website_sale',
        'stock',
    ],
    'data': [
        'data/groups.xml',
        'security/ir.model.access.csv',
        'views/flower_views.xml',
        'views/product_views.xml',
        'views/sale_order_lines_views.xml',
        'views/flower_templates.xml',
        'views/stock_production_lot_views.xml',
        'views/flower_water_views.xml',
        'views/weather_api.xml',
        'report/flower_sale_order_view.xml',
        'report/paperformat_flower_sale_order.xml',
        'report/report_action_flower_sale_order.xml',
        'report/sale_order_form_button.xml',
    ],
    'application': True,
    
}
