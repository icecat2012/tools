import argparse
import sys
from pathlib import Path

try:
    from moviepy.editor import VideoClip, VideoFileClip
except ModuleNotFoundError:
    from moviepy import VideoClip, VideoFileClip  # MoviePy 2.x (no moviepy.editor)


def _rotate_clip(clip: VideoFileClip, angle: int) -> VideoClip:
    """MoviePy 1: clip.rotate; MoviePy 2: Rotate effect."""
    rotate = getattr(clip, "rotate", None)
    if callable(rotate):
        return rotate(angle, expand=True)
    from moviepy.video.fx.Rotate import Rotate

    return clip.with_effects([Rotate(float(angle), expand=True)])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rotate a video with MoviePy (default angle: 90 degrees)."
    )
    parser.add_argument(
        "video",
        type=Path,
        help="Input video file (e.g. clip.mp4)",
    )
    parser.add_argument(
        "angle",
        nargs="?",
        type=int,
        default=90,
        help="Rotation angle in degrees (default: 90)",
    )
    args = parser.parse_args()

    inp = args.video.expanduser().resolve()
    if not inp.is_file():
        print(f"Error: file not found: {inp}", file=sys.stderr)
        return 1

    out = inp.with_name(f"{inp.stem}_rotated{inp.suffix}")

    clip: VideoFileClip | None = None
    rotated: VideoClip | None = None
    try:
        clip = VideoFileClip(str(inp))
        rotated = _rotate_clip(clip, args.angle)
        rotated.write_videofile(
            str(out),
            codec="libx264",
            audio_codec="aac",
            ffmpeg_params=["-preset", "medium", "-movflags", "+faststart"],
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    finally:
        if rotated is not None:
            rotated.close()
        if clip is not None:
            clip.close()

    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
