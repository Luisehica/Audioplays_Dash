import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text

import json

### Setup database
with open('credentials.json', 'r') as json_file:
    credentials = json.load(json_file)

sql_engine = create_engine(f"postgresql://{credentials['user']}:{credentials['password']}@{credentials['host']}:{credentials['port']}/{credentials['dbname']}")


def runQuery(sql):
    result = sql_engine.connect().execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())

### Querys
# Users suscribed
def users_suscribed(start, end):
    df_suscribed = runQuery(f"""
        WITH users_suscribed AS (
            SELECT id
            FROM users
            WHERE has_been_subscribed
        ),
        first_time_played(user_id, month_date) AS (
            SELECT DISTINCT ap.user_id
            , DATE_TRUNC('month', FIRST_VALUE(ap.created_at) OVER (PARTITION BY ap.user_id ORDER BY ap.created_at))::date
            FROM audiobook_plays ap
            INNER JOIN users_suscribed us
            ON ap.user_id = us.id
            WHERE ap.created_at BETWEEN '{start}'::TIMESTAMP AND '{end}'::TIMESTAMP
        )
        SELECT CONCAT(DATE_PART('year', month_date), '-',DATE_PART('month', month_date)) AS month_year
        FROM first_time_played;
    """)

    return df_suscribed


