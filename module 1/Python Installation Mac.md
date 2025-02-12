# **How to Set Up Python 3 on Mac & Troubleshoot Common Issues**

## **Step 1: Check if Python 3 is Already Installed**
Before installing Python 3, check if it is already installed:
```bash
python3 --version
```
If it's installed, you will see an output like:
```
Python 3.x.x
```
If not, proceed with the installation.

---

## **Method 1: Install Python 3 via Homebrew (Recommended)**
Homebrew is the easiest way to install and manage Python versions on macOS.

### **Step 1: Install Homebrew**
If you don't have Homebrew installed, install it first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Verify Homebrew installation:
```bash
brew --version
```

### **Step 2: Install Python 3**
Once Homebrew is installed, run:
```bash
brew install python3
```
This installs the latest Python 3 version.

### **Step 3: Verify Installation**
After installation, check the installed Python version:
```bash
python3 --version
```
You should see an output like:
```
Python 3.x.x
```
To check the installed location:
```bash
which python3
```
This should return something like:
```
/usr/local/bin/python3
```
or for Apple Silicon (M1/M2 Mac):
```
/opt/homebrew/bin/python3
```

### **Step 4: Install `pip3` (If Not Installed)**
Check if `pip3` (Python’s package manager) is installed:
```bash
pip3 --version
```
If not, install it using:
```bash
python3 -m ensurepip --default-pip
```
Then upgrade it:
```bash
pip3 install --upgrade pip
```

---

## **Method 2: Install Python 3 from Official Installer**
If you prefer using the official Python installer:

1. Go to the [official Python website](https://www.python.org/downloads/mac-osx/).
2. Download the latest macOS installer (`.pkg` file).
3. Open the downloaded file and follow the installation steps.
4. After installation, verify it:
   ```bash
   python3 --version
   ```

---

## **Method 3: Install Python Using Pyenv (For Multiple Versions)**
If you need to manage multiple Python versions, install `pyenv`:

### **Step 1: Install Pyenv**
```bash
brew install pyenv
```
Then, add the following lines to your shell profile:
- If using **zsh** (default on macOS Catalina and later):
  ```bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
  source ~/.zshrc
  ```
- If using **bash**:
  ```bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
  echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
  source ~/.bash_profile
  ```

### **Step 2: Install Python via Pyenv**
```bash
pyenv install 3.x.x  # Replace with desired Python version
pyenv global 3.x.x    # Set it as the global version
```
Check installed Python version:
```bash
python --version
```

---

## **Common Issues and Troubleshooting**

### **Issue 1: `python3` Command Not Found**
If `python3` is missing, reinstall Python using Homebrew:
```bash
brew reinstall python3
```
Then check:
```bash
which python3
python3 --version
```

### **Issue 2: Python 2 is Default Instead of Python 3**
If running `python` defaults to Python 2, update it to point to Python 3:
```bash
alias python=python3
```
To make this permanent, add it to your shell profile:
- **For zsh** (macOS default shell):
  ```bash
  echo "alias python=python3" >> ~/.zshrc
  source ~/.zshrc
  ```
- **For bash**:
  ```bash
  echo "alias python=python3" >> ~/.bash_profile
  source ~/.bash_profile
  ```

### **Issue 3: `pip3` Not Found**
If `pip3` is missing:
```bash
python3 -m ensurepip --default-pip
pip3 install --upgrade pip
```

### **Issue 4: `zsh: command not found: python3`**
If you see this error:
1. Check if Python is installed:
   ```bash
   ls /usr/local/bin/python3
   ```
   or
   ```bash
   ls /opt/homebrew/bin/python3  # For M1/M2 Macs
   ```
2. If missing, reinstall:
   ```bash
   brew install python3
   ```
3. Ensure your `PATH` is correctly set:
   ```bash
   echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### **Issue 5: `brew install python3` Hangs**
Try resetting Homebrew:
```bash
brew doctor
brew cleanup
brew update
brew upgrade
```
Then reinstall Python:
```bash
brew install python3
```

### **Issue 6: `pyenv` Not Working Properly**
If `pyenv` isn't working:
```bash
brew uninstall pyenv
brew install pyenv
```
Ensure you’ve added it to your shell profile:
```bash
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
source ~/.zshrc
```

### **Issue 7: SSL Certificate Issues When Using pip3**
If you see an SSL error while using `pip3`:
```bash
pip3 install requests
```
Error:
```
Could not fetch URL due to SSL verification issue
```
Fix it by reinstalling the SSL package:
```bash
brew reinstall openssl
```
Then, link Python with OpenSSL:
```bash
export PATH="/usr/local/opt/openssl/bin:$PATH"
```
To make this permanent, add it to your `~/.zshrc`:
```bash
echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## **Final Check**
Run the following to confirm Python is installed correctly:
```bash
python3 --version
pip3 --version
which python3
which pip3
```



