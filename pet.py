class Pet:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __str__(self):
        return "id={id_value} ; name={name_value}".format(id_value=self.id, name_value=self.name)
