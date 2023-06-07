const btns = document.getElementsByTagName('button')

for (let btnCount = 0;btnCount<btns.length;btnCount++){
    btns[btnCount].onclick = (e) => {
        if (e.target.innerText === "Submit") {
            let form = document.createElement('form')
            form.action = 'submit'
            form.method = 'post'
            let formQuestion = document.createElement('input'), formAnswer = document.createElement('input')
            formQuestion.name = 'question'
            formQuestion.value = document.getElementsByClassName('question')[0].innerText
            form.innerHTML+=csrf
            form.appendChild(formQuestion)
            let options = document.getElementsByName('option')
            for (let i = 0;i<options.length;i++) {
                if (options[i].checked) {
                    formAnswer.name = 'answer'
                    formAnswer.value = options[i].value
                }
            }
            if (formAnswer.name === '') {
                alert('select an option')
                return
            }
            form.appendChild(formAnswer)
            document.getElementsByClassName("container")[0].appendChild(form)
            form.submit()
            document.getElementsByClassName("container")[0].removeChild(form)
        } else if (e.target.innerText === "Reset") {
            let options = document.getElementsByName('option')
            for (let i = 0;i<options.length;i++) {
                options[i].checked = false
            }
        } else if (e.target.innerText === "Finish") {
            console.log('Clicked')
            window.location = '/score'
        }
    }
}