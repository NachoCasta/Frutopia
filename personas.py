class MetaPersona(type):
    
    personas = []

    def __call__(cls, *args, **kw):
        print(args)
        for persona in cls.personas:
            if persona.nombre == args[0] and \
               persona.apellido == args[1]:
                return persona
        instancia = super().__call__(*args, **kw)
        cls.personas.append(instancia)
        return instancia

class Persona(metaclass=MetaPersona):

    def __init__(self, nombre, apellido, telefono=None, mail=None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail

    def __repr__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Vendedor(Persona):

    def __init__(self, nombre, apellido, telefono=None, mail=None):
        super().__init__(nombre, apellido, telefono, mail)


class JefeDeGrupo(Persona):

    last_id = 0

    def __init__(self, nombre, apellido, telefono=None, mail=None):
        super().__init__(nombre, apellido, telefono, mail)
        JefeDeGrupo.last_id += 1
        self.grupo = JefeDeGrupo.last_id
        self.vendedores = []
        self.deudas = []

class Trabajador(Persona):

    def __init__(self, nombre, apellido, trabajo, paga, telefono=None, mail=None):
        super().__init__(nombre, apellido, telefono, mail)
        self.trabajo = trabajo
