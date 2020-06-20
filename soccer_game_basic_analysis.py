#importing important libraries
import pandas as pd
import sqlite3

#Select a path where the sqlite file is located 
path = '//path/database.sqlite'

#Build a sqlite connection
conn = sqlite3.connect(path)

#Run a query to view all tables
query = """select * from sqlite_master where type = 'table'; """

#Create a dataframe
df = pd.read_sql_query(query, conn)

#Print dataframe to view all tables
df

#Table 1.Sqlite_sequence
#Table 2.Player_attributes
#Table 3.Player
#Table 4.Match
#Table 5.League
#Table 6.Country
#Table 7.Team_Attributes

#Let's run a most basic query to view each table to understand the tables structure
#Pull data of Sqlite sequence table
sqlite_sequence = """select * from sqlite_sequence;"""
sqlite_sequence_df = pd.read_sql_query(sqlite_sequence, conn)
sqlite_sequence_df

#Pull data of Player attributes table
player_attributes = """select * from player_attributes; """
player_attributes_df = pd.read_sql_query(player_attributes, conn)
player_attributes_df

#Pull data of Player table
player = """select * from player;"""
player_df = pd.read_sql_query(player, conn)
player_df

#Pull data of Match table
match = """select * from match;"""
match_df = pd.read_sql_query(match, conn)
match_df

#Pull data of League table
league = """select * from league; """
league_df = pd.read_sql_query(league, conn)
league_df

#Pull data of Country table
country = """select * from country; """
country_df = pd.read_sql_query(country, conn)
country_df

#Pull data of Team_Attributes
team_attributes = """select * from team_attributes;"""
team_attributes_df = pd.read_sql_query(team_attributes, conn)
team_attributes_df