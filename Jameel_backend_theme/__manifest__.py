{
    "name": "Jameel backend Theme",
    "version": "18.0",
    "description": "Minimalist and elegant backend "
                   "theme for Odoo 18, Backend Theme",
    "summary": "Jameel Backend Theme is an attractive theme for backend",
    "category": "Themes/Backend",
    'author': 'llmarifa',
    'company': 'llmarifa',
    'maintainer': 'llmarifa',
    'currency': 'USD',
    'price': '80.00',
    'website': "https://www.llmarifa.co",
    "depends": ['base', 'web', 'mail'],
    "currency": 'USD',
    "price": '80.00',
    "data": [
        'views/layout.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'jameel_backend_theme/static/src/scss/login.scss',
        ],
        'web.assets_backend': [
            'jameel_backend_theme/static/src/scss/variables.scss',
            'jameel_backend_theme/static/src/scss/navigation_bar.scss',
            'jameel_backend_theme/static/src/scss/override.scss',
            'jameel_backend_theme/static/src/scss/style.scss',
            'jameel_backend_theme/static/src/xml/styles.xml',
        ],
    },
    'images': [
        'static/description/icon.png',
        'static/description/banner.jpg',
    ],
    'icon': 'static/description/icon.png',
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
