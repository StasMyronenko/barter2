from config.db import Session


async def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
