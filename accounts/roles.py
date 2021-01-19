from rolepermissions.roles import AbstractUserRole

class Operations(AbstractUserRole):
    available_permission = {
        'edit_product': True,
        'read_product': True,
        'update_product': True
    }

class SystemAdmin(AbstractUserRole):
    available_permissions = {
        'edit_user': True,
        'read_user': True,
        'update_user': True,
        'edit_product': True,
        'read_product': True,
        'update_product': True
    }

class Finance(AbstractUserRole):
    available_permissions = {
        'edit_finance': True
    }