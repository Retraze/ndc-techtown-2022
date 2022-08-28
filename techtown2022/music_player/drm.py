class DRMViolationError(Exception):
    pass


artist_blacklist = ["Metalica"]


def check_drm(artist: str):
    if artist in artist_blacklist:
        raise DRMViolationError(f"For DRM reasons, this application does not support {artist}. Sorry.")
