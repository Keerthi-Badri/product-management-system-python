$(function () {

    // Load products
    $.get(productListApiUrl, function (response) {

        if (response) {
            var table = '';

            $.each(response, function (index, product) {

                table += `
                    <tr>
                        <td>${product.name}</td>
                        <td>${product.uom_name}</td>
                        <td>${product.price_per_unit}</td>
                    </tr>
                `;
            });

            $("table tbody").empty().html(table);
        }
    });

    // Search box
    $(document).on("keyup", "#productSearch", function () {

        var value = $(this).val().toLowerCase();

        $("table tbody tr").filter(function () {

            $(this).toggle(
                $(this).text().toLowerCase().indexOf(value) > -1
            );

        });
    });

});