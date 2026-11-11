
class Owner:

    def __init__(self, nic: str, name: str, address: str):
        self.nic = nic
        self.name = name
        self.address = address

class DataPlan:

    def __init__(self, phone_no: str, owner: Owner, data_gb: str):
        self.__phone_no = phone_no
        self.__owner = owner
        self.__data_gb = data_gb

    def get_phone_no(self):
        return self.__phone_no

    def get_owner_nic(self):
        return self.__owner.nic