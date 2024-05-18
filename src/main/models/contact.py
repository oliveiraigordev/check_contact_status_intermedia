from src.main.database.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.main.models.company import Company


class Contact(db.Model):
    __tablename__ = "contact"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    company_id: Mapped[int] = mapped_column(ForeignKey('company.id'))
    company: Mapped[Company] = relationship("Company", back_populates="contacts")
    number: Mapped[str] = mapped_column(unique=True)
    active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self):
        return f'<Company {self.company_id.name} {self.number}>'
