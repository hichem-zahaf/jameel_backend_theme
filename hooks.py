import base64
from odoo import tools


def process_menu_item(menu):
    """
       Process a menu item by updating its web_icon_data.
       param:
           menu (record): The menu item to process.
       """
    menu_list = [
        'Contacts', 'Link Tracker', 'Dashboards', 'Sales', 'Invoicing',
        'Inventory', 'Purchase', 'Calendar', 'Point of Sale', 'Website',
        'Notes', 'CRM', 'Surveys', 'Project', 'SMS Marketing',
        'Email Marketing', 'Repairs', 'Manufacturing', 'Timesheets',
        'Fleet', 'Lunch', 'Live Chat', 'Maintenance', 'Expenses', 'Time Off',
        'Attendances', 'Recruitment', 'Employees', 'Members', 'eLearning',
        'Events'
    ]
    if menu.name not in menu_list:
        return
    img_path = tools.misc.file_path(
        f'jameel_backend_theme/static/src/img/icons/{menu.name}.png')
    with open(img_path, "rb") as img_file:
        menu.write({'web_icon_data': base64.b64encode(img_file.read())})


def init_hooks(env):
    """
        Initialize hooks by updating the web_icon_data of certain menus.
        param:
            env (Environment): Odoo environment.
        """
    menu_item = env['ir.ui.menu'].search([('parent_id', '=', False)])
    for menu in menu_item:
        process_menu_item(menu)
