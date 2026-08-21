# python-notes

Personal study notes on Python and related topics — written for my own learning, organized as markdown tutorials and static sites. If they are useful for your study too, you are welcome to read and use them.

See [LICENSE](LICENSE) for terms (CC BY-NC 4.0 — attribution, non-commercial use; no warranty).

## Topics

| Topic | Description | Start reading | Site |
|-------|-------------|---------------|------|
| [Easy Python](easypy/) | Python for absolute beginners — variables, loops, functions, classes, and building Tetris step by step | [Welcome to Programming](easypy/part1-welcome/01-welcome-to-programming.md) | [site](easypy/site/index.html) |

Sample program (text + Pygame Tetris): [tetris/](tetris/)

Each topic folder includes an `index.md` with the full chapter list. HTML sites are generated with [MDWeb](https://github.com/hoihky/MDWeb) and are best previewed with a local static server (e.g. `npx serve easypy/site`) so diagrams and assets load correctly.

## Repository layout

```text
python-notes/
├── easypy/            # Easy Python — beginner tutorial with Tetris project
│   ├── part1-welcome/
│   ├── part2-setup/
│   ├── …              # parts 3–12 (40 chapters total)
│   ├── index.md
│   └── site/          # generated HTML (MDWeb output)
├── easypy-theme/      # MDWeb theme (dark code blocks, custom styling)
├── tetris/            # working sample program (text + Pygame Tetris)
├── footer.html        # page footer fragment for MDWeb
└── LICENSE
```

## Regenerating the site

From the repository root (adjust the MDWeb path if needed):

```bash
dotnet run --project /path/to/MDWeb/src/MDWeb.Cli -- \
  --source ./easypy \
  --output ./easypy/site \
  --theme ./easypy-theme \
  --title "Easy Python — Learn Programming with Tetris" \
  --footer-file ./footer.html
```

Preview:

```bash
npx serve easypy/site
```

## License

This repository is licensed under **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)** (Creative Commons Attribution-NonCommercial 4.0 International). You may share and adapt the notes for **non-commercial** purposes with **attribution**. The content was created and edited with **AI assistance** and is intended for **educational use** only. The material is provided **without warranty**. Full text and disclaimers: [LICENSE](LICENSE).
