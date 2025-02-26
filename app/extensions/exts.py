from typing import Final

VIDEO_EXTS: Final = frozenset((".mp4", ".mkv", ".flv", ".avi", ".wmv", ".ts", ".rmvb", ".webm", "wmv"))
AUDIO_EXTS: Final = frozenset((".mp3", ".wav"))
MEDIA_EXTS: Final = frozenset(VIDEO_EXTS.union(AUDIO_EXTS))

EXTENDED_VIDEO_EXTS: Final = frozenset(MEDIA_EXTS.union((".strm",)))

SUBTITLE_EXTS: Final = frozenset((".ass", ".srt", ".ssa", ".sub", ".vtt", ".lrc"))

IMAGE_EXTS: Final = frozenset((".png", ".jpg", ".webp", ".gif"))

NFO_EXTS: Final = frozenset((".nfo",))
