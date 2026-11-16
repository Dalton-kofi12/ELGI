from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        UniqueConstraint(
            "organisation_id",
            "email",
            name="uq_user_organisation_email",
        ),
        CheckConstraint(
            "role IN ('student', 'teacher', 'admin', 'owner')",
            name="ck_user_valid_role",
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    organisation_id = Column(
        Integer,
        ForeignKey("organisations.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    full_name = Column(
        String(200),
        nullable=False,
    )

    email = Column(
        String(255),
        nullable=False,
    )

    password_hash = Column(
        String(255),
        nullable=False,
    )

    role = Column(
        String(20),
        nullable=False,
        default="student",
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_verified = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True,
    )

    def __repr__(self):
        return f"<User(email='{self.email}', role='{self.role}')>"
