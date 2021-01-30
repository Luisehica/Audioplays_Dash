# Beak Data Challenge - Data Analyst
## Database exploration and analysis


```python
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text


### Setup the database server
credentials = {
    'host':'35.227.110.100',
    'dbname':'postgres',
    'user':'postgres',
    'password':'n$EYUJRrmZ9jz2>7o',
    'port':'5432'
}

sql_engine = create_engine(f"postgresql://{credentials['user']}:{credentials['password']}@{credentials['host']}:{credentials['port']}/{credentials['dbname']}")

def runQuery(sql):
    result = sql_engine.connect().execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())
```

## 1. Top Ten

### Users


```python
runQuery("""
SELECT user_id, SUM(seconds) as Total_time
FROM audiobook_plays
GROUP BY user_id
ORDER BY Total_time DESC
LIMIT 10;
""")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>total_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>876083</td>
      <td>1685061.545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>954745</td>
      <td>1295564.176</td>
    </tr>
    <tr>
      <th>2</th>
      <td>829232</td>
      <td>920223.793</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53930</td>
      <td>901351.575</td>
    </tr>
    <tr>
      <th>4</th>
      <td>967058</td>
      <td>823700.546</td>
    </tr>
    <tr>
      <th>5</th>
      <td>980108</td>
      <td>751762.359</td>
    </tr>
    <tr>
      <th>6</th>
      <td>844824</td>
      <td>670955.438</td>
    </tr>
    <tr>
      <th>7</th>
      <td>958114</td>
      <td>604498.961</td>
    </tr>
    <tr>
      <th>8</th>
      <td>527831</td>
      <td>601459.086</td>
    </tr>
    <tr>
      <th>9</th>
      <td>910357</td>
      <td>594632.452</td>
    </tr>
  </tbody>
</table>
</div>



### Audiobooks


```python
runQuery("""
    SELECT audiobook_id, SUM(seconds) as Total_time
    FROM audiobook_plays
    GROUP BY audiobook_id
    ORDER BY Total_time DESC
    LIMIT 10;
""")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>audiobook_id</th>
      <th>total_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>308346</td>
      <td>5025181.050</td>
    </tr>
    <tr>
      <th>1</th>
      <td>238952</td>
      <td>4092814.217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>249087</td>
      <td>3022995.480</td>
    </tr>
    <tr>
      <th>3</th>
      <td>223467</td>
      <td>2483408.005</td>
    </tr>
    <tr>
      <th>4</th>
      <td>223494</td>
      <td>2465606.344</td>
    </tr>
    <tr>
      <th>5</th>
      <td>223329</td>
      <td>2118576.488</td>
    </tr>
    <tr>
      <th>6</th>
      <td>105720</td>
      <td>2118238.976</td>
    </tr>
    <tr>
      <th>7</th>
      <td>243851</td>
      <td>1745427.782</td>
    </tr>
    <tr>
      <th>8</th>
      <td>182131</td>
      <td>1632881.546</td>
    </tr>
    <tr>
      <th>9</th>
      <td>202942</td>
      <td>1492383.766</td>
    </tr>
  </tbody>
</table>
</div>



## 2. Weakly Unique Active Users


```python
runQuery("""
    WITH WAU (year, weekly, user_id) AS (
        SELECT date_part('year', created_at::date),
        date_part('week', created_at::date),
        user_id
        FROM audiobook_plays
    )
    SELECT year,
        weekly,
        COUNT(DISTINCT user_id)
    FROM WAU
    GROUP BY year, weekly
    ORDER BY year, weekly
    LIMIT 50;
""")

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>weekly</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018.0</td>
      <td>1.0</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018.0</td>
      <td>49.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018.0</td>
      <td>50.0</td>
      <td>36</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018.0</td>
      <td>51.0</td>
      <td>86</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018.0</td>
      <td>52.0</td>
      <td>161</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2019.0</td>
      <td>1.0</td>
      <td>167</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2019.0</td>
      <td>2.0</td>
      <td>235</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019.0</td>
      <td>3.0</td>
      <td>544</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2019.0</td>
      <td>4.0</td>
      <td>663</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2019.0</td>
      <td>5.0</td>
      <td>557</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2019.0</td>
      <td>6.0</td>
      <td>454</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2019.0</td>
      <td>7.0</td>
      <td>458</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2019.0</td>
      <td>8.0</td>
      <td>371</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2019.0</td>
      <td>9.0</td>
      <td>316</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2019.0</td>
      <td>10.0</td>
      <td>325</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2019.0</td>
      <td>11.0</td>
      <td>355</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2019.0</td>
      <td>12.0</td>
      <td>400</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2019.0</td>
      <td>13.0</td>
      <td>348</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2019.0</td>
      <td>14.0</td>
      <td>392</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2019.0</td>
      <td>15.0</td>
      <td>261</td>
    </tr>
  </tbody>
</table>
</div>



## 3. Week over week retention rate of active users


```python
runQuery("""
    WITH user_week_date(user_id, 
        current_date_, prev_date) AS (
        SELECT DISTINCT
            abp.user_id,
            cw.current_week,
            (cw.current_week - INTERVAL '7 days')::date
        FROM audiobook_plays abp,
            LATERAL(SELECT DISTINCT abp.user_id, DATE_TRUNC('week',created_at)::date AS current_week) cw
        ORDER BY user_id, cw.current_week
    ),
    user_week_active AS (
        SELECT *,
            LAG(current_date_) OVER(PARTITION BY user_id ORDER BY current_date_) AS last_week
        FROM user_week_date uwa
    ),
    user_retention AS (
        SELECT *, 
            prev_date=last_week AS retained
        FROM user_week_active
    ),
    WAU AS (
        SELECT current_date_, 
        COUNT(1) AS total_users,
        COUNT(CASE WHEN retained THEN 1 END) AS active_users
        FROM user_retention
        GROUP BY current_date_
        ORDER BY current_date_
    )
    SELECT current_date_ AS week, 
        total_users,
        active_users,
        ROUND(active_users::numeric/total_users*100, 2) AS retention_rate
    FROM WAU;
""")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>week</th>
      <th>total_users</th>
      <th>active_users</th>
      <th>retention_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-12-03</td>
      <td>11</td>
      <td>0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-12-10</td>
      <td>36</td>
      <td>6</td>
      <td>16.67</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-12-17</td>
      <td>86</td>
      <td>13</td>
      <td>15.12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-12-24</td>
      <td>161</td>
      <td>57</td>
      <td>35.40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-12-31</td>
      <td>186</td>
      <td>94</td>
      <td>50.54</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2019-01-07</td>
      <td>235</td>
      <td>83</td>
      <td>35.32</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2019-01-14</td>
      <td>544</td>
      <td>129</td>
      <td>23.71</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019-01-21</td>
      <td>663</td>
      <td>260</td>
      <td>39.22</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2019-01-28</td>
      <td>557</td>
      <td>290</td>
      <td>52.06</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2019-02-04</td>
      <td>454</td>
      <td>226</td>
      <td>49.78</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2019-02-11</td>
      <td>458</td>
      <td>188</td>
      <td>41.05</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2019-02-18</td>
      <td>371</td>
      <td>200</td>
      <td>53.91</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2019-02-25</td>
      <td>316</td>
      <td>173</td>
      <td>54.75</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2019-03-04</td>
      <td>325</td>
      <td>153</td>
      <td>47.08</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2019-03-11</td>
      <td>355</td>
      <td>169</td>
      <td>47.61</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2019-03-18</td>
      <td>400</td>
      <td>200</td>
      <td>50.00</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2019-03-25</td>
      <td>348</td>
      <td>193</td>
      <td>55.46</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2019-04-01</td>
      <td>392</td>
      <td>182</td>
      <td>46.43</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2019-04-08</td>
      <td>261</td>
      <td>167</td>
      <td>63.98</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Average time listened last 30 days


```python

```




```python

```
