"""
DO NOT LOOK at this code unless you want spoilers!

This module contains tests that comply with the assignment.
"""

import pytest
import mock

from python_properly.music_player.business_logic import play_song
from python_properly.music_player.song import SongData
from python_properly.music_player.drm import DRMViolationError


@pytest.fixture
def mocked_dbconnection(monkeypatch):
    mocked_dbconnection = mock.MagicMock()
    monkeypatch.setattr("python_properly.music_player.dbconn.DBConnection", mocked_dbconnection)
    return mocked_dbconnection


@pytest.fixture
def mocked_audio_player(monkeypatch):
    mocked_audio_player = mock.MagicMock()
    monkeypatch.setattr("python_properly.music_player.audio_player.AudioPlayer", mocked_audio_player)
    return mocked_audio_player



def test_player_song_ok(mocked_dbconnection, mocked_audio_player):
    song_data = SongData("Fear of the Aardvark", "Steel Maiden", 1345)
    mocked_dbconnection.get_song.return_value = song_data
    song_title = "Fear of the Aardvark"

    play_song(song_title, mocked_dbconnection, mocked_audio_player)

    mocked_dbconnection.get_song.assert_called()
    mocked_audio_player.play.assert_called()

    # Bonus
    mocked_dbconnection.get_song.assert_called_with(song_title=song_title)
    mocked_audio_player.play.assert_called_with(song_id=song_data.player_song_id)


def test_player_song_metalica(mocked_dbconnection, mocked_audio_player):
    song_data = SongData("Meeseeks and Destroy", "Metalica", 2413)
    mocked_dbconnection.get_song.return_value = song_data
    song_title = "Meeseeks and Destroy"
    with pytest.raises(DRMViolationError):
        play_song(song_title, mocked_dbconnection, mocked_audio_player)

    mocked_dbconnection.get_song.assert_called_with(song_title=song_title)
    mocked_audio_player.play.assert_not_called()
