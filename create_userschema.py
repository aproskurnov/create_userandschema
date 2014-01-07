#!/usr/local/bin/python
#created: 2014-01-03
#author: Aleksey Proskurnov <proskurn@gmail.com>
#Copyright (c) 2014, Aleksey Proskurnov

import argparse
import mysql.connector

user = "root"

parser = argparse.ArgumentParser()
parser.add_argument("-p","--password")
parser.add_argument("-n","--name")
args = parser.parse_args()

if args.password and args.name:
	cnx = mysql.connector.connect(user=user,password=args.password,host='127.0.0.1')
	cnx.start_transaction()
	try:
		cur = cnx.cursor()
		cur.execute("CREATE USER '" + args.name + "'@'localhost' IDENTIFIED BY '" + args.name + "';")
		cur.execute("CREATE SCHEMA " + args.name + ";")
		cur.execute("GRANT ALL PRIVILEGES ON " + args.name + ".* TO '" + args.name + "'@'localhost';")
	except mysql.connector.Error as err:
		print(err)
		cnx.rollback()
	else:
		cnx.commit()
		cur.close()
		cnx.close()
		print("user and schema with name",args.name,"was created")
else:
	print("need insert root password and name for user and schema")
