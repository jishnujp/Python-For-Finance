# **How to Install Python on Windows & Troubleshooting Common Issues**

## **Step 1: Check if Python is Already Installed**
Before installing Python, check if it is already installed:

1. Open **Command Prompt (cmd)**.
2. Type:
   ```cmd
   python --version
   ```
   or
   ```cmd
   python3 --version
   ```
3. If Python is installed, you will see:
   ```
   Python 3.x.x
   ```
   If not, proceed with installation.

---

## **Step 2: Download and Install Python**
### **Method 1: Install Using the Official Installer (Recommended)**
1. **Download Python:**
   - Go to [Python's official website](https://www.python.org/downloads/windows/).
   - Click **Download Python 3.x.x** (latest version).

2. **Run the Installer:**
   - Open the downloaded `.exe` file.
   - **Important:** Check the box **"Add Python to PATH"** before clicking "Install Now".

3. **Wait for the installation to complete** and then click **Close**.

4. **Verify Installation:**
   - Open **Command Prompt** (`Win + R`, type `cmd`, press Enter).
   - Type:
     ```cmd
     python --version
     ```
     or
     ```cmd
     python3 --version
     ```
   - If Python is installed correctly, it will display the version number.

---

## **Step 3: Install pip (Python's Package Manager)**
After installing Python, `pip` (Python’s package manager) should be installed automatically.

### **Verify pip Installation**
```cmd
pip --version
```
If pip is not found, install it manually:
```cmd
python -m ensurepip --default-pip
python -m pip install --upgrade pip
```

---

## **Step 4: Setting Up Environment Variables (If Python Command Doesn’t Work)**
If you get the error `"python is not recognized as an internal or external command"`:

### **Solution: Manually Add Python to PATH**
1. Press **Win + R**, type `sysdm.cpl`, and hit **Enter**.
2. Go to the **Advanced** tab → Click **Environment Variables**.
3. Under **System Variables**, find and select **Path**, then click **Edit**.
4. Click **New** and add the following:
   ```
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts\
   ```
   *(Replace `Python3x` with the installed version, e.g., `Python311` for Python 3.11.)*
5. Click **OK** → **Apply** → **Restart your computer**.
6. Test Python again:
   ```cmd
   python --version
   ```

---

## **Step 5: Install Virtual Environment (Optional but Recommended)**
If you plan to work on multiple projects, it is good practice to use virtual environments.

1. Open **Command Prompt** and type:
   ```cmd
   python -m venv myenv
   ```
2. To activate the virtual environment:
   ```cmd
   myenv\Scripts\activate
   ```
3. To deactivate the virtual environment:
   ```cmd
   deactivate
   ```

---

## **Common Issues and Fixes**

### **Issue 1: `python` Command Not Found**
#### **Solution:**
1. Ensure Python is installed by checking:
   ```cmd
   where python
   ```
2. If Python is not found, add it to the system PATH (See **Step 4**).

---

### **Issue 2: `pip` Not Found**
#### **Solution:**
1. Try:
   ```cmd
   python -m ensurepip --default-pip
   python -m pip install --upgrade pip
   ```
2. If pip is still missing, reinstall Python and **ensure you check "Add Python to PATH"**.

---

### **Issue 3: `pip install` Fails with SSL Certificate Error**
#### **Error Message:**
```
Could not fetch URL due to SSL verification issue.
```
#### **Solution:**
1. Upgrade pip:
   ```cmd
   python -m pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
   ```
2. If the issue persists, reinstall Python.

---

### **Issue 4: `pip install` Fails Due to Missing Permissions**
#### **Error Message:**
```
PermissionError: [WinError 5] Access is denied
```
#### **Solution:**
Run the command prompt as **Administrator**:
1. Press **Win + S**, type `cmd`, right-click, and select **Run as administrator**.
2. Try installing the package again:
   ```cmd
   pip install package_name
   ```

---

### **Issue 5: `python` Points to Python 2 Instead of Python 3**
On some Windows systems, running `python` might launch **Python 2**.
#### **Solution:**
Use `python3` instead:
```cmd
python3 --version
```
Or manually update Python in system variables (See **Step 4**).

---

### **Issue 6: Virtual Environment Activation Fails**
#### **Error Message:**
```
venv\Scripts\activate : File cannot be loaded because running scripts is disabled
```
#### **Solution:**
Enable execution of scripts:
```cmd
Set-ExecutionPolicy Unrestricted -Scope Process
```
Then, activate the virtual environment:
```cmd
myenv\Scripts\activate
```

---

### **Final Check**
Run these commands to confirm Python is installed correctly:
```cmd
python --version
pip --version
where python
```

---

## **Summary**
✅ **Install Python on Windows:**
- Download from [python.org](https://www.python.org/downloads/windows/).
- Run the installer and **check "Add Python to PATH"**.
- Verify using `python --version`.

✅ **Fix Common Issues:**
- **Python not found?** Add it to **Environment Variables**.
- **pip not found?** Use `python -m ensurepip --default-pip`.
- **SSL errors?** Upgrade pip with `--trusted-host`.
- **Permission issues?** Run Command Prompt as **Administrator**.
- **Virtual environment issues?** Enable scripts using `Set-ExecutionPolicy`.

