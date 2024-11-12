# Natas Solver

<br />
  <p align="center">
<img width="204" alt="Screenshot 2024-11-12 at 10 57 05" src="https://github.com/user-attachments/assets/94d7c3d0-d7ae-41f8-abeb-61c1a133d7d1">
  </p>
<br />

This project is a Python script to help solve the first levels of the <a href="https://overthewire.org/wargames/natas/" >Natas wargame from OverTheWire</a> on the command line.

## Requirements

- Python 3.x
- `click` library
- `requests` library
- `beautifulsoup4` library
- `Pygments` library

## Installation

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

4. **Ensure the script has execute permissions:**

```bash
chmod +x natas.py
```

5. **Run the script:**

```bash
./natas.py
```

## Usage

The script uses the click library to handle command-line options and prompts. Here are the available options:

- --username or -u: Prompts for the username.
- --password or -p: Prompts for the password.

#### Directory Traversal

To trying out different paths in a URL to find out hidden directories, select 1 when asked to enter a URL suffix and add the path. If the URL does not require manipulation, press Enter.

- Enter URL suffix: <some/path>

#### Custom Header

To create a custom header, select 1 when prompted to enter a custom header, then enter the key and value.

- Enter custom header key: <custom_key>
- Enter custom header value: <custom_value>
