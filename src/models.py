from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }


class Publicacion(db.Model):
    __tablename__ = "Publicaciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"))


class Comentario(db.Model):
    __tablename__ = "Comentarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("Publicaciones.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"))
    text_coment: Mapped[str] = mapped_column(String(120))


class Seguidor(db.Model):
    __tablename__ = "seguidores"

    usuario_to_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"), primary_key=True)
    usuario_from_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"), primary_key=True)


class Media(db.Model):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(80), nullable=False)
    url: Mapped[str] = mapped_column(String(200), nullable=False)
    Post_id: Mapped[int] = mapped_column(ForeignKey("Publicaciones.id"))