
const MOBILE_FIELD_VALUE_FROM_BACKEND_FOR_LOGIN = "{{ given_mobile }}";
document.getElementById("{{ LF.username.id_for_label }}").value = MOBILE_FIELD_VALUE_FROM_BACKEND_FOR_LOGIN;
let LOGIN_ALLOWED = true;


document.getElementById("{{LF.username.id_for_label}}").addEventListener("keyup",()=>{
    function validateMobile(mobile){
        if(mobile.length!=10)
            return false;

        const regex = /^(?!0+$)\d+$/;
        return regex.test(mobile);
    }

    const ERR_X = document.getElementsByClassName("errMsgMobile")[0];
    
    if(validateMobile(document.getElementById("{{LF.username.id_for_label}}").value)){
        ERR_X.textContent = "";
        LOGIN_ALLOWED &= true;
    } else {
        ERR_X.style.color = "red";
        ERR_X.textContent = "Malformed mobile number";
        LOGIN_ALLOWED = false;
    }
});



function isSignAllowed(){
    const ERR_MOB = document.getElementsByClassName("errMsgMobile")[0];

    if(LOGIN_ALLOWED){
        ERR_MOB.textContent = "";
        LOGIN_ALLOWED = true;
    } else {
        ERR_MOB.style.color = "red";
        ERR_MOB.textContent = "Invalid mobile number";
        LOGIN_ALLOWED = false;
    }
    return (LOGIN_ALLOWED)? true : false;
}
