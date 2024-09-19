const displayForm = (e) => {
    console.log("hello");
    var form = document.getElementById("quizForm");
    if(form.style.display === "none" || form.style.display === "") {
        form.style.display = 'block';
    }
    else {
        form.style.display = "none";
    }
}