from sqlalchemy.orm import Session

import models, schemas

#crud cho doi xe

def get_doi_xe(db: Session, id: int):
    return db.query(models.Doi_xe).filter(models.Doi_xe.id == id).first()


def get_all_doi_xe(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doi_xe).offset(skip).limit(limit).all()


def create_doi_xe(db: Session, doi_xe: schemas.Doi_xe_Create):
    db_doi_xe = models.Doi_xe(ten_doi_xe=doi_xe.ten_doi_xe)
    db.add(db_doi_xe)
    db.commit()
    db.refresh(db_doi_xe)
    return db_doi_xe

def update_doi_xe(db: Session, doi_xe_id:int , ten_doi_xe : str):
    db_doi_xe=get_doi_xe(db=db, doi_xe_id=doi_xe_id)
    db_doi_xe.ten_doi_xe=ten_doi_xe
    db.commit()
    db.refresh(db_doi_xe)
    return db_doi_xe

def delete_doi_xe (db: Session , id:int):
        db_doi_xe = get_doi_xe(db=db , id=id)
        db.delete(db_doi_xe)
        db.commit()

#crud cho xe
def get_xe(db: Session, xe_id:int):
    return db.query(models.Xe).filter(models.Xe.id == xe_id).first()

def get_all_xe(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Xe).offset(skip).limit(limit).all()

def create_doi_xe(db:Session, xe: schemas.Xe_Create):
    db_xe = models.Xe(ten_xe=xe.ten_xe)
    db.add(db_xe)
    db.commit()
    db.refresh(db_xe)
    return db_xe

def update_xe(db:Session, xe_id:int , ten_xe : str):
    db_xe=get_xe(db=db, xe_id=xe_id)
    db_xe.ten_xe = ten_xe
    db_xe.xe_id = xe_id
    db.commit()
    db.refresh(db_doi_xe)
    return db_doi_xe

def delete_xe (db:Session , id:int):

    db_xe = get_xe(db=db , xe_id=xe_id)
    db.delete(db_tai_xe)
    db.commit()


#Crud cho tai xe
def get_tai_xe(db:Session, tai_xe_id:int):
    return db.query(models.Tai_xe).filter(models.Tai_xe.id == tai_xe_id).first()

def get_all_tai_xe(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tai_xe).offset(skip).limit(limit).all()

def create_tai_xe(db:Session, tai_xe: schemas.Tai_xe_Create):
    db_tai_xe = models.Tai_xe(ten_tai_xe=tai_xe.ten_tai_xe)
    db.add(db_tai_xe)
    db.commit()
    db.refresh(db_tai_xe)
    return db_tai_xe

def update_tai_xe(db:Session, _id:int , ten_tai_xe : str ):
    db_tai_xe=get_tai_xe(db=db, id=id)
    db_tai_xe.ten_tai_xe = ten_tai_xe
    db.commit()
    db.refresh(db_doi_xe)
    return db_doi_xe

def delete_tai_xe (db:Session , id:int):

    db_tai_xe = get_tai_xe(db=db , id=id)
    db.delete(db_tai_xe)
    db.commit()

#crud cho chuyen xe
def get_chuyen_xe(db:Session, id:int):
    return db.query(models.Chuyen_xe).filter(models.Chuyen_xe.id == id).first()

def get_all_chuyen_xe(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Chuyen_xe).offset(skip).limit(limit).all()

def create_chuyen_xe(db:Session, tai_xe: schemas.Tai_xe_Create):
    db_chuyen_xe = models.Chuyen_xe(ten_tai_xe=tai_xe.ten_tai_xe)
    db.add(db_tai_xe)
    db.commit()
    db.refresh(db_tai_xe)
    return db_tai_xe

def update_chuyen_xe(db:Session, _id:int , ten_chuyen_xe : str ):
    db_chuyen_xe=get_chuyen_xe(db=db, id=id)
    db_chuyen_xe.ten_chuyen_xe = ten_chuyen_xe
    db.commit()
    db.refresh(db_chuyen_xe)
    return db_chuyen_xe

def delete_chuyen_xe (db:Session , id:int):

    db_chuyen_xe = get_chuyen_xe(db=db , id=id)
    db.delete(db_chuyen_xe)
    db.commit()