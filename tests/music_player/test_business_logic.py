""" These test fail! We have rewrite the tests with mock """
import pytest

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
