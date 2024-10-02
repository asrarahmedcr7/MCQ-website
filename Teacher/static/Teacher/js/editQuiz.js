function callDeleteChoice(choice_id, question_id) {
    fetch(`${question_id}/${choice_id}/delete-choice`)
    .then(response => response.json())
    .then(data => {
        if(data.message === "Success") {
            document.getElementById("choice_"+choice_id).remove();
        }
    });
};

function toggleAddChoiceForm(event, question_id) {
    const choiceForm = document.getElementById("addChoiceForm_"+question_id);
    try {
        if(choiceForm.style.display === "block") {
            choiceForm.style.display = "none";
            event.target.innerHTML = "Add Choice";
        }
        else {
            choiceForm.style.display = "block";
            event.target.innerHTML = "Cancel";
        }
    } catch (TypeError) {
        choiceForm.style = "display:block;";
    }
};

function callDeleteQuestion(question_id) {
    fetch(question_id + '/deleteQuestion')
    .then(response => response.json())
    .then(data => {
        if(data.message === "Success") {
            document.getElementById("question_"+question_id).remove();
        }
    })
};

function callEditQuestion(e, question_id) {
    e.preventDefault();
    const formdata = new FormData(e.target);
    console.log(formdata);
    fetch(`${question_id}/editQuestion`, {
        method:'POST',
        body: formdata,
        headers: {
            'X-CSRFToken':getCSRFToken()
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.message === "Success") {
            window.alert("Question edited successfully");
        }
        else {
            window.alert("Enter Details Properly");
        }
    })
};

function callAddChoice(e, question_id) {
    e.preventDefault();
    const formdata = new FormData(e.target);
    fetch(`${question_id}/add-choice`, {
        method:'POST',
        body: formdata,
        headers: {
            'X-CSRFToken':getCSRFToken()
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.message === "Success") {
            const ul = document.getElementById(`question_${question_id}_choice_list`);
            const li = document.createElement('li');
            li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
            const inp = document.createElement('input');
            inp.type = 'text';
            inp.name = `choice_${data.choice_id}`;
            inp.setAttribute('value', data.choice_text);
            inp.setAttribute('class', 'form-control mr-2');
            const rem = document.createElement('input');
            rem.type = 'button';
            rem.setAttribute('value','Remove');
            rem.setAttribute('onclick', `callDeleteChoice(${data.choice_id}, ${question_id})`);
            rem.setAttribute('class','btn btn-danger');
            inp.required = true;
            li.id = `choice_${data.choice_id}`;
            li.appendChild(inp);
            li.appendChild(rem);
            ul.appendChild(li);
            e.target.reset();
        }
        else {
            window.alert("Enter Details Properly");
        }
    })
}

function getCSRFToken() {
    let cookieValue = null;
    const name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}