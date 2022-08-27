import pytest
import mock

from python_properly.music_player.business_logic import play_song, DRMViolationError
from python_properly.music_player.song import SongData

# without mocking
"""
from python_properly.music_player.dbconn import DBConnection
from python_properly.music_player.audio_player import AudioPlayer

def test_player_song_without_mocking():
    dbconn = DBConnection()
    player = AudioPlayer()
    song_title = "Fear of the Aardvark"

    play_song(song_title, dbconn, player)

def test_player_song_without_mocking_metalica():
    song_title = "Meeseeks and Destroy"
    with pytest.raises(DRMViolationError):
        play_song(song_title, dbconn, player)
    player.play.assert_not_called()
"""

# with mocking
@mock.patch("python_properly.music_player.dbconn.DBConnection")
@mock.patch("python_properly.music_player.audio_player.AudioPlayer")
def test_player_song_ok(player, dbconn):
    song_data = SongData("Fear of the Aardvark", "Steel Maiden", 1345)
    dbconn.get_song.return_value = song_data
    song_title = "Fear of the Aardvark"

    play_song(song_title, dbconn, player)

    dbconn.get_song.assert_called()
    player.play.assert_called()
    
    # Bonus
    dbconn.get_song.assert_called_with(song_title=song_title)
    player.play.assert_called_with(song_id=song_data.player_song_id)

@mock.patch("python_properly.music_player.dbconn.DBConnection")
@mock.patch("python_properly.music_player.audio_player.AudioPlayer")
def test_player_song_metalica(player, dbconn):
    song_data = SongData("Meeseeks and Destroy", "Metalica", 2413)
    dbconn.get_song.return_value = song_data
    song_title = "Meeseeks and Destroy"
    with pytest.raises(DRMViolationError):
        play_song(song_title, dbconn, player)
    player.play.assert_not_called()
    

