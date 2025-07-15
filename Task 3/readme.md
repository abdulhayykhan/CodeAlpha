# ⚙️ Task 3 – Task Automation: Email Extractor

This task demonstrates the automation of a real-world problem using Python:  
**Extracting all email addresses** from a `.txt` file and saving them to a separate output file.

---

## ✅ Features

- Reads an input `.txt` file line by line
- Uses regular expressions to identify valid email addresses
- Handles file not found errors with `try-except`
- Saves all found email addresses to a new file (`extracted_emails.txt`)
- Displays total number of emails extracted

---

## 🧠 Concepts Used

- `re` module (regular expressions)
- File handling (`open()`, `read()`, `write()`)
- Exception handling using `try-except`
- String manipulation and pattern matching
- Basic automation workflow

---

## 🧪 Logic Overview

1. Open a `.txt` file containing any kind of text.
2. Use a regular expression pattern to match email addresses: [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}
3. Extract all matches and store them in a list.
4. Write the matched emails into a new `.txt` file.
5. If no emails are found, notify the user.

---

## 📸 Example Interaction

- Extracting emails from 'sample_text.txt'...

- ✅ 3 email(s) extracted and saved to 'extracted_emails.txt'


📄 Content of `sample_text.txt`:
Hello Team,

Please contact us at support@example.com or hr@company.org.
Also reach out to xyzname@mailservice.net for collaboration.

Regards,
Admin


📄 Output in `extracted_emails.txt`:
- support@example.com
- hr@company.org
- xyzname@mailservice.net

---

## 🙋‍♂️ Author

**Abdul Hayy Khan**  
Python Developer | CodeAlpha Intern

---

## 📜 License

This project was created as part of the **CodeAlpha Python Internship** and is intended for learning and demonstration purposes only.

