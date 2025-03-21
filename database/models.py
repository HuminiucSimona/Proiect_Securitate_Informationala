from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Key(Base):
    __tablename__ = 'keys'
    id = Column(Integer, primary_key=True)
    key_encrypted = Column(String, nullable=False)
    algorithm_id = Column(Integer, ForeignKey('algorithms.id', ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    algorithm = relationship("Algorithm", back_populates="keys")

    def __repr__(self):
        return f'''<Key(id={self.id}, 
                key_encrypted={self.key_encrypted}, 
                algorithm_id={self.algorithm_id})>'''
    
class Algorithm(Base):
    __tablename__ = 'algorithms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    keys = relationship("Key", back_populates="algorithm", cascade="all, delete")
    files = relationship("File", back_populates="algorithm", cascade="all, delete")

    def __repr__(self):
        return f'''<Algorithm(id={self.id},
                name={self.name})>'''

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    file_path = Column(String, nullable=False)
    encrypted = Column(Boolean, default=False)
    algorithm_id = Column(Integer, ForeignKey('algorithms.id', ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    algorithm = relationship("Algorithm", back_populates="files")

    def __repr__(self):
        return f'''<File(id={self.id}, 
                path={self.file_path}, 
                encrypted={self.encrypted})>'''

class PerformanceMetric(Base):
    __tablename__ = 'performance_metrics'
    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id', ondelete="CASCADE"), nullable=False)
    encryption_time = Column(Float, nullable=False)
    decryption_time = Column(Float, nullable=False)
    memory_usage = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    file = relationship("File", cascade="all, delete")

    def __repr__(self):
        return f'''<PerformanceMetric(id={self.id}, 
            enc_time={self.encryption_time}, 
            dec_time={self.decryption_time})>'''
#parolaproiectSI