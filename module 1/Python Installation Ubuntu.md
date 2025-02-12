# **How to Install Python 3 on Ubuntu and Troubleshoot Issues**

### **Step 1: Check if Python 3 is Already Installed**
Before installing Python 3, check if it's already installed by running:
```bash
python3 --version
```
If it's installed, you'll see an output like:
```
Python 3.x.x
```
If it's not installed or outdated, follow the steps below.

---

## **Method 1: Install Python 3 Using APT (Recommended)**
### **Step 2: Update and Upgrade Ubuntu Packages**
Run the following commands to update your system:
```bash
sudo apt update && sudo apt upgrade -y
```

### **Step 3: Install Python 3**
To install the default version of Python 3 available in Ubuntu’s repositories:
```bash
sudo apt install python3 -y
```

### **Step 4: Verify the Installation**
After installation, check the installed version:
```bash
python3 --version
```

---

## **Method 2: Install Latest Python from Deadsnakes PPA (For Newer Versions)**
If you need the latest version of Python, use the **Deadsnakes PPA**:
```bash
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
```
Now install the latest version:
```bash
sudo apt install python3.x -y  # Replace x with the desired version (e.g., 3.12)
```

Verify installation:
```bash
python3.x --version
```

---

## **Method 3: Install Python 3 from Source (For Custom Installation)**
If you need a specific version or want to compile Python from source:

### **Step 1: Install Dependencies**
```bash
sudo apt update
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev \
    libsqlite3-dev libreadline-dev libbz2-dev liblzma-dev zlib1g-dev
```

### **Step 2: Download and Compile Python**
1. Go to [Python’s official site](https://www.python.org/ftp/python/) and find the latest release.
2. Download it using `wget`:
   ```bash
   wget https://www.python.org/ftp/python/3.x.x/Python-3.x.x.tgz
   ```
   *(Replace `3.x.x` with the latest version)*
3. Extract and navigate to the folder:
   ```bash
   tar -xvf Python-3.x.x.tgz
   cd Python-3.x.x
   ```
4. Compile and install:
   ```bash
   ./configure --enable-optimizations
   make -j$(nproc)
   sudo make altinstall
   ```
   *(Use `altinstall` to avoid overwriting `python` binary used by the system.)*

5. Verify:
   ```bash
   python3.x --version
   ```

---

## **Common Issues and Fixes**

### **Issue 1: Python 3 is Installed But Not Default**
Check the current default version:
```bash
python --version
```
If it shows `Python 2.x`, change the default using:
```bash
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.x 1
sudo update-alternatives --config python  # Choose Python 3.x
```
Verify with:
```bash
python --version
```

### **Issue 2: `pip3` Not Found**
If `pip3` (Python package manager) is missing:
```bash
sudo apt install python3-pip -y
pip3 --version
```

### **Issue 3: `apt` Fails Due to Conflicting Python Versions**
If you installed Python from source and `apt` is broken, fix it with:
```bash
sudo apt --fix-broken install
```

### **Issue 4: `ModuleNotFoundError` After Installing Python from Source**
If Python 3 is missing standard libraries:
```bash
sudo apt install python3-venv python3-distutils python3-dev -y
```

### **Issue 5: `cannot import name '_ssl'`**
Fix by installing missing SSL dependencies:
```bash
sudo apt install libssl-dev
```

### **Issue 6: `make` Command Not Found**
If you encounter:
```
make: command not found
```
Install it using:
```bash
sudo apt install build-essential -y
```

---

## **Final Check**
Ensure everything is set up correctly:
```bash
python3 --version
pip3 --version
which python3
which pip3
```

