```bash
# Install Python 3.10 (recommended)

# Then recreate environment
python3.10 -m venv my_env

# Activate
source my_env/bin/activate    # Linux Bash
source my_env/Scripts/activate   # Git Bash

# Upgrade pip
pip install --upgrade pip

# If above can not work
# python.exe   -m pip install --upgrade pip

# Install again
pip install -r requirements.txt

# Run streamlit
streamlit run app/main_app.py
```