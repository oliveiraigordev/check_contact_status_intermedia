from typing import List
from src.main.database.database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Company(db.Model):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    name: Mapped[str]
    responsible: Mapped[str]
    email: Mapped[str]
    active: Mapped[bool] = mapped_column(default=True)
    contacts: Mapped[List["Contact"]] = relationship("Contact", back_populates="company", cascade="all, delete")

    def __repr__(self):
        return f'<Company {self.name}>'
