# Easy Python Tetris — Sample Program

Working Tetris sample for the [Easy Python](../easypy/) tutorial. Code structure and names follow the book chapters (Parts 9–12).

## Project layout

| File | Role |
|------|------|
| `constants.py` | Board size, symbols, scoring table |
| `shapes.py` | Tetromino offsets, `get_cells`, `spawn_piece` |
| `board.py` | Grid creation and terminal drawing |
| `collision.py` | `can_place` collision checks |
| `piece.py` | `Piece` class |
| `game.py` | `Game` class and shared game rules |
| `tetris.py` | Text Tetris (terminal) |
| `tetris_gui.py` | Color Tetris (Pygame) |

## Text Tetris

```bash
cd tetris
python3 tetris.py
```

Controls: `a` left, `d` right, `s` soft drop, `w` rotate, `h` hard drop, `q` quit.

## Pygame Tetris

```bash
cd tetris
pip install -r requirements.txt
python3 tetris_gui.py
```

Controls: arrow keys (same as text), `Space` hard drop, `Q` or `Esc` quit.

## Quick tests

```bash
python3 board.py      # draw empty board and O-piece
python3 -c "from collision import can_place; from board import make_board; print(can_place(make_board(), [(0,0),(0,1),(1,0),(1,1)]))"
```
