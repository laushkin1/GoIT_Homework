from database.models import Base
from database.db import engine
from seed import make_seed

if __name__ == "__main__":
    Base.metadata.bind = engine
    make_seed()
    #After runing this file go to run_select.py