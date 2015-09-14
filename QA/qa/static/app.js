$(document).ready(function() {
    var root = '/qa';

    var code = false;
    var image = {
        id: null,
        first_index: null,
        second_index: null,
        init: function (id, i1, i2) {
            this.id = id;
            this.first_index = i1;
            this.second_index = i2;
        }
    };

    var Url = {
        'checkUser': root + '/check-user',
        'answer': root + '/answer',
        'next': root + '/next'
    };

    function checkUser() {
        var tmp = $("#user-code-input").val();
        $.ajax(
            Url.checkUser,
            {
                type: "GET",
                data: { 'code': tmp }
            }
        )
            .done(function () {
                code = tmp;
                $("#user-panel").hide();
                getNext();
                $("#qa-panel").show();
            })
            .fail(function () {
                alert("用户不存在");
            });
    }

    function getNext() {
        $.ajax(
            Url.next,
            {
                type: "GET",
                data: { user_code: code }
            }
        )
            .done(function (data) {
                if (data["error_code"]) {
                    alert("您已经完成了所有的题目，谢谢您的配合！");
                    window.location.reload();
                }

                function changeImageWithUrl(container, url) {
                    if (!(container instanceof jQuery)) {
                        container = $(container);
                    }
                    var template = '<img src="%url%" class="center-block"/>';
                    var str = template.replace("%url%", url);
                    container.html(str);
                }

                image.init(data.id, data["first"].index, data["second"].index);
                changeImageWithUrl($("#origin-image"), data.url);
                changeImageWithUrl($("#first-image"), data["first"].url);
                changeImageWithUrl($("#second-image"), data["second"].url);
                $("#remain-notice").html(data["number"] + '/ 120');
            })
            .fail();
    }

    function answer(score) {
        var time = -1;
        var data = {
            user_code: code,
            image_id: image.id,
            index_1: image.first_index,
            index_2: image.second_index,
            score: score,
            time: time
        };
        $.ajax(
            Url.answer,
            {
                type: "POST",
                data: data
            }
        )
            .done(function () {
                getNext();
            })
            .fail(function () {
                alert("Error.");
            });
    }

    (function () {
        $("#user-panel").show();
        $("#qa-panel").hide();

        $("#login-confirm-btn").click(checkUser);
        $(".mark-btn").click(function () {
            answer($(this).data("score"));
        });
    })();

//    Debug function
    $("#debug-btn").click(function () {
        getNext();
    });
});


// settings for CSRF
$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});