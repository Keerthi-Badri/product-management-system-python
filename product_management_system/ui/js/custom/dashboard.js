$(function () {
    console.log("Dashboard loaded");

    $.get(orderListApiUrl)
        .done(function (response) {
            console.log("API RESPONSE:", response);

            if (!response || response.length === 0) {
                console.log("No orders found");
                return;
            }

            var table = '';
            var totalCost = 0;

            $.each(response, function (index, order) {
                totalCost += parseFloat(order.total);

                table += '<tr>' +
                    '<td>' + order.datetime + '</td>' +
                    '<td>' + order.order_id + '</td>' +
                    '<td>' + order.customer_name + '</td>' +
                    '<td>' + parseFloat(order.total).toFixed(2) + ' Rs</td>' +
                    '</tr>';
            });

            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>' +
                totalCost.toFixed(2) + ' Rs</b></td></tr>';

            $("table tbody").html(table);
        })
        .fail(function (err) {
            console.log("API FAILED:", err);
        });
});