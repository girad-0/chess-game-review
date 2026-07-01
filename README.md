# ♟️ Chess Game Review

A Django-based web application that analyzes chess games from PGN files using the Stockfish chess engine. The application provides move-by-move engine evaluations, identifies inaccuracies, mistakes, and blunders, and displays an interactive chessboard for game review.

---

## Features

- Upload chess games in PGN format
- Automatic PGN parsing using `python-chess`
- Engine analysis powered by Stockfish
- Move-by-move evaluation in centipawns
- Detects:
  - Best Moves
  - Inaccuracies
  - Mistakes
  - Blunders
- Interactive chessboard with move navigation
- Displays complete move list
- Simple and responsive web interface built with Django

---

## Tech Stack

- Python 3
- Django
- python-chess
- Stockfish Chess Engine
- HTML
- CSS
- JavaScript
- Chessboard.js
- SQLite

---

## Project Structure

```
chess-game-review/
│
├── chess_review/          # Django project settings
├── review/                # Main Django application
│   ├── templates/
│   ├── static/
│   ├── parser.py
│   ├── engine.py
│   ├── views.py
│   ├── models.py
│   └── urls.py
│
├── media/                 # Uploaded PGN files
├── engine/                # Stockfish executable (ignored by Git)
├── manage.py
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/girad-0/chess-game-review.git
cd chess-game-review
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Download Stockfish

Download the latest Stockfish release from:

https://stockfishchess.org/download/

Place the executable inside:

```
engine/
```

Example:

```
engine/
    stockfish.exe
```

Update the Stockfish path inside `engine.py` if required.

---

### 5. Apply migrations

```bash
python manage.py migrate
```

---

### 6. Run the server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

## How It Works

1. User uploads a PGN file.
2. The application parses every move using `python-chess`.
3. Each position is analyzed by the Stockfish engine.
4. Engine evaluations are converted into move classifications.
5. Results are displayed alongside an interactive chessboard.

---

## Future Improvements

- Accuracy percentage calculation
- Brilliant move detection
- Opening recognition
- Evaluation graph
- Multi-PV analysis
- User authentication
- Save analysis history
- Cloud deployment
- Puzzle generation from mistakes
## License

This project is licensed under the MIT License.
