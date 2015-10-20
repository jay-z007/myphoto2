        $(".menu-icon").hover(function(){
            $(".wrapper").addClass("open-half");
        });
        $(".menu-main").mouseleave(function(){
            $(".wrapper").removeClass("open-half open-full ");
        });
        $(".menu-content").hover(function(){
            $(".wrapper").removeClass("open-half");
            $(".wrapper").addClass("open-full");
        });
    
    