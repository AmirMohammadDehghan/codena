$(document).ready(function () {

    $('.addToCartBtn').click(function (e) {
        alert();
        e.preventDefault();
        const course_id = $(this).closest('.course_data').find('.cors_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: "POST",
            url: "/add-to-cartlist",
            data: {
                'course_id':course_id,
                csrfmiddlewaretoken:token


            },
            success: function (response) {
            console.log(response)
            alertify.success(response.status)
            }
        });
    });
    $('.delete-cartlist-item').click(function (e) {
    alert();
    e.preventDefault();
    var course_id = $(this).closest('.course_data').find('.cors_id').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();


    $.ajax({
        type: "POST",
        url: "/delete-cartlist-item",
        data: {
            'course_id':course_id,
            csrfmiddlewaretoken:token

           },

        success: function (response) {
            alertify.success(response.status);
            location.reload()
        }
    });

});
});

function Faze_Id (id) {
    document.getElementById('faz_id').value = id;
}

$(document).ready(function () {

    $('.addFazeToCartBtn').click(function (e) {
        alert();
        e.preventDefault();
        const faze_id = $(this).closest('.faze_data').find('.faz_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: "POST",
            url: "/add-faze-to-cartlist",
            data: {
                'faze_id':faze_id,
                csrfmiddlewaretoken:token


            },
            success: function (response) {
            console.log(response)
            alertify.success(response.status)
            }
        });
    });
    $('.delete-faze-cartlist-item').click(function (e) {
    alert();
    e.preventDefault();
    var faze_id = $(this).attr('id');
    var token = $('input[name=csrfmiddlewaretoken]').val();
    console.log(faze_id)

    $.ajax({
        type: "POST",
        url: "/delete-faze-cartlist-item",
        data: {
            'faze_id':faze_id,
            csrfmiddlewaretoken:token

           },

        success: function (response) {
            alertify.success(response.status);
            location.reload()
        }
    });

});
});



function courseDiscountInputCart(course_id){
    document.getElementById('go-pay-'+course_id).href = '../ATM/request/course/'+ course_id +'/'+ document.getElementById('cors-discount-code-'+course_id).value
    document.getElementById('cors-discount-code-'+course_id).classList.add("bordering-green")

}

function fazeDiscountInputCart(faze_id){
    document.getElementById('go-faze-pay-'+faze_id).href = '../ATM/request/faze/'+ faze_id +'/'+ document.getElementById('faz-discount-code-'+faze_id).value
    document.getElementById('faz-discount-code-'+faze_id).classList.add("bordering-green")

}