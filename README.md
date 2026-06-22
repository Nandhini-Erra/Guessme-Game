# QuickNote App 📝

A single-page web application to write, save, and manage notes using a Python Flask backend and SQLite database.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **Database**: SQLite

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
Go to: http://localhost:5000

## Features
- ✅ Write and save notes
- ✅ View all saved notes
- ✅ Delete notes
- ✅ Notes stored in SQLite database
- ✅ Real-time character count
- ✅ Ctrl+Enter shortcut to save

## Project Structure
```
quicknote/
├── app.py          # Flask backend
├── index.html      # Frontend UI
├── requirements.txt
└── notes.db        # Auto-created SQLite database
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/notes | Get all notes |
| POST | /api/notes | Add a new note |
| DELETE | /api/notes/<id> | Delete a note |
