""" These test fail! We have rewrite the tests with mock """
import pytest

from techtown2022.music_player.business_logic import play_song
from techtown2022.music_player.dbconn import DBConnection
from techtown2022.music_player.audio_player import AudioPlayer
from techtown2022.music_player.drm import DRMViolationError


def test_player_song_without_mocking():
    dbconn = DBConnection()
    player = AudioPlayer()
    song_title = "Fear of the Aardvark"

    play_song(song_title, dbconn, player)


def test_player_song_without_mocking_metalica():
    dbconn = DBConnection()
    player = AudioPlayer()
    song_title = "Meeseeks and Destroy"
    with pytest.raises(DRMViolationError):
        play_song(song_title, dbconn, player)
    player.play.assert_not_called()
