$(document).on("keypress", "textarea", function (e) {
    if (e.which == 13 && $('textarea').val().trim() != "") {
        rawInput = $(this).val().replace(/</g, "&lt;").replace(/>/g, "&gt;");
        inputVal = "<li class='m-2 p-2 rounded chat-grey'>" + rawInput + "</li>";
        $("ol").append(inputVal);
        $('textarea').val('');
        e.preventDefault();
    }
});

$(document).ready(function () {
    $('.chat-body').hide();
    $('.chat-box').css({"bottom":"55px"});
    $("#min").click(function () {
        $('.chat-box').css({"bottom":"55px"});
        $('.chat-body').hide();
        $(this).hide();
        $('#max').show();
    });
    $("#max").click(function () {
        $('.chat-box').css({"bottom":"100px"});
        $('.chat-body').show();
        $(this).hide();
        $('#min').show();
    });
});

$(document).ready(function () {
    var colorList = [
        { "id": 0, "text": "Red", "bcgColor": "#F44336", "fontColor": "#FAFAFA" },
        { "id": 1, "text": "Pink", "bcgColor": "#E91E63", "fontColor": "#FAFAFA" },
        { "id": 2, "text": "Purple", "bcgColor": "#9C27B0", "fontColor": "#FAFAFA" },
        { "id": 3, "text": "Indigo", "bcgColor": "#3F51B5", "fontColor": "#FAFAFA" },
        { "id": 4, "text": "Blue", "bcgColor": "#2196F3", "fontColor": "#212121" },
        { "id": 5, "text": "Teal", "bcgColor": "#009688", "fontColor": "#212121" },
        { "id": 6, "text": "Lime", "bcgColor": "#CDDC39", "fontColor": "#212121" },
        { "id": 7, "text": "Yellow", "bcgColor": "#FFEB3B", "fontColor": "#212121" },
        { "id": 8, "text": "Amber", "bcgColor": "#FFC107", "fontColor": "#212121" },
        { "id": 9, "text": "Orange", "bcgColor": "#FF5722", "fontColor": "#212121" },
        { "id": 10, "text": "Brown", "bcgColor": "#795548", "fontColor": "#FAFAFA" }
    ];

    var colorSelected = { "text": "Indigo", "bcgColor": "#3F51B5", "fontColor": "#FAFAFA" }

    localStorage.colorList = JSON.stringify(colorList);
    localStorage.colorSelected = JSON.stringify(colorSelected);

});

$(document).ready(function () {
    $('.my-select').select2({
        data: JSON.parse(localStorage.colorList)
    });
});

$('.apply-button').on('click', function () { 
    var selectValue = $(".my-select").val();
    if(selectValue >= 0 && selectValue <= 10){
        colorList = JSON.parse(localStorage.colorList);
        colorSelected = colorList[selectValue];
        $('body').css('background', colorSelected['bcgColor']);
        localStorage.colorSelected = JSON.stringify(colorList[selectValue]);
    }
})