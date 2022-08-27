from dataclasses import dataclass


@dataclass
class SongData:
    title: str
    artist: str
    player_song_id: int


# We currently know of these songs
# They can be used for testing purposes
song1 = SongData("Fear of the Aardvark", "Steel Maiden", 1345)
song2 = SongData("Meeseeks and Destroy", "Metalica", 2413)