const API = "http://localhost:5000"

function addStudent(){

let name = document.getElementById("name").value
let marks = document.getElementById("marks").value

fetch(API + "/add",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
name:name,
marks:marks
})
})

.then(res=>res.json())
.then(data=>{
alert(data.message)
loadStudents()
})

}

function loadStudents(){

fetch(API + "/students")

.then(res=>res.json())

.then(data=>{

let list=document.getElementById("list")
list.innerHTML=""

data.forEach(s=>{
list.innerHTML+=`<li>${s[1]} - ${s[2]}</li>`
})

})

}

loadStudents()