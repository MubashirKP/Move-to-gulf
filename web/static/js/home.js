/**
 * Created by mubas on 26-Aug-15.
 */
;(function($){
    "use strict";
    $(function() {
        var data = window.movetogulf.postdata,
        pagination_data = [];

        var $all = $("#all");

        $.each(data,function() {
            var tmpl = '<div class="recent-job-list-home"><div class="job-list-logo col-md-1 ">' +
                    '<img src=\'{%static "images/upload/dummy-job-open-1.png"%}\' class="img-responsive" alt="dummy-joblist"/>' +
                    '</div><div class="col-md-6 job-list-desc"><h6>' + this.title + '</h6><p>' + this.description + '</p></div>' +
                    '<div class="col-md-5 full"> <div class="row"><div class="job-list-location col-md-7 "><h6>' +
                    '<i class="fa fa-map-marker"></i>' + this.location + '</h6></div><div class="job-list-type col-md-5 ">' +
                    '<h6><i class="fa fa-user"></i>' + this.type + '</h6></div></div></div><div class="clearfix"></div></div>';

                $all.append(tmpl);
            });

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
