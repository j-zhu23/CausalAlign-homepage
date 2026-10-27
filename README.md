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

The assets are generated from the CausalAlign paper workspace by `scripts/prepare_assets.py`. The abstract follows the updated CausalAlign PDF; visual assets come from the paper's figure sources and the method slide layers. The demo is the latest 158-second narrated render. To regenerate the media on the original workspace:

```sh
python scripts/prepare_assets.py --workspace ..
```

This optional script requires PyMuPDF, Pillow, and OpenCV. The site itself has no runtime dependency on them.

## Publishing destination

The public site is `https://pku-value-lab.github.io/CausalAlign-homepage/`, published from the root of the `main` branch in `PKU-VaLuE-Lab/CausalAlign-homepage`. All local asset URLs are relative to that project path. The personal `j-zhu23/CausalAlign-homepage` repository is a public working copy with the same current files.

The Paper button links to the CausalAlign preprint at `https://arxiv.org/abs/2610.29915`, and the Hugging Face button links to `https://huggingface.co/papers/2610.29915`. The Code button links to `https://github.com/PKU-VaLuE-Lab/CausalAlign`, which hosts the updated demo and the released training and WAM code.
