from rolepermissions.roles import AbstractUserRole

class People(AbstractUserRole):
    available_permissions = {
        'make_tranfer' : True,
        'receive_transfer' : True,
         
    }
    
class Company(AbstractUserRole):
    available_permissions = {
        'make_transfer' : False,
        'receive_transfer' : True,
    }