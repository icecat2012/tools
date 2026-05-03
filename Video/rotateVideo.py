import argparse
import shutil
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


def _open_clip(path: Path) -> VideoFileClip:
    """Open the file using the source audio sample rate so decode/mux timing matches the file."""
    path_s = str(path)
    try:
        probe = VideoFileClip(path_s, audio=False)
    except TypeError:
        return VideoFileClip(path_s)
    try:
        infos = probe.reader.infos
        has_audio = bool(infos.get("audio_found"))
        native_sr = infos.get("audio_fps")
    finally:
        probe.close()
    if not has_audio or native_sr is None:
        return VideoFileClip(path_s)
    return VideoFileClip(
        path_s,
        audio_fps=int(round(float(native_sr))),
    )


def _write_rotated(rotated: VideoClip, out: Path) -> None:
    """Write video with the same frame rate and audio rate as the clip (avoids resync / length drift)."""
    kwargs: dict = {
        "codec": "libx264",
        "audio_codec": "aac",
        "preset": "medium",
        "ffmpeg_params": ["-movflags", "+faststart"],
    }
    if getattr(rotated, "fps", None) is not None:
        kwargs["fps"] = rotated.fps
    if rotated.audio is not None:
        kwargs["audio_fps"] = rotated.audio.fps
        nb = getattr(rotated.audio, "nbytes", None)
        if nb is not None:
            kwargs["audio_nbytes"] = nb
    else:
        kwargs["audio"] = False

    rotated.write_videofile(str(out), **kwargs)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rotate a video with MoviePy (default angle: 90 degrees)."
    )
    parser.add_argument(
        "-f",
        "--file",
        type=Path,
        required=True,
        help="Input video file (e.g. clip.mp4)",
    )
    parser.add_argument(
        "-d",
        "--degree",
        type=int,
        default=90,
        help="Rotation angle in degrees (default: 90)",
    )
    args = parser.parse_args()

    inp = args.file.expanduser().resolve()
    if not inp.is_file():
        print(f"Error: file not found: {inp}", file=sys.stderr)
        return 1

    out = inp.with_name(f"{inp.stem}_rotated{inp.suffix}")

    clip: VideoFileClip | None = None
    rotated: VideoClip | None = None
    try:
        clip = _open_clip(inp)
        rotated = _rotate_clip(clip, args.degree)
        _write_rotated(rotated, out)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    finally:
        if rotated is not None:
            rotated.close()
        if clip is not None:
            clip.close()

    # Match Explorer Created / Modified / Accessed to the source file (Windows: Python 3.8+).
    try:
        shutil.copystat(inp, out, follow_symlinks=True)
    except OSError as e:
        print(f"Warning: could not copy file timestamps: {e}", file=sys.stderr)

    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
