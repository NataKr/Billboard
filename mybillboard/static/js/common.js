console.log("I am index");
Billboard={};

$(document).ready(function(){
    Billboard.bindButtonsAndEvents();

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
        }
        }
        }
        return cookieValue;
        }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
    }
});

});

Billboard.bindButtonsAndEvents=function(){
    $("#add-post").click(Billboard.showNewPostField);
    $("#clear-post").click(Billboard.clearPost);
//    $("#submit-post").click(Billboard.submitPost);
//    $("#submit-btn-wrap").click(Billboard.additionalSubmitActions);
    $('#myform').submit(Billboard.removeMessage);
}

Billboard.showNewPostField=function(){
    var today=new Date();
    var date=(today.getMonth()+1)+"/"+today.getDate()+"/"+today.getFullYear();
    $("#curr-post-date").text(date);
    $(".post-box-new").removeClass("hidden-content");
    $(".two-buttons").removeClass("hidden-content");
    $("#add-post").addClass("hidden-content");
//    $.get("/mybillboard/board/return_post_date", function(result){
//
//    },"json");
}

Billboard.clearPost=function(){
    $("#subject-field").val("");
    $("#message-field").val("");
}

//Billboard.additionalSubmitActions=function(){
//    $("#subject-field").val("");
//    $("#message-field").val("");
//    $(".post-box-new").addClass("hidden-content");
//    $(".two-buttons").addClass("hidden-content");
//    $("#add-post").removeClass("hidden-content");
//}

//Billboard.submitPost=function(){
//    alert("works!");
//}

Billboard.removeMessage=function(e){
    console.log('form clicked');
    e.preventDefault();
    var form=$(this);
//    var form=$("<form/>");
//    var inp=$("<input/>");
//    inp.attr('name','subject');
//    inp.val(subj);
//    console.log(inp.val());
//    form.append(inp);
//    console.log(form);
    $.post('/mybillboard/board/delete/', form.serialize() ,function(answer){
        console.log(answer['msg']);
        form.remove();

    })
    return false;
}