#  SafeClick – URL-Risk-Detection-System

SafeClick is a web-based security application that analyzes URLs for phishing, malicious intent, and suspicious behavior using a combination of rule-based checks and machine learning.

It helps users determine whether a link is **Safe, Suspicious, or Dangerous** before interacting with it.

---

##  Features

-  URL risk analysis in real-time  
-  Machine Learning-based prediction  
-  Pattern-based phishing detection  
-  Domain trust analysis  
-  Redirect tracking  
-  Risk scoring system (0–100)  
-  Explanation of detected risks  
-  QR code scanning support  
-  User reporting system (domain memory)

---

##  Project Structure

![structure](https://github.com/user-attachments/assets/03c2c035-e6e3-4730-8123-3d416ce6d730)

---

##  How It Works

1. User inputs a URL or scans a QR code  
2. URL is normalized and cleaned  
3. Multiple checks are performed:
   - Pattern detection  
   - Redirect tracking  
   - Domain analysis  
   - User reports  
   - ML prediction  
4. All signals are combined into a **risk score (0–100)**  
5. Final classification:
   - ✅ Safe  
   - ⚠️ Suspicious  
   - ❌ Dangerous  
6. Explanation is generated for the result  

---

## 🤖 Machine Learning

- Model: Random Forest Classifier  
- Features used:
  - URL length  
  - Number of dots and hyphens  
  - HTTPS usage  
  - Suspicious keywords  
  - Digit count  
  - Subdomain count  
  - IP usage  

- Output:
  - Probability of URL being malicious  

---

##  Running the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
