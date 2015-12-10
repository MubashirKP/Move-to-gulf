/**
 * Created by mubas on 26-Aug-15.
 */
;(function($){
    "use strict";
    $(function() {
        var data = window.movetogulf.postdata,
        pagination_data = [];


        var region = window.movetogulf.autofill.locations;
        $.each(region,function(){
            $("select.input-location").append($('<option>',{
                value: this.id,
                text: this.title
                }));

        });

        var category = window.movetogulf.autofill.category;
        $.each(category,function(){
           $("select.input-job").append($('<option>',{
               value:this.id,
               text:this.name
           }));
        });
    });
    $("button.btn-default").on("click",function(){

       var json={"category":$("select.input-job").val(),
                 "location":$("select.input-location").val(),
                  'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()};
        $.ajax({
            url: "/search/",
            type: "POST",
            data: json,
            success: function(response) {
                $("body").html(response);
            },
            error: function(response) {
                console.log("failed!");
            }
        });
    });
}(window.jQuery));
