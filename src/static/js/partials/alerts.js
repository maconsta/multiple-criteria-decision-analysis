"use strict";

$(document).ready(function () {
    const Help = Swal.mixin({
        allowOutsideClick: false,
        confirmButtonColor: "#597E52",
        confirmButtonText: 'Ok',
        icon: 'question',

    });

    $(".help-icon").on("click", function () {
        const id = $(this).attr("data-for");

        Help.fire({
            template: "#" + id
        })
    });
});