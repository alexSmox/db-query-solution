from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class ShortName(Base):
    __tablename__ = "short_name"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False)


class FullName(Base):
    __tablename__ = "full_name"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=True)
