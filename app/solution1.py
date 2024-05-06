from datetime import datetime

from sqlalchemy import create_engine, text

from db.config import DatabaseSettings

with create_engine(DatabaseSettings().url).connect() as conn:
    statement = text(
        """WITH name_status AS (
    SELECT sn.status, fn.name
    FROM full_name fn
    JOIN short_name sn ON sn.name = SPLIT_PART(fn.name, '.', 1) 
        )
        UPDATE full_name
        SET status = ns.status
        FROM name_status ns
        WHERE full_name.name = ns.name;"""
    )

    start_time = datetime.utcnow()
    conn.execute(statement)
    end_time = datetime.utcnow()
    conn.commit()

print(end_time - start_time)
