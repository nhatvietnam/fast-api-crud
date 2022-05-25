from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Doi_xe(Base):
    __tablename__="Doi_xe"
    id = Column(Integer, primary_key=True)
    ten_doi_xe = Column(String(80))
    #doi xe lien ket 1 to many voi xe
    #xe_id = relationship('Xe' , backref='doi_xe' , lazy = True)
    xe_id = relationship("Xe" , back_populates= "doi_xe_id")

class Xe(Base):
    __tablename__ = 'Xe'
    id = Column(Integer, primary_key=True)
    ten_xe = Column(Text)

    #lien ket voi doi xe 
    doi_xe_id = relationship( "Doi_xe" , back_populates = "xe_id")    
    
    #doi xe lien ket many to many voi tai xe
    xe_tai_xe = relationship( "Tai_xe" , back_populates ="tai_xe_xe")

class Tai_xe(Base):
    __tablename__ = 'Tai_xe'
    id = Column(Integer, primary_key=True)
    ten_tai_xe = Column(Text)
    tai_xe_xe = relationship( "Xe" , back_populates ="xe_tai_xe")

   
    #lien ket voi chuyen xe theo many to many

    tai_xe_chuyen_xe = relationship( "Chuyen_xe" , back_populates ="chuyen_xe_tai_xe")


class Chuyen_xe(Base):
    __tablename__ = 'Chuyen_xe'
    id = Column(Integer, primary_key=True)
    ten_chuyen_xe=Column(Text)
    chuyen_xe_tai_xe = relationship( "Tai_xe" , back_populates ="tai_xe_chuyen_xe")


    