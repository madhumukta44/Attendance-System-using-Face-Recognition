const toggel=document.querySelectorAll('.toggel')
const password=document.querySelectorAll('.Password')


toggel[0].addEventListener('click',()=>{
    if(password[0].type == 'password'){
        password[0].type='text'
        toggel[0].innerHTML= '<i class="fa fa-eye-slash"></i>' 
    }
    else
    {
        password[0].type='password'
        toggel[0].innerHTML= '<i class="fa fa-eye"></i>'
    }
}
)
toggel[1].addEventListener('click',()=>{
    if(password[1].type == 'password'){
        password[1].type='text'
        toggel[1].innerHTML= '<i class="fa fa-eye-slash"></i>' 
    }
    else
    {
        password[1].type='password'
        toggel[1].innerHTML= '<i class="fa fa-eye"></i>'
    }
}
)