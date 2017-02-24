import mysql.connector
import time
import datetime
import MySQLdb

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='MediaTracker')

cursor = cnx.cursor()

# find list of all followers that were just added
# query = 'select id from followers'

# cursor.execute(query)
data = []
# for unfollowerid in unfollowerIds:
#     data.append((unfollowerid, influencerId, date, 1))

# extra saftey, stops from adding duplicate following rows
# for row in cursor:
#     # 1 is mario's ID row[0] is followers ID
#     isFollower = findFollowerStatus(row[0], 1)
#     if (not isFollower):
#         data.append((row[0], influencerID, date, 1))

# print (data)

createInfluencer = 'CREATE TABLE Influencer (id int(11) NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL DEFAULT '', PRIMARY KEY (id))'
createFollower = 'CREATE TABLE Follower (id int(11) NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL DEFAULT '', PRIMARY KEY (id), UNIQUE (name))'
createInfluencer2Follower =  'CREATE TABLE Influencer2Follower ' \
                             '(id int(25) NOT NULL AUTO_INCREMENT,' \
                             ' influencerID int(11) NOT NULL,' \
                             ' followerID int(11) NOT NULL,' \
                             ' followed int(11) DEFAULT 1,' \
                             ' unfollowed int(11) DEFAULT 1)'

#query_string = 'INSERT INTO Influencer2Follower (followerID, influencerID, created, unfollowed) VALUES (%s, %s, %s, %s)'
cursor.execute(query_string)
cursor.executemany(query_string, data)
cnx.commit()

cursor.close()
cnx.close()
