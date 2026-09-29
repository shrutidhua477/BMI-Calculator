# BMI Health Tracker

## 1. Project Overview

BMI Health Tracker is a beginner-friendly Python-based application that calculates a user's Body Mass Index (BMI) using their height and weight.

The application accepts basic user information, calculates BMI, identifies the corresponding BMI category, and provides a basic health suggestion. The program also allows the user to perform multiple BMI calculations during the same session.

The project is implemented using multiple Python modules to maintain a simple and organized structure.

---

## 2. Features

* Accepts the user's name and age.
* Accepts height in meters.
* Accepts weight in kilograms.
* Calculates Body Mass Index (BMI).
* Displays the calculated BMI value.
* Identifies the BMI category.
* Provides a basic health suggestion based on the BMI category.
* Allows the user to calculate BMI multiple times.
* Provides an option to exit the program.
* Handles invalid yes/no choices.

---

## 3. Technologies and Tools Used

* **Programming Language:** Python
* **Development Environment:** Python IDLE
* **Version Control:** Git
* **Repository Hosting:** GitHub

---

## 4. Project Structure

```text
BMI_Health_Tracker/
│
├── main.py
├── user_input.py
├── bmi_calculation.py
├── bmi_category.py
├── health_suggestion.py
├── display_result.py
│
├── README.md
├── statement.md
│
└── screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

### Description of Python Modules

| File                   | Purpose                                                          |
| ---------------------- | ---------------------------------------------------------------- |
| `main.py`              | Controls the overall program workflow.                           |
| `user_input.py`        | Collects user information such as name, age, height, and weight. |
| `bmi_calculation.py`   | Calculates the user's BMI.                                       |
| `bmi_category.py`      | Determines the BMI category.                                     |
| `health_suggestion.py` | Provides a basic suggestion based on the BMI category.           |
| `display_result.py`    | Displays the final BMI result to the user.                       |

---

## 5. How to Run the Project

### Step 1: Download the Project

Download or clone this GitHub repository to your computer.

### Step 2: Keep the Files Together

Make sure all six Python files are located in the same folder.

### Step 3: Open the Main Program

Open `main.py` using Python IDLE.

### Step 4: Run the Program

In Python IDLE:

**Run → Run Module**

or press:

**F5**

### Step 5: Enter the Required Information

The program will ask the user for:

* Name
* Age
* Height in meters
* Weight in kilograms

The program will then calculate and display the BMI and its category.

---

## 6. Example Program Workflow

```text
Start
  ↓
Ask whether the user wants to calculate BMI
  ↓
Enter user details
  ↓
Calculate BMI
  ↓
Determine BMI category
  ↓
Generate health suggestion
  ↓
Display result
  ↓
Ask whether the user wants another calculation
  ↓
Yes → Repeat
No → Exit
```

---

## 7. Testing

The application can be tested using different input values and user choices.

### Test Cases

| Test Case | Input/Action                    | Expected Result                                 |
| --------- | ------------------------------- | ----------------------------------------------- |
| 1         | Enter `yes`                     | User details are requested.                     |
| 2         | Enter valid height and weight   | BMI is calculated and displayed.                |
| 3         | BMI below 18.5                  | `Underweight` category is displayed.            |
| 4         | BMI between 18.5 and 24.9       | `Healthy Weight` category is displayed.         |
| 5         | BMI between 25 and 29.9         | `Overweight` category is displayed.             |
| 6         | BMI 30 or above                 | `Obese` category is displayed.                  |
| 7         | Enter `no` at the beginning     | Program exits.                                  |
| 8         | Enter `yes` after a calculation | Another BMI calculation starts.                 |
| 9         | Enter `no` after a calculation  | Program displays a thank-you message and exits. |
| 10        | Enter an invalid yes/no choice  | Program displays an invalid-choice message.     |

---

## 8. Screenshots

Screenshots demonstrating the execution and results of the program are available in the `screenshots` folder.

The screenshots include:

* Program starting screen
* BMI calculation result
* Multiple-calculation/exit option

---

## 9. Input and Output

### Input

The program accepts:

* User name
* User age
* Height in meters
* Weight in kilograms
* Yes/no choices for continuing the program

### Output

The program displays:

* User name
* User age
* Calculated BMI
* BMI category
* Basic health suggestion
* Program exit message

---

## 10. Project Purpose

The purpose of this project is to apply Python programming concepts to a simple real-world problem. The project demonstrates modular programming, functions, conditional statements, loops, user input, calculations, and basic validation.

PROGRAM SCREENSHOTS
<img width="1366" height="721" alt="image" src="https://github.com/user-attachments/assets/82a81c5a-2828-4746-8eea-407f9fdcbd0d" />
<img width="1366" height="726" alt="image" src="https://github.com/user-attachments/assets/74161623-5f8a-4927-b631-2b0fde7e9bb7" />
Functional Module
user_inout()
<img width="1366" height="726" alt="image" src="https://github.com/user-attachments/assets/ff485eec-093d-4ae2-a730-bacb1a6ce696" />
bmi_calculation()
<img width="1365" height="724" alt="image" src="https://github.com/user-attachments/assets/eab8fe01-e2c9-48cf-b658-b30412000f77" />
bmi_category()
<img width="1363" height="730" alt="image" src="https://github.com/user-attachments/assets/41ca8aaf-9a17-4254-a898-009701c909ff" />
category_suggestion()
<img width="1361" height="729" alt="image" src="https://github.com/user-attachments/assets/eb2151cd-2fdc-4996-a53f-418531c3ae32" />
display_result()
<img width="1366" height="730" alt="image" src="https://github.com/user-attachments/assets/bfed04bd-b699-4c53-8350-ca0e17660771" />
result
<img width="1363" height="729" alt="image" src="https://github.com/user-attachments/assets/d1248186-c2cb-4806-afb5-7f679d88325b" />
<img width="1365" height="730" alt="image" src="https://github.com/user-attachments/assets/0cbb9619-0cee-4bf3-bad0-138dbd7f3c7f" />

---

## 11. Author

**Student Project — VITyarthi Build Your Own Project**

**Project:** BMI Health Tracker
