def getRole(user):
    role_map = {
        'customer': 'Customer',
        'stylist': 'Stylist',
        'admin': 'Admin',
    }
    return role_map.get(getattr(user, 'role', ''), 'Unknown')
