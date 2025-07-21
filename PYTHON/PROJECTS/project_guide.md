
# 📄 Resume Parser Project — Beginner to Advanced Notes

---

## ✅ **What This Project Does (Plain English)**

This Python project reads resumes in **multiple file formats** (PDF, DOCX, TXT), extracts **important candidate details**, and prints them out in a structured format. It’s like the **first step of an automated HR system**, doing the initial data extraction before a recruiter reviews the resume.

It extracts:

* **Contact Info:** Name, email, phone number, and address.
* **Education Info:** Detected degrees and qualifications.
* **Work Experience:** Job roles and domains mentioned in the resume.

---

## 🔍 **How the Code Works**

---

### **1. Reading the Resume File**

```python
def extract_text(filepath):
```

✔️ Handles PDF, DOCX, and TXT formats.
✔️ Uses **PyMuPDF (`fitz`)** for PDF, **python-docx** for DOCX, and native reading for TXT.

* **PDF:** Reads the text from each page.
* **DOCX:** Reads each paragraph.
* **TXT:** Reads the whole file as plain text.

Example usage:

```python
resume_text = extract_text("resumes/resume2.pdf")
```

---

### **2. Extracting Contact Details**

```python
def extract_contact_details(text):
```

✔️ Uses **regular expressions** to find:

* ✅ Email addresses (e.g., [john@example.com](mailto:john@example.com))
* ✅ Phone numbers in multiple formats (+91 98765 43210, 9876543210, etc.)

✔️ Naively assumes the **first line is the candidate's name**.
✔️ Looks for any line containing the word “address”.

Example output:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+91 9876543210",
  "address": "Address: 123, Main Street"
}
```

---

### **3. Extracting Education**

```python
def extract_education(text):
```

✔️ Searches for common education keywords like **"Bachelor", "Master", "PhD"**.
✔️ Collects any lines containing those words.

Example output:

```json
{
  "total_qualifications": 2,
  "qualifications": [
      "Bachelor of Engineering in Computer Science",
      "Master of Science in Data Science"
  ]
}
```

---

### **4. Extracting Work Experience**

```python
def extract_experience(text):
```

✔️ Searches for lines that mention “experience” or common job titles like **“developer”, “manager”, “finance”**.
✔️ Collects them in a list.

Example output:

```json
{
  "total_experiences": 3,
  "experiences": [
      "5 years of experience in software development",
      "Worked as a machine learning engineer",
      "Lead a team of data analysts"
  ]
}
```

---

### **5. Final Output Example**

The results are printed like this:

```python
print("Candidate Details:", contact)
print("Education:", education)
print("Experience:", experience)
```

---

## 🌟 **How Beginners Can Improve This Project**

---

### 🛡️ More Accurate Data Extraction:

* Use **spaCy's NER (Named Entity Recognition)** to extract names, locations, and organizations:

  * PERSON → candidate's name
  * GPE/LOC → address/location
  * ORG → education/workplace names

---

### 📚 Smarter Education & Experience Parsing:

* Extract not only degree names but also **college names, year of graduation, and GPA**.
* For experience:

  * Extract **years worked, company names, job roles**, and **technologies used**.

---

### 🗃️ Add a Database:

* Save the extracted results to a **CSV, SQLite, or MongoDB** database.
* Later you could build a search system over these resumes.

---

### 🌐 Turn into a Web App:

* Convert the script into a web app using:

  * **Flask or FastAPI** for the backend.
  * **Streamlit** for a drag-and-drop web interface.

---

### 🔎 Improve Resume Search:

* Add a **keyword search** to let HR filter candidates:

  * Example: "Find all candidates with Python + AWS + SQL skills."

---

### ⚙️ Process a Folder of Resumes:

* Instead of one file, scan a **whole folder of resumes** and summarize results for each.

---

### 🔑 Add Scoring Logic:

* Score resumes based on:

  * Skills matched from the job description.
  * Years of experience.
  * Education level.
* Example: “85% match for Backend Developer role.”

---

### ☁️ Deploy to Cloud:

* Deploy your web app on **Render, Railway, Heroku**, or **AWS EC2**.

---

## 🎯 **Summary for Beginners**

➡️ A great starter project covering:

* File reading in Python
* Regex basics for text search
* Simple text parsing
* Clean project structure

➡️ **Next level upgrades:**

* Use **real NLP tools** (spaCy, transformers)
* Turn it into an API or web app
* Add a database and search
* Improve accuracy with AI models

---

If you want to improve this together step by step (API, spaCy, scoring system, frontend), just ask — I’ll help you build and deploy it!
