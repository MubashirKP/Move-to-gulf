/**
 * Created by mubas on 23-Aug-15.
 */
;(function($){
    "use strict";
    $(function(){
        var movetogulf = window.movetogulf;
        var $form = $("form.post-job-form"),
            Email = $form.find("#email"),
            jobTitle = $form.find ("#jobtitle"),
            jobRegion = $form.find("#jobregion"),
            jobType = $form.find("#jobtype"),
            jobCategory = $form.find("#jobcategory"),
            jobDesc = $form.find(".jobdesc"),
            joburl = $form.find("#url"),
            jobclose = $form.find("#closedate"),
            companyname = $form.find("#companyname"),
            companylogo = $form.find("#logo");

        var region = movetogulf.data.locations;
        $.each(region,function(){
            jobRegion.append($('<option>',{
                value: this.id,
                text: this.title
                }));

        });
        var type = movetogulf.data.types;
        $.each(type,function(){
           jobType.append($('<option>',{
               value:this.id,
               text:this.type
           }));
        });

        var category = movetogulf.data.category;
        $.each(category,function(){
           jobCategory.append($('<option>',{
               value:this.id,
               text:this.name
           }));
        });

    });
}(window.jQuery));

