# Frontend-reconstruction-UTRGV

Visual reconstruction of UTRGV / Microsoft login UI for educational analysis. Contains static frontend components, with no real authentication logic.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

To start the server, run:
```bash
python server.py
```

Once the server is running, wait a few seconds for it to initialize. Once ready, the site will be fully available at `http://localhost:5000`.

Open your browser and navigate to `http://localhost:5000` to view the UTRGV homepage. Click the "Sign In" button to see the Microsoft login page.

## Important Notes

- **Credential Storage**: When you submit the login form, your email and password will be saved locally in `saved_credentials.json` for educational analysis purposes.
- **Post-Login Behavior**: After signing in, the application will redirect you to an error page from the original Microsoft website, as this is a frontend reconstruction with no real authentication logic.
