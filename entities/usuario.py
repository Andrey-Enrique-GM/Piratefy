from dataclasses import dataclass
from typing import Optional



@dataclass
class Usuario:
    nombre: str
    email: str
    password: str
    id: Optional[int] = None


    @classmethod
    def from_row(cls, row: dict) -> "Usuario":
        return cls(
            id=row.get("id"),
            nombre=row["nombre"],
            email=row["email"],
            password=row["password"],
        )


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
        }
    