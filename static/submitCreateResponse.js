let btn = document.getElementsByTagName('button')
let p = document.getElementsByTagName('textarea')
let inp = document.getElementsByTagName('input')

for (let i = 0;i<btn.length;i++) {
    btn[i].onclick = (e) => {
        if (e.target.innerText === "Submit") {
            let flag = 1
            var ans = document.createElement('input')
            ans.type = 'text'
            for (let tc = 0;tc<p.length;tc++) {
                if (p[tc].value.trim() === "") {
                    p[tc].focus()
                    alert('Value Missing')
                    return
                }
                if (p[tc].previousSibling.checked) {
                    flag = 0
                    ans.name = 'answer'
                    ans.value = p[tc].value
                }
            }
            let form = document.createElement('form')
            form.action = 'create'
            form.method = 'post'
            form.innerHTML+=csrf
            form.appendChild(p[0].cloneNode(true))
            form.appendChild(p[1].cloneNode(true))
            form.appendChild(p[2].cloneNode(true))
            form.appendChild(p[3].cloneNode(true))
            form.appendChild(p[4].cloneNode(true))
            form.appendChild(ans.cloneNode(true))
            document.getElementsByClassName('container')[0].appendChild(form)
            form.submit()
            document.getElementsByClassName('container')[0].removeChild(form)
        } else if (e.target.innerText === "Reset") {
            p[0].value = "Enter your Question Here"
            p[1].value = "Option 1"
            p[2].value = "Option 2"
            p[3].value = "Option 3"
            p[4].value = "Option 4"
        }
    }
}