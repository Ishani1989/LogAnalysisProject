import psycopg2
from itertools import islice

DBNAME = "news"
"""Return all posts from the 'database', most recent first."""
db = psycopg2.connect(database=DBNAME)
query = """select count(a.path), substring(a.path, 10) as views, b.title,
c.name from log as a join articles as b
 on substring(a.path, 10) = b.slug join authors as c
 on b.author = c.id where status = '200 OK' group by path, b.title, c.name
 having length(substring(path, 10))>0 order by count(path) desc;"""
c = db.cursor()
c.execute(query)
results = c.fetchall()

print ("1. What are the most popular three articles of all time?")
print
iterator = islice(results, 3)
for a in iterator:
    print (u"\u00B7"+" "+str(a[2])+' - '+str(a[0])+' views')
print


query = """select name, sum(count) as popularity from summary
 group by name order by popularity desc limit 3;"""
c.execute(query)
results = c.fetchall()

print("2. Who are the most popular article authors of all time?")
print
for i in results:
    print u"\u00B7", i[0], '-', i[1], 'views'
print


query = """select wkdate, round(count401*100.0/(count200+count401),2)
as errorprc from(
select date(time) as wkdate,
sum(case when status='200 OK'      then 1 else 0 END) as count200,
sum(case when status='404 NOT FOUND' then 1 else 0 END) as count401
 from log group by date(time)
) as derived_table where count401*100/(count200+count401)>1"""
c.execute(query)
results = c.fetchall()
db.close()

print("3. On which days did more than 1% of requests lead to errors?")
print
print results[0][0].strftime('%d, %b %Y'), ' - ', str(results[0][1])+'% errors'
