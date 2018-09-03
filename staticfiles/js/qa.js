$(function () {
    function getCookie(name) {
        // Function to get any cookie available in the session.
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
    };

    function csrfSafeMethod(method) {
        // These HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    var page_title = $(document).attr("title");
    // This sets up every ajax call with proper headers.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#publish").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form").submit();
    });

    $("#publish2").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form-2").submit();
    });

    $("#publish3").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form-3").submit();
    });

    $("#publish4").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form-4").submit();
    });

    $("#publish5").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form-5").submit();
    });

    $("#publish6").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form-6").submit();
    });

    $("#publish7").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form-7").submit();
    });

    $("#publish8").click(function () {
        // function to operate the Publish button in the question form, marking
        // the question status as published.
        $("input[name='status']").val("O");
        $("#question-form-8").submit();
    });

    $("#draft").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form").submit();
    });

    $("#draft2").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form-2").submit();
    });

    $("#draft3").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form-3").submit();
    });

    $("#draft4").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form-4").submit();
    });

    $("#draft5").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form-5").submit();
    });

    $("#draft6").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form-6").submit();
    });

    $("#draft7").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form-7").submit();
    });

    $("#draft8").click(function () {
        // Function to operate the Draft button in the question form, marking
        // the question status as draft.
        $("input[name='status']").val("D");
        $("#question-form-8").submit();
    });

    $(".question-vote").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes").text(data.votes);
            }
        });
    });

    $(".question-vote2").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote-2/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes2").text(data.votes);
            }
        });
    });

    $(".question-vote3").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote-3/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes3").text(data.votes);
            }
        });
    });

    $(".question-vote4").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote-4/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes4").text(data.votes);
            }
        });
    });

    $(".question-vote5").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote-5/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes5").text(data.votes);
            }
        });
    });

    $(".question-vote6").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote-6/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes6").text(data.votes);
            }
        });
    });

    $(".question-vote7").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote-7/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes7").text(data.votes);
            }
        });
    });

    $(".question-vote8").click(function () {
        // Vote on a question.
        var span = $(this);
        var question = $(this).closest(".question").attr("question-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/question/vote-8/',
            data: {
              'question': question,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#questionVotes8").text(data.votes);
            }
        });
    });

    $(".answer-vote").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes").text(data.votes);
            }
        });
    });

    $(".answer-vote2").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote-2/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes2").text(data.votes);
            }
        });
    });

    $(".answer-vote3").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote-3/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes3").text(data.votes);
            }
        });
    });

    $(".answer-vote4").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote-4/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes4").text(data.votes);
            }
        });
    });

    $(".answer-vote5").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote-5/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes5").text(data.votes);
            }
        });
    });

    $(".answer-vote6").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote-6/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes6").text(data.votes);
            }
        });
    });

    $(".answer-vote7").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote-7/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes7").text(data.votes);
            }
        });
    });

    $(".answer-vote8").click(function () {
        // Vote on an answer.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        vote = null;
        if ($(this).hasClass("up-vote")) {
            vote = "U";
        } else {
            vote = "D";
        }
        $.ajax({
            url: '/qa/answer/vote-8/',
            data: {
              'answer': answer,
              'value': vote
            },
            type: 'post',
            cache: false,
            success: function (data) {
              $('.vote', span).removeClass('voted');
              if (vote === "U") {
                $(span).addClass('voted');
              }
              $("#answerVotes8").text(data.votes);
            }
        });
    });

    $("#acceptAnswer").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer").removeClass("accepted");
                $("#acceptAnswer").prop("title", "Click to accept the answer");
                $("#acceptAnswer").addClass("accepted");
                $("#acceptAnswer").prop("title", "Click to unaccept the answer");
            }
        });
    });

    $("#acceptAnswer2").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer-2/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer2").removeClass("accepted");
                $("#acceptAnswer2").prop("title", "Click to accept the answer");
                $("#acceptAnswer2").addClass("accepted");
                $("#acceptAnswer2").prop("title", "Click to unaccept the answer");
            }
        });
    });

    $("#acceptAnswer3").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer-3/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer3").removeClass("accepted");
                $("#acceptAnswer3").prop("title", "Click to accept the answer");
                $("#acceptAnswer3").addClass("accepted");
                $("#acceptAnswer3").prop("title", "Click to unaccept the answer");
            }
        });
    });

    $("#acceptAnswer4").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer-4/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer4").removeClass("accepted");
                $("#acceptAnswer4").prop("title", "Click to accept the answer");
                $("#acceptAnswer4").addClass("accepted");
                $("#acceptAnswer4").prop("title", "Click to unaccept the answer");
            }
        });
    });

    $("#acceptAnswer5").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer-5/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer5").removeClass("accepted");
                $("#acceptAnswer5").prop("title", "Click to accept the answer");
                $("#acceptAnswer5").addClass("accepted");
                $("#acceptAnswer5").prop("title", "Click to unaccept the answer");
            }
        });
    });

    $("#acceptAnswer6").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer-6/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer6").removeClass("accepted");
                $("#acceptAnswer6").prop("title", "Click to accept the answer");
                $("#acceptAnswer6").addClass("accepted");
                $("#acceptAnswer6").prop("title", "Click to unaccept the answer");
            }
        });
    });

    $("#acceptAnswer7").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer-7/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer7").removeClass("accepted");
                $("#acceptAnswer7").prop("title", "Click to accept the answer");
                $("#acceptAnswer7").addClass("accepted");
                $("#acceptAnswer7").prop("title", "Click to unaccept the answer");
            }
        });
    });

    $("#acceptAnswer8").click(function () {
        // Mark an answer as accepted.
        var span = $(this);
        var answer = $(this).closest(".answer").attr("answer-id");
        $.ajax({
            url: '/qa/accept-answer-8/',
            data: {
                'answer': answer
            },
            type: 'post',
            cache: false,
            success: function (data) {
                $("#acceptAnswer8").removeClass("accepted");
                $("#acceptAnswer8").prop("title", "Click to accept the answer");
                $("#acceptAnswer8").addClass("accepted");
                $("#acceptAnswer8").prop("title", "Click to unaccept the answer");
            }
        });
    });
});
