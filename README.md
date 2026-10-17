# CausalAlign project page

Static, buildless project page for **CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion**. The visual layout is adapted from the [D4RT project page](https://d4rt-paper.github.io/); all research text, results, figures, and video shown here are CausalAlign material.

Page order: title and authors → demo → abstract → three-stage method → quantitative results → qualitative results.

## Preview

From the repository root, run:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory ..
```

Open `http://127.0.0.1:8000/CausalAlign-homepage/` in your browser. Keep the terminal open while previewing, and press `Ctrl+C` to stop the server. This path mirrors the final project's `/CausalAlign-homepage/` subpath. The committed page needs no build step.

## Source material

The assets are generated from the CausalAlign paper workspace by `scripts/prepare_assets.py`. The abstract follows the updated CausalAlign PDF; visual assets come from the paper's figure sources and the method slide layers. The demo is the latest 96-second narrated render. To regenerate the media on the original workspace:

```sh
python scripts/prepare_assets.py --workspace ..
```

This optional script requires PyMuPDF, Pillow, and OpenCV. The site itself has no runtime dependency on them.

## Publishing destination

This repository is currently private at `j-zhu23/CausalAlign-homepage`. The latest paper gives `https://pku-value-lab.github.io/CausalAlign-homepage/` as the project URL; it is also used as this site's canonical and Open Graph URL. The address will become live after the repository is moved to the PKU-VaLuE-Lab account and GitHub Pages is enabled there. All local asset URLs are relative, so they work under that subpath.

The Paper button temporarily links to `https://arxiv.org/abs/2603.02133`. **That ID currently resolves to SimRecon, not CausalAlign, and must be replaced before this page is public.** The Code button is labelled “Coming soon” until the code repository is ready.

Do not enable public Pages hosting while the page is intended to remain owner-private.
