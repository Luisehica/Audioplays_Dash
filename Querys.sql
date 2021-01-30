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
GROUP BY Year, Week, Week_date
ORDER BY Year, Week;

-- 3 Falta terminar
-- Week over Week retention rato of active user
WITH WAU (Year, Weekly, User_id) AS (
    SELECT date_part('year', created_at::date),
    date_part('week', created_at::date),
    user_id
    FROM audiobook_plays
)
SELECT WAU.Year, WAU. Weekly, WAU.User_id
FROM WAU
LIMIT 10;

-- solución chato
WITH semanas AS (
	SELECT DISTINCT	user_id,
	date_trunc('week',created_at)::date as semana
	FROM audiobook_plays ap 
	ORDER BY user_id, semana
), 
sem_anterior as (
	select 
	user_id
	, semana as semana_actual
	, lag(semana) over (partition by user_id order by semana asc) as semana_anterior
	from semanas
), 
comparacion as (
	select *
	, case when (semana_anterior is null or (semana_actual - semana_anterior) > 7) then false
		else true end as retention
	from sem_anterior
	)
select semana_actual,
	total_users,
	usuarios_retenidos,
	(usuarios_retenidos::float / total_users::float)*100 as rate
from (
	select semana_actual, 
	count(distinct case when retention then user_id end ) usuarios_retenidos
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

-- query corta
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
SELECT current_date_, 
	total_users,
	active_users,
	ROUND(active_users::numeric/total_users*100, 2) AS retention_rate
FROM WAU;



-- 4 
-- Average Hours_played_last_30_days
WIT





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

SELECT id, LENGTH(book_category_codes[1])
FROM audiobook
LIMIT 20;