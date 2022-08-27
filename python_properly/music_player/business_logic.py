from .dbconn import DBConnection
from .audio_player import AudioPlayer
from .song import SongData
from .drm import check_drm



def play_song(song_title, db_conn: DBConnection, player: AudioPlayer):
    """
    1. loads song data
    2. does a DRM check
    3. starts song playback
    """
    song_data: SongData = db_conn.get_song(song_title=song_title)
    check_drm(song_data.artist)
    player.play(song_id=song_data.player_song_id)
