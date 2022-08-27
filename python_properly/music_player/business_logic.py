from .dbconn import DBConnection
from .audio_player import AudioPlayer
from .song import SongData


class DRMViolationError(Exception):
    pass


artist_blacklist = [
    "Metalica"
]


def play_song(song_title, db_conn: DBConnection, player: AudioPlayer):
    """
    1. loads song data
    2. does a DRM check
    3. starts song playback
    """
    song_data: SongData = db_conn.get_song(song_title=song_title)
    if song_data.artist in artist_blacklist :
        raise DRMViolationError(f"For DRM reasons, this application does not support {song_data.artist}. Sorry.")
    player.play(song_id=song_data.player_song_id)
