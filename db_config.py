
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = "postgresql://root:rdr@localhost:5432/dummy"
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)