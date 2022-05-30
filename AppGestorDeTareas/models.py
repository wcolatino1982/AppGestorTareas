import db
from sqlalchemy import Column, Integer, String, Boolean, CHAR, Date


class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    categoria = Column(CHAR(20))
    fecha = Column(Date)
    hecha = Column(Boolean)

    def __init__(self, contenido, categoria, fecha, hecha):
        # el id se crea automaticamente
        self.contenido = contenido
        self.categoria = categoria
        self.fecha = fecha
        self.hecha = hecha

    def __fechaFormateada__(self):
        fechaFormateada = self.fecha.strftime('%d-%m-%Y')
        return "{}".format(fechaFormateada)

    def __str__(self):
        return "Tarea {}: {} de {} ({})".format(self.id, self.contenido, self.categoria, self.hecha)

