from models import Framework, Key, PerformanceMetric, Algorithm, File, Base
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from config import DATABASE_URL
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
db = next(get_db())

def create_framework(db: Session, name : str):
    try:
        framework = Framework(name=name)
        db.add(framework)
        db.commit()
        db.refresh(framework)
        print(f"Created: {framework}")
        return framework
    except IntegrityError as e:
        db.rollback()
        print(f"Integrity error: The framework '{name}' already exists or invalid data.")
        return None
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemy error: {str(e)}")
        return None
    except Exception as e:
        db.rollback()
        print(f"Unexpected error: {str(e)}")
        return None
    
def get_frameworks(db: Session):
    return db.query(Framework).all()

def get_framework(db: Session, framework_id: int):
    return db.query(Framework).filter(Framework.id == framework_id).first()

def update_framework(db: Session, framework_id: int, new_name: str):
    try:
        framework = db.query(Framework).filter(Framework.id == framework_id).first()
        if not framework:
            print(f"No framework found with ID {framework_id}")
            return None
        framework.name = new_name
        db.commit()
        db.refresh(framework)
        print(f"Updated: {framework}")
        return framework
    except IntegrityError:
        db.rollback()
        print(f"Integrity error: The name '{new_name}' might already exist.")
        return None
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemy error: {str(e)}")
        return None
    
def delete_framework(db: Session, framework_id: int):
    try:
        framework = db.query(Framework).filter(Framework.id == framework_id).first()
        if not framework:
            print(f"No framework found with ID {framework_id}")
            return False
        db.delete(framework)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemy error: {str(e)}")
        return False
