{
    "name": "Jameel Backend Theme",
    "version": "18.0",
    "description": "Minimalist and elegant backend "
                   "theme for Odoo 19, Backend Theme",
    "summary": "Jameel Backend Theme V19 is an attractive theme for backend",
    "category": "Themes/Backend",
    'author': 'llmarifa',
    'company': 'llmarifa',
    'maintainer': 'llmarifa',
    'website': "https://www.llmarifa.co",
    "depends": ['base', 'web', 'mail'],
    "data": [
        'views/icons.xml',
        'views/layout.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'jameel_backend_theme/static/src/scss/login.scss',
        ],
        'web.assets_backend': [
            # SCSS - Load in order (variables first, then components, then main style)
            'jameel_backend_theme/static/src/scss/variables.scss',
            'jameel_backend_theme/static/src/scss/components/_animations.scss',
            'jameel_backend_theme/static/src/scss/components/_buttons.scss',
            'jameel_backend_theme/static/src/scss/components/_tables.scss',
            'jameel_backend_theme/static/src/scss/components/_forms.scss',
            'jameel_backend_theme/static/src/scss/components/_cards.scss',
            'jameel_backend_theme/static/src/scss/components/_dialogs.scss',
            'jameel_backend_theme/static/src/scss/components/_navbar.scss',
            'jameel_backend_theme/static/src/scss/components/_responsive.scss',
            'jameel_backend_theme/static/src/scss/style.scss',
            # XML Templates
            'jameel_backend_theme/static/src/xml/styles.xml',
            'jameel_backend_theme/static/src/xml/sidebar.xml',
            'jameel_backend_theme/static/src/xml/top_bar.xml',
            # JavaScript (only NavBarJameel.js for sidebar functionality)
            'jameel_backend_theme/static/src/js/NavBarJameel.js',
        ],
    },
    'images': [
        'static/description/banner.jpg',
        'static/description/theme_screenshot.jpg',
    ],
    'icon': 'static/description/icon.png',
    'license': 'MIT',
    'pre_init_hook': 'init_hooks',
    'post_init_hook': 'init_hooks',
    'installable': True,
    'application': False,
    'auto_install': False,
}
