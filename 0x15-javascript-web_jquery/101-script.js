/*
$("DIV#add_item").bind("click", function() {
    $("UL.my_list").append("<li>Item</li>");
})

$("DIV#remove_item").bind("click", function() {
    $("UL.my_list").remove("li");
});

$("DIV#clear_list").bind("click", function() {
    $("UL.my_list").append("<li>Item_new</li>");;
});
*/

let count = 0;
$(function () {
    $("DIV#add_item").click(function() {
        $("UL.my_list").append("<li>Item</li>");
        count++;
    });

    $("DIV#remove_item").bind("click", function() {
        $("UL.my_list li").last().remove();
    });
    
    $("DIV#clear_list").bind("click", function() {
        $("UL.my_list").empty();
    });
});
