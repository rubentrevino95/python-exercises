var count = 0;

function execute() {
    var size = false;

    var sizePref = ["Medium", "Large", "XLarge", "Small"];

    var searchText = "shirt";
    var color = "black";

    count++;
    if(document.title != "Supreme") {
        var sel = document.getElementById("size");
        var opTags = document.getElementsByTagName("option");

    if (size) {
        for(var i = 0; i < sizePref.length; i++) {
            for(var x = 0; x < opTags.length; x++) {
                if(sizePref[i] === opTags[x].textContent) {
                sel.value = opTags[x].value;
                break;
                }
            }
            break;
        }
    }

        setTimeout(function(){
            document.querySelector('#details form input[type="submit').click();
        }, 200);

        setTimeout(function(){
            window.location.href = 'https://supremenewyork.com/checkout';
          }, 450);

        window.setInterval(function () {
            setTimeout(function(){
                document.querySelector('#cart-footer .checkout').click();
            }, 370);
            setTimeout(function() {
                document.querySelector('#cart-footer .checkout').click();
            }, 500);
        }, 500);

    }
    else {
        var aTags = document.getElementsByTagName("a");
        var found;
        var theLink;
        var theColorLink;
        var items = [];

        for (var i = 0; i < aTags.length; i++) {
            if (aTags[i].textContent.toLowerCase().includes(color)) {
                if(items.indexOf(aTags.indexOf(aTags[i].getAttribute("href")) > -1)) {
                    found = aTags[i];
                }
            }
        }

        if(found != null) {
            console.log("execute")
            window.location.href = found.getAttribute("href");
        }
    }
}
execute();

window.setInterval(function () {
    setTimeout(function () {
        if(count < 3)
        execute();
    }, 370);
}, 200);
