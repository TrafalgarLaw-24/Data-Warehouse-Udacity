## Summary
### Sparkify Redshift
This project aims to test the understanding of Data warehousing concepts.
The task includes facilitating the Sparkify app in setting up a data warehouse
that would have the data of songs which users are listening to.
This would help Sparkify analyze the user activities to understand user base.

This project uses `Amazon s3 bucket` for file storage and `Amazon Redshift`
 for database storage and data warehouse purpose.

## Source Data
The source data is present in log files given in the Udacity public Amazon s3 bucket  at `s3://udacity-dend/log_data`
and `s3://udacity-dend/song_data` containing log data and songs data.

Log files contains songplay events of the users in json format
while song_data contains list of songs details.

## Database Schema
Following are the fact and dimension tables made for this project:
#### Dimension Tables:
   * users
        * columns: user_id, first_name, last_name, gender, level
   * songs
        * columns: song_id, title, artist_id, year, duration
   * artists
        * columns: artist_id, name, location, lattitude, longitude
   * time
        * columns: start_time, hour, day, week, month, year, weekday

#### Fact Table:
   * songplays
        * columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

## To execute the project:
   * Update the `dwh.cfg` file with your AWS credentials and IAM role that will be used to access the cluster.
   * Run the `create_tables.py`. This will create the database and all the necessary tables.
   * Run `etl.py`. This will start the pipeline which will read the data from the files and populate the tables.

## About:
This project is done as part of Udacity Data Engineer Nano degree program
