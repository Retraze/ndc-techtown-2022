

Make unit test(s) for python_properly.music_player.business_logic.display_song. 

Hint: you can use the @mock.patch decorator to provide mocked objects

Verify that:
- dbconn.get_song() gets called 
- DRMViolationError is raised if any songs by artist "Metalica"
  - player.play() does not get called
- No exception is raised if any other artist is played
  - player.play() does get called


Verify that:
- dbconn.get_song() gets called and returns a SongData object
- playe.play() gets called with a SongData object


Bonus:
- make a fixture that provides the mocked objects instead of using mock.patch