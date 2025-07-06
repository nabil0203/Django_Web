# 📘 Contact Book Management System (CLI Python Project)

## OVERVIEW

In this assignment, you are required to develop a Command Line Interface (CLI) project using Python for a Contact Book Management System. The project should apply the Python concepts you’ve learned throughout the course. You are not required to use any Graphical User Interface (GUI), frameworks, or external libraries - everything should run directly in the terminal.

> **Note:** Avoid using AI tools, as it is essential to build skills independently for your long-term career growth.

---

## TASKS

### ➕ Add Contacts:
- Allow users to add contacts with at least the following details: Name, Email, Phone Number, and Address.
- You can include additional fields if necessary.

### 🚫 Prevent Duplicate Numbers:
- Ensure that the same phone number cannot be assigned to multiple names.

### 📄 View Contacts:
- Display all saved contacts in a well-organized format. A neat and user-friendly presentation is encouraged.

### 💾 Save to File:
- Store all contact information in a file of your choice (example: `.txt`, `.csv`, `.json`, etc.).
- Contacts should be automatically saved to the file upon addition.

### 📂 Load from File:
- Ensure all previously saved contact data is loaded when the program starts.

### ❌ Remove Contacts:
- Provide an option to delete contacts from the file.

---

## BONUS FEATURES

### 🔍 Search Contacts:
- Implement functionality to search for specific contacts based on their details.

### ⚠️ Error Handling:
Display meaningful error messages for invalid inputs, such as:
- The contact’s name must be a string.
- The phone number must be an integer.
- Provide clear guidance to users on resolving input issues.

---

## NOTES

### 🗃️ File Structure:
Organize your project into multiple Python files, each dedicated to specific features or functionalities.

### ♻️ Modular Code:
Write reusable and maintainable code by encapsulating features within functions.

### 🚫 No External Libraries:
Use only the Python as taught in the course. Avoid third-party packages or frameworks.

### 🧭 Menu System:
Design an interactive menu with an Exit option for easy navigation. All features should be accessible from this menu.

---

## 📤 Submission

Submit your project via **GitHub Repository Link** or **Zip file**.  
⚠️ If you provide a **private GitHub link**, it will result in **zero marks**.

---
---
---

## Sample 1: Program Startup (Loading Contacts)
Welcome to the Contact Book CLI System!

Loading contacts from contacts.csv... Done!

=========== MENU ===========

1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit

============================

Enter your choice: 
