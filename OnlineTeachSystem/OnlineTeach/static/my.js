/**
 * Created with JetBrains WebStorm.
 * User: pwanwu
 * Date: 18/09/2013
 * Time: 17:41
 * To change this template use File | Settings | File Templates.
 */

var questions = [{
    Question_description: "_____ of us felt very tired but quite happy after _____ sports meeting.\r\nA. Everyone, a two days\u2019   B. Every one, the two days\r\nC. Every one, the two-day   D. None, a two-day" ,
    Question_default_answer: "A",
    Question_categery:"python",
    Question_type:"1",
    Question_categery: "python",
    Question_feature: "easy|fifth" ,
    Question_id: "english1",
},
{
    Question_description: "_____ of us felt very tired but quite happy after _____ sports meeting.\r\nA. Everyone, a two days\u2019   B. Every one, the two da\
ys\r\nC. Every one, the two-day   D. None, a two-day" ,
    Question_default_answer: "A",
    Question_categery:"python",
    Question_type:"1",
    Question_categery: "python",
    Question_feature: "easy|fifth" ,
    Question_id: "english1",


},
];

var currentQuestion = 0;
var correctAnswers = 0;
var quizOver = false;

$(document).ready(function () {

    // Display the first question
    displayCurrentQuestion();
    $(this).find(".quizMessage").hide();

    // On clicking next, display the next question
    $(this).find(".nextButton").on("click", function () {
        if (!quizOver) {

            value = $(input[type='text']).val();

            if (value == undefined) {
                $(document).find(".quizMessage").text("Please select an answer");
                $(document).find(".quizMessage").show();
            } else {
                // TODO: Remove any message -> not sure if this is efficient to call this each time....
                $(document).find(".quizMessage").hide();

                if (value == questions[currentQuestion].Question_default_answer) {
                    correctAnswers++;
                }

                currentQuestion++; // Since we have already displayed the first question on DOM ready
                if (currentQuestion < questions.length) {
                    displayCurrentQuestion();
                } else {
                    displayScore();
                    //                    $(document).find(".nextButton").toggle();
                    //                    $(document).find(".playAgainButton").toggle();
                    // Change the text in the next button to ask if user wants to play again
                    $(document).find(".nextButton").text("Play Again?");
                    quizOver = true;
                }
            }
        } else { // quiz is over and clicked the next button (which now displays 'Play Again?'
            quizOver = false;
            $(document).find(".nextButton").text("Next Question");
            resetQuiz();
            displayCurrentQuestion();
            hideScore();
        }
    });

});

// This displays the current question AND the choices
function displayCurrentQuestion() {

    console.log("In display current Question");

    var question = questions[currentQuestion].Question_description;
    var questionClass = $(document).find(".quizContainer > .Question_description ");
    var choiceList ;

    // Set the questionClass text to the current question
    $(questionClass).text(question);

    // Remove all current <li> elements (if any)

  $('.type="text"').val().appendTo(choiceList);
}

function resetQuiz() {
    currentQuestion = 0;
    correctAnswers = 0;
    hideScore();
}

function displayScore() {
    $(document).find(".quizContainer > .result").text("You scored: " + Question_default_answer + " out of: " + questions.length);
    $(document).find(".quizContainer > .result").show();
}

function hideScore() {
    $(document).find(".result").hide();
}
