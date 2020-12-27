from typing import Optional

from v3io.dataplane import Client as V3IOClient
from v3io_frames import Client as FramesClient

from model_monitoring.constants import DEFAULT_CONTAINER

# TODO: Can be done nicer, also this code assumes environment parameters exist for initializing both frames and v3io
_v3io_client: Optional[V3IOClient] = None
_frames_client: Optional[FramesClient] = None


def get_frames_client() -> FramesClient:
    global _frames_client
    if _frames_client is None:
        _frames_client = FramesClient(container=DEFAULT_CONTAINER, should_check_version=False)
    return _frames_client


def get_v3io_client() -> V3IOClient:
    global _v3io_client
    if _v3io_client is None:
        _v3io_client = V3IOClient()
    return _v3io_client
