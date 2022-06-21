$(document).ready(function(){
    $("#registration_btn").click(function(){
    var serializeData = $("#registration_form").serialize();
    $.ajax({
        url: "/Registration_ajax",
        data:serializeData,
        type: "POST",
        success: function(one,two,three){
    alter("hi");
        },
        error: function(one,two,three)
        {
    alter("why");
        }
    })
    });
        });