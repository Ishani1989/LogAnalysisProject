# Logs Analysis Project

This project is written in Python and uses psycopg2 to connect to database and PostgreSQL to fetch data from database 'news'.
The news database comprises of 3 tables namely, articles, authors and log. This project analyses data from these 3 tables to answer some basic questions.


## Installation/Setup

Python version - 2.7.13
Vagrant version - 1.9.5
Oracle VirtualBox version - 5.1.22 r115126 (Qt5.6.2)
ubuntu-16.04-i386


## Usage

1. Install a virtual machine (vagrant)
2. Once installed, start the VM with the command 'vagrant up'. 
3. Then log into it with vagrant ssh. (I have used Putty to login)
4. Download the data provided. Unzip it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
5. Load the site's data into your local database, using the command psql -d news -f newsdata.sql.
6. Connect to the database news using command 'psql news'.
7. Run the following query to create a view named summary.
	'create view summary as select count(a.path), substring(a.path, 10) as views, b.title, c.name from log as a join articles as b
	 on substring(a.path, 10) = b.slug join authors as c on b.author = c.id where status = '200 OK' group by path, b.title, c.name
	 having length(substring(path, 10))>0 order by count(path) desc;'
8. Place the file newsdb.py in the same directory as the newsdata.sql file and run it using the command 'python newsdb.py'
9. Running the file prints out the questions with their respective answers after queryin the database.


## History

First checkin done on May 31, 2017

## Credits

ishmukherjee89@gmail.com