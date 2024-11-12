# Natas

<br />
  <p align="center">
<img width="204" alt="Screenshot 2024-11-12 at 10 57 05" src="https://github.com/user-attachments/assets/94d7c3d0-d7ae-41f8-abeb-61c1a133d7d1">
  </p>
<br />

This project is a Python script to help interact the first levels of the <a href="https://overthewire.org/wargames/natas/" >Natas wargame from OverTheWire</a> on the command line.

## Requirements

- Python 3.x
- `click` library
- `requests` library
- `beautifulsoup4` library
- `Pygments` library

1. **Clone the repository:**

```bash
git clone https://github.com/bodhisatva/natas-solver
cd natas-solver
```

2. **Create a virtual environment:**

```bash
python3 -m venv natas-venv
source natas-venv/bin/activate
```

3. **Install the required packages:**

```bash
pip install -e .
```

4. **Run the script:**

```bash
./natas.py
```

### Usage

The script uses the click library to handle command-line options and prompts. Here are the available options:

- --username or -u: Prompts for the username.
- --password or -p: Prompts for the password.
- --url_suffix or -url: Prompts for the URL suffix or leave empty.
