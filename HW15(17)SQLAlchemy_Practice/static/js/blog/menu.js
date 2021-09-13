$(document).ready(function () {
    $.ajax({
        method: "GET",
        url: "/api/menu-items",
        success: function (data) {
            if (data.success) {
                for (let el of data.items) {
                    let menuItemHtml = "<li class=\"nav-item\">\n" +
                        "                    <a class=\"nav-link active\" aria-current=\"page\" href=\""+ el.link +"\">" + el.name + "</a>\n" +
                        "                </li>"
                    $("#menuItemsList").append(menuItemHtml);
                }
            }
        }
    });
});