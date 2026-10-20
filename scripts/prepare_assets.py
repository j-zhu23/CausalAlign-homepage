"""Build static page media from the CausalAlign paper workspace.

Example (from this repository):
    python scripts/prepare_assets.py --workspace ..
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import cv2
import fitz
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def render_figure(source: Path, dest: Path, zoom: float, quality: int = 88) -> None:
    with fitz.open(source) as document:
        page = document[0]
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    image.save(dest, "WEBP", quality=quality, method=6)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, required=True)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    ASSETS.mkdir(exist_ok=True)

    demo = workspace / "demo" / "CausalAlign_demo_153s.mp4"
    shutil.copyfile(demo, ASSETS / "causalalign-demo.mp4")

    figure_dir = workspace / "CausalAlign_open_version" / "Figure"
    render_figure(figure_dir / "rise_and_fall.pdf", ASSETS / "geometric-state-retention.webp", 2.5)
    render_figure(figure_dir / "loop_jittering.pdf", ASSETS / "camera-trajectories.webp", 3.2)

    rollouts = Image.open(figure_dir / "wam_mobile_rollouts_1.png").convert("RGB")
    midpoint = rollouts.width // 2
    rollouts.crop((0, 0, midpoint, rollouts.height)).save(
        ASSETS / "rollout-bowl.webp", "WEBP", quality=91, method=6
    )
    rollouts.crop((midpoint, 0, rollouts.width, rollouts.height)).save(
        ASSETS / "rollout-basket.webp", "WEBP", quality=91, method=6
    )

    layers = workspace / "demo" / "assets"
    method = Image.new("RGBA", (2980, 1320), "white")
    for name in ("method_layer1.png", "method_layer2.png",
                 "method_layer3.png", "method_align.png"):
        layer = Image.open(layers / name).convert("RGBA")
        if layer.size != method.size:
            raise ValueError(f"Method layer has unexpected size: {name}")
        method.alpha_composite(layer)
    method.convert("RGB").save(ASSETS / "method.webp", "WEBP", quality=91, method=6)

    cap = cv2.VideoCapture(str(demo))
    try:
        cap.set(cv2.CAP_PROP_POS_MSEC, 19500)
        ok, frame = cap.read()
        if not ok:
            raise RuntimeError("Cannot read the 19.5-second demo poster frame")
        poster = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        poster.save(ASSETS / "demo-poster.webp", "WEBP", quality=84, method=6)
    finally:
        cap.release()

    for path in sorted(ASSETS.iterdir()):
        print(f"{path.name}: {path.stat().st_size / 1024 / 1024:.2f} MiB")


if __name__ == "__main__":
    main()
