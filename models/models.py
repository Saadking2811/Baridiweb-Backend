from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String)
    email = Column(String, unique=True)
    phoneNumber = Column(String, nullable=False)
    hashedPassword = Column(String)
    isAdmin = Column(Boolean, default=False)
    isActive = Column(Boolean, default=False)
    cle = Column(String, default="")
    ccp = Column(String, default="")

    # One-to-Many relationship with Document
    documents = relationship(
        "Document", 
        back_populates="owner", 
        overlaps="paymentProofs"
    )


class Document(Base):  # Ensure you have this base class
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    docType = Column(String, default="")
    filePath = Column(String)

    # Relationship back to User
    owner = relationship(
        "User", 
        back_populates="documents", 
        overlaps="paymentProofs"
    )
# Specialized documents extend the base class
class Check(Document):
    __tablename__ = "checks"
    id = Column(Integer, ForeignKey("documents.id"), primary_key=True)
    check_number = Column(String, nullable=False)
    amountInDigits = Column(String, nullable=False)
    amountInText = Column(String, nullable=False)

class IDCard(Document):
    __tablename__ = "Idcards"
    id=Column(Integer, ForeignKey("documents.id"),primary_key=True)
    idNumber=Column(String,nullable=False)
    firstName=Column(String,nullable=False)
    lastName=Column(String,nullable=False)
    issueDate=Column(String,nullable=False)

class CheckSecours(Document):
    __tablename__ = "check_secours"
    id = Column(Integer, ForeignKey("documents.id"), primary_key=True)
    amountInDigits = Column(String, nullable=False)
    amountInText = Column(String, nullable=False)
    senderFirstName = Column(String, nullable=False)
    senderLastName = Column(String, nullable=False)
    receiverFirstName = Column(String, nullable=False)
    receiverLastName = Column(String, nullable=False)
    receiverCle = Column(String, nullable=False)
    receiverCCP = Column(String, nullable=False)
    __mapper_args__ = {"polymorphic_identity": "check_secours"}
    
class PaymentOrder(Base):
    __tablename__ = "payment_orders"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    document_id = Column(String)
    amount = Column(Float)
    payment_type = Column(String)
