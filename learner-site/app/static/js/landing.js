
const MOBILE_FIELD_VALUE_FROM_BACKEND_FOR_SIGNUP = "{{ given_mobile }}";
document.getElementById("{{ SF.user.id_for_label }}").value = MOBILE_FIELD_VALUE_FROM_BACKEND_FOR_SIGNUP;
let SIGNIN_ALLOWED = true;

document.getElementById("{{SF.user.id_for_label}}").addEventListener("keyup",()=>{
    function validateMobile(mobile){
        if(mobile.length!=10)
            return false;

        const regex = /^(?!0+$)\d+$/;
        return regex.test(mobile);
    }

    const ERR_X = document.getElementsByClassName("errMsgMobile")[0];
    
    if(validateMobile(document.getElementById("{{SF.user.id_for_label}}").value)){
        ERR_X.textContent = "";
        SIGNIN_ALLOWED &= true;
    } else {
        ERR_X.style.color = "red";
        ERR_X.textContent = "Malformed mobile number";
        SIGNIN_ALLOWED = false;
    }
});



function isSignAllowed(){
    const ERR_MOB = document.getElementsByClassName("errMsgTotal")[0];
    
    if(document.getElementById("{{SF.user.id_for_label}}").value==''||document.getElementById("{{SF.fname.id_for_label}}").value==''||document.getElementById("{{SF.lname.id_for_label}}").value==''||document.getElementById("{{SF.email.id_for_label}}").value==''||document.getElementById("{{SF.pass1.id_for_label}}").value==''){
        ERR_MOB.style.color = "orange";
        ERR_MOB.textContent = "Empty fields exist";
        SIGNIN_ALLOWED = false;
        return false;
    }


    if(SIGNIN_ALLOWED){
        ERR_MOB.textContent = "";
    } else {
        ERR_MOB.style.color = "red";
        ERR_MOB.textContent = "Not all fields are valid";
    }

    return SIGNIN_ALLOWED;
}




function checkOneWord(n){
    let NAME = "";
    let ERR_BOX = "";
    let RE = /^[a-zA-Z]+$/;

    if(n==1){
        NAME = document.getElementById("{{SF.fname.id_for_label}}");
        ERR_BOX = document.getElementsByClassName("errMsgFName")[0];
    }
    else{
        NAME = document.getElementById("{{SF.lname.id_for_label}}");
        ERR_BOX = document.getElementsByClassName("errMsgLName")[0];
    }

    console.log(NAME.value,"...",RE.test(NAME.value))
    if(RE.test(NAME.value) & NAME.value.length>1){
        ERR_BOX.textContent = "";
        SIGNIN_ALLOWED &= true;
    } else {
        ERR_BOX.style.color = "red";
        ERR_BOX.textContent = "Name can't have spaces, digits or special characters";
        SIGNIN_ALLOWED = false;
    }

}


document.getElementById("{{SF.fname.id_for_label}}").addEventListener("keyup",() => { checkOneWord(1) });
document.getElementById("{{SF.lname.id_for_label}}").addEventListener("keyup",() => { checkOneWord(2) });


document.getElementById("pass2").addEventListener("keyup",() => { 

    const p1 = document.getElementById("{{ SF.pass1.id_for_label }}").value;
    const p2 = document.getElementById("pass2").value;

    const ERR_RE_PASS = document.getElementsByClassName("errMsgConfirmPass")[0];

    if(p1 == p2){
        console.log([p1,p2]);
        ERR_RE_PASS.style.color = "green";
        ERR_RE_PASS.textContent = "Passwords match!";
        SIGNIN_ALLOWED &= true;
        return;
    }

    ERR_RE_PASS.style.color = "red";
    ERR_RE_PASS.textContent = "Passwords don't match";
    SIGNIN_ALLOWED = false;

});


document.getElementById("{{ SF.pass1.id_for_label }}").addEventListener("keyup", () => {
    const PASS = document.getElementById("{{ SF.pass1.id_for_label }}").value;
    const ERR_PASS = document.getElementsByClassName("errMsgPass")[0];

    if(PASS==''){
        ERR_PASS.style.color = "red";
        ERR_PASS.textContent = "Password can't be empty";
        SIGNIN_ALLOWED = false;
        return;
    }

    const RE = /^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=_]).*$/;

    if(RE.test(PASS)){
        if(PASS.length>8){
            ERR_PASS.textContent = "";
            SIGNIN_ALLOWED &= true;
            return;
        } else {
            ERR_PASS.style.color = "red";
            ERR_PASS.textContent = "Password should be atleast 8 characters long";
            SIGNIN_ALLOWED = false;
        }
    } else {
        ERR_PASS.style.color = "red";
        ERR_PASS.textContent = "Password should have atleast one lower, upper case letter, one digit, and one special character from: @#$%^&+=_";
        SIGNIN_ALLOWED = false;
    }
});
