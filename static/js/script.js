$(document).ready(function () {

    // Submit the query when Select input changes
    $('#category-selector').change(function (){
        $('#filter').submit();
    });

    // Update Select box with the current Category
    var category_selected = $('#category-selector').attr('data-selected');
    $("#category-selector").val(category_selected);
});
