const displayForm = (e) => {
    var form = document.getElementById("quizForm");
    if(form.style.display === "none" || form.style.display === "") {
        form.style.display = 'block';
    }
    else {
        form.style.display = "none";
    }
}

const deleteQuiz = (quiz_id) => {
    fetch(quiz_id+'/delete_quiz')
    .then(response => response.json())
    .then(data => {
        if(data.message === "Success") document.getElementById("Quiz_"+quiz_id).remove();
    });
}

const toggleEditMode = (quiz_id) => {
    var detailDiv = document.getElementById("quiz_detail_"+quiz_id);
    var editDiv = document.getElementById("edit_form_"+quiz_id);
    if(detailDiv.style.display === "none") {
        detailDiv.style.display = "block";
        editDiv.style.display = "none";
    }
    else {
        detailDiv.style.display = "none";
        editDiv.style.display = "block";
    }
}

const showQuestions = (quiz_id) => {
    window.location.assign(quiz_id + '/show_questions');
}