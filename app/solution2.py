from datetime import datetime

from sqlalchemy import create_engine, text

from db.config import DatabaseSettings

with create_engine(DatabaseSettings().url).connect() as conn:
    statement = text(
        """UPDATE full_name
    SET status = (
        SELECT short_name.status
        FROM short_name
        WHERE short_name.name = SPLIT_PART(full_name.name, '.', 1)
    );
    """
    )

    start_time = datetime.utcnow()
    conn.execute(statement)
    end_time = datetime.utcnow()
    conn.commit()

print(end_time - start_time)
