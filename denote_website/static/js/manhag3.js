/*$(document).ready(function(){
   /* var r =Number(document.getElementById(".numb").value);
    var p =Number(document.getElementById(".numb2").value); 
    var o = (6000 / 10);
    $(".presint").animate({
        width: o
    });

    
});*/
$(document).ready(function(){
    
    $(".contact").hide()
   
});

$(document).ready(function(){
    $(".contact .clos").click(function(){
        $(".contact").hide()
    });
});
$(document).ready(function(){
    $(".list #open").click(function(){
        $(".contact").show()
    });
});


$(document).ready(function(){
    
    $(".partners").hide()
   
});

$(document).ready(function(){
    $(".partners .clos1").click(function(){
        $(".partners").hide()
    });
});
$(document).ready(function(){
    $(".list #open1").click(function(){
        $(".partners").show()
    });
});




$(document).ready(function(){
    
    $(".about").hide()
   
});

$(document).ready(function(){
    $(".about .clos2").click(function(){
        $(".about").hide()
    });
});
$(document).ready(function(){
    $(".list #open2").click(function(){
        $(".about").show()
    });
});

