# Student Grade Calculator

## 📖 Project Overview
The Student Grade Calculator is a Python-based command-line application designed to evaluate student performance. It accepts a student's name and numerical marks, rigorously validates the input, and calculates the appropriate letter grade[cite: 1]. Alongside the grade, it provides a tailored, encouraging feedback message to the student[cite: 1]. 

## 🗂️ Code Structure
The repository is organized as follows to maintain a clear file hierarchy:
*   `README.md`: Project documentation and setup guidelines.
*   `grade_calculator.py`: The main Python executable script containing the program logic and grading functions[cite: 1].
*   `test_cases.txt`: A text file documenting various input scenarios and their expected outputs.
*   `screenshots/`: A directory containing visual evidence of the program running successfully.

## ⚙️ Setup Instructions
Follow these step-by-step instructions to configure and run the project locally:
1.  **Prerequisites:** Ensure you have Python 3.x installed on your system.
2.  **Clone the Repository:** Download or clone the project files to your local machine.
3.  **Navigate to the Directory:** Open your terminal or command prompt and change the directory to the project folder.
4.  **Run the Application:** Execute the script using the following command:
    ```bash
    python grade_calculator.py
    ```
5.  **Follow Prompts:** Enter the student's name and marks as prompted in the console[cite: 1].

## 🧠 Technical Details & Documentation

### Algorithms and Architecture
The application relies on sequential execution and conditional branching (`if-elif-else` statements) to map numerical scores to distinct grade categories[cite: 1]. 

### Functions Used
The script is modularized into two primary functions:
*   `calculate_grade(marks)`: This function contains the core grading logic[cite: 1]. It evaluates the passed numerical marks against predefined thresholds and returns a tuple containing the corresponding letter grade and a specific feedback message[cite: 1].
*   `main()`: This function handles user interaction and continuous input validation[cite: 1]. It utilizes a `while True` loop and a `try...except ValueError` block to ensure the program doesn't crash upon receiving non-numeric inputs[cite: 1].

### Grading Logic
The evaluation criteria implemented in `calculate_grade(marks)` is strictly defined as follows[cite: 1]:
*   **90 to 100:** Grade `A` — "Excellent! You are doing amazing work! 🌟"[cite: 1]
*   **80 to 89.9:** Grade `B` — "Very Good! Keep it up! 👍"[cite: 1]
*   **70 to 79.9:** Grade `C` — "Good job! With a little more effort, you can reach the top! 📈"[cite: 1]
*   **60 to 69.9:** Grade `D` — "Passed. Let's work harder next time to boost this score! 📚"[cite: 1]
*   **Below 60:** Grade `F` — "Don't give up! Reach out for help and try again. You can do it! 💪❤️"[cite: 1]

## 🧪 Testing Evidence
The application includes robust input validation ensuring that marks strictly fall between 0 and 100[cite: 1]. 

**Example Test Cases (Documented in `test_cases.txt`):**
*   *Valid High Score:* Inputting `95` correctly yields an `A` grade[cite: 1].
*   *Valid Borderline Score:* Inputting `60` correctly yields a `D` grade[cite: 1].
*   *Out of Bounds Error:* Inputting `105` triggers the warning: `"Invalid input. Marks must be between 0 and 100."`[cite: 1].
*   *Value Error (String input):* Inputting `abc` triggers the exception warning: `"Invalid input. Please enter a valid number."`[cite: 1].

## 📸 Visual Documentation
*(Note: Add actual image files to the `screenshots/` folder and update these paths)*
*   ![Successful Grade Calculation](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week2-grade_calculator/Screenshot%202026-08-28%20090934.png)
    *Caption: Demonstrates a successful grade calculation with formatted emoji output.*
*   ![Input Validation Handling](https://github.com/SugamSagar-DS458/TheDeveloperArena-Internship-Projects/blob/main/Week2-grade_calculator/Screenshot%202026-08-28%20091502.png)
    *Caption: Demonstrates the program successfully catching and rejecting alphabetical inputs and out-of-range numbers.*

---
## ✅ Quality Standards Checklist
- [x] Project Overview included
- [x] Setup Instructions provided
- [x] Code Structure outlined
- [x] Grading logic and functions explained
- [x] Technical details (algorithms/architecture) detailed
- [x] Testing evidence and examples provided
- [x] Visual documentation placeholders included
