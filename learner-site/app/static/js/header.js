
    /* HIDE TAGS OF SECOND HEADER ROW ON RESIZE --------------------------------- */

    document.querySelector(".leftSection .titleContainer").addEventListener("click",() => {
        window.location.href = "/home/";
    })











    /* HIDE TAGS OF SECOND HEADER ROW ON RESIZE --------------------------------- */
    window.addEventListener("resize", () => { hideTags(); } );

    (() => { hideTags(); })();


    function hideTags(){
        
        const homeTags = document.getElementsByClassName("fieldContainer");
        const w = window.innerWidth;

        if(w<1310){
            document.getElementsByClassName("j")[0].style.display = "none";
            if(w<1240){
                document.getElementsByClassName("i")[0].style.display = "none";
                if(w<1080){
                    document.getElementsByClassName("h")[0].style.display = "none";
                    if(w<980){
                        document.getElementsByClassName("g")[0].style.display = "none";
                        if(w<910){
                            document.getElementsByClassName("f")[0].style.display = "none";
                        }
                    }
                }
            }

        }
        
        if(w>910){
            document.getElementsByClassName("f")[0].style.display = "flex";
            if(w>980){
                document.getElementsByClassName("g")[0].style.display = "flex";
                if(w>1080){
                    document.getElementsByClassName("h")[0].style.display = "flex";
                    if(w>1240){
                        document.getElementsByClassName("i")[0].style.display = "flex";
                        if(w>1310){
                            document.getElementsByClassName("j")[0].style.display = "flex";
                        }
                    }
                }
            }
        }





        if(w>1310){
            document.getElementsByClassName("j")[0].style.display = "flex";

            if(w>1230){
                document.getElementsByClassName("i")[0].style.display = "flex";

                if(w>1080){
                    document.getElementsByClassName("h")[0].style.display = "flex";

                    if(w>980){
                        document.getElementsByClassName("g")[0].style.display = "flex";


                    }
                }
            }
        }

    }

