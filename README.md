# MCQ Website

Welcome to the MCQ Website, an interactive platform for teachers to create and manage quizzes and for students to participate in quizzes and view their performance on the leaderboard.

## Features

### For Teachers:
- **Create Quizzes**: Teachers can create quizzes with multiple-choice questions (MCQs).
- **Edit/Delete Quizzes**: Update or remove quizzes and questions easily.
- **View Quiz Submissions**: Check the students' quiz responses.
- **Leaderboard**: See the top-performing students for each quiz.

### For Students:
- **Take Quizzes**: Students can take available quizzes created by teachers.
- **Real-Time Feedback**: After submitting the quiz, students can view their scores immediately.
- **Leaderboard**: Students can view the overall leaderboard and compare their scores with other students.
- **Responsive Design**: Optimized for desktop and mobile devices.

## Technologies Used
- **Django**: Backend framework for handling user authentication, quiz creation, and submissions.
- **HTML/CSS/Bootstrap**: Frontend design for a user-friendly interface.
- **SQLite**: Database for storing quiz questions, answers, and user information.
- **JavaScript**: Interactivity for dynamic content updates.

## How to Use

### For Teachers:
1. **Sign Up**: Create an account or log in as a teacher.
2. **Create a Quiz**: Navigate to the "Create Quiz" page and add your quiz title, description, and questions.
3. **Manage Quizzes**: You can view, edit, or delete any quizzes you've created.

### For Students:
1. **Sign Up**: Create an account or log in as a student.
2. **Take a Quiz**: Browse the available quizzes and take the quiz of your choice.
3. **View Results**: After submitting the quiz, view your score and correct answers.
4. **Leaderboard**: See your rank on the leaderboard based on your performance across quizzes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/quiz-website.git
    cd quiz-website
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for teacher access):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and visit:
    ```
    http://127.0.0.1:8000
    ```

## Contributing
If you'd like to contribute to this project, feel free to submit pull requests or report issues.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
