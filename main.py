import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqLite://my_played_tracks.sqlite"
USER_ID = "benogle"
TOKEN = "BQAWdrxtB6OvUES7K1YJzz2JzbqdXMpSf2eymXtnJ-sBG0zvYgCnTkO84xHk_ecQufsMb-tMUZbfcii7_BvvR_9xJ1j9AUI2T_fOt6rLYLnSnoHKeBTcGQi8TdM6PeBNwpxPbLatduWJ5g85"

# Transform the Data


def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Check if the dataframe is empty
    if df.empty:
        print("No song data was fetched")
        return False

    # Primary Key Check
    if pd.Series(df["played_at"]).is_unique:
        pass
    else:
        raise Exception("Primary Key Check has been violated")

    # Check for null values
    if df.isnull().values.any():
        raise Exception("Null value found")

    # Check to ensure all timestamps include yesterday's date
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    timestamps = df["timestamp"].tolist()
    for timestamp in timestamps:
        if datetime.datetime.strptime(timestamp, '%Y-%m-%d') != yesterday:
            raise Exception(
                "At least one of the returned songs does not have a yesterday's timestamp")

    return True


# Extract the Data
if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(
        time=yesterday_unix_timestamp), headers=headers)

    data = r.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }

    song_df = pd.DataFrame(song_dict, columns=[
                           "song_name", "artist_name", "played_at", "timestamp"])
    print(song_df)
# Validate the Data
    if check_if_valid_data(song_df):
        print("Data valid, proceed to load stage")
