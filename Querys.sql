-- 1
-- Top ten users with more audio time listened
SELECT user_id, SUM(seconds) as Total_time
FROM audiobook_plays
GROUP BY user_id
ORDER BY Total_time DESC
LIMIT 10;

-- Top ten audiobooks with more audio time listened
SELECT audiobook_id, SUM(seconds) as Total_time
FROM audiobook_plays
GROUP BY audiobook_id
ORDER BY Total_time DESC
LIMIT 10;

-- 2
-- Dates between audiobook_plays table
SELECT MIN(created_at), MAX(created_at)
FROM audiobook_plays
LIMIT 10;

-- Weekly Unique Active Users
SELECT date_part('year', created_at) as Year,
    date_part('week', created_at) as Week,
    date_trunc('week', created_at)::date as Week_date,
    COUNT(DISTINCT(user_id)) as Users
FROM audiobook_plays
GROUP BY Year, Weekly, _week
ORDER BY Year, Weekly;

-- 3 Falta terminar
-- Week over Week retention rato of active user
WITH WAU (Year, Weekly, User_id)
AS (
    SELECT date_part('year', created_at::date),
    date_part('week', created_at::date),
    user_id
    FROM audiobook_plays
)
SELECT WAU.Year, WAU. Weekly, WAU.User_id
FROM WAU
LIMIT 10;

-- solución chato
with semanas as (
	select distinct 
	user_id 
	, date_trunc('week',created_at)::date as semana
	from audiobook_plays ap 
	order by user_id, semana 
)


, sem_anterior as (
	select 
	user_id
	, semana as semana_actual
	, lag(semana) over (partition by user_id order by semana asc) as semana_anterior
	from semanas
)

, comparacion as (
	select *
	, case when (semana_anterior is null or (semana_actual - semana_anterior) > 7) then false
		else true end as retention
	from sem_anterior
	)
	
	
select 
semana_actual
, total_users
, usuarios_retenidos
, (usuarios_retenidos::float / total_users::float)*100 as rate
from (
	select 
	semana_actual
	, count(distinct case when retention then user_id end ) usuarios_retenidos
	from comparacion
	group by 1
	) ret
left join (
	select 
	semana as semana_anterior
	, count(distinct user_id) as total_users
	from semanas
	group by 1
	) act
on ret.semana_actual = act.semana_anterior;

--

SELECT * 

-- 4 
-- Average Hours_played_last_30_days
WITH dummy_query (last_date)
AS (
    SELECT MAX(created_at)
    FROM audiobook_plays
)
SELECT user_id, ROUND(AVG(seconds/60),2) AS Hours_played_last_30_days
FROM audiobook_plays, dummy_query
WHERE created_at > (dummy_query.last_date - interval '30 days')
GROUP BY user_id
ORDER BY Hours_played_last_30_days DESC

-- 5
-- Month over month growth (%)

SELECT *
FROM 
LIMIT 10

-- 6
-- Distribution per month of user suscribed





--Querys for user-audiobook-book_category[1]
SELECT u.id as User_id, u.gender as Gender,
    ab.id as Book_id, ab.actual_size, ab.grade_level, ab.language,
    abp.seconds as time_listened,
    bc.name
FROM audiobook_plays abp
INNER JOIN audiobook ab
ON abp.audiobook_id = ab.id
INNER JOIN users u
ON abp.user_id = u.id
INNER JOIN book_categories bc
ON ab.book_category_codes[1] = bc.book_cateogory_code
LIMIT 10;

-- Query
SELECT *
FROM audiobook_plays abp
INNER JOIN audiobook ab
ON abp.audiobook_id = ab.id
INNER JOIN users u
ON abp.user_id = u.id
LIMIT 10;


SELECT name, LENGTH(book_cateogory_code)
FROM book_categories
LIMIT 100;

SELECT id, LENGTH(book_category_codes[2])
FROM audiobook
LIMIT 20;