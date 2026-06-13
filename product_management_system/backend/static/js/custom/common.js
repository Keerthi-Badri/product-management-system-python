// Define your api here
var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';


function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (msg) {
            console.log("SUCCESS:", msg);
            window.location.reload();
        },
        error: function (err) {
            console.log("ERROR:", err);
        }
    });
}


/* =========================
   CALCULATE TOTAL ORDER
========================= */
function calculateValue() {
    var total = 0;

    $(".product-item").each(function(index) {
        var qty = parseFloat($(this).find('.product-qty').val()) || 0;
        var price = parseFloat($(this).find('#product_price').val()) || 0;

        price = price * qty;

        $(this).find('#item_total').val(price.toFixed(2));
        total += price;
    });

    $("#product_grand_total").val(total.toFixed(2));
}


/* =========================
   FIXED ORDER PARSER
========================= */
function orderParser(order) {
    return {
        id: order.order_id,
        date: order.datetime,
        orderNo: order.order_id,
        customerName: order.customer_name,
        cost: order.total
    };
}


/* =========================
   FIXED PRODUCT PARSER
========================= */
function productParser(product) {
    return {
        id: product.id,
        name: product.name,
        unit: product.uom_name || product.unit,
        price: product.price
    };
}


/* =========================
   PRODUCT DROPDOWN PARSER
========================= */
function productDropParser(product) {
    return {
        id: product.id,
        name: product.title
    };
}


/* =========================
   TOOLTIP (optional)
========================= */
// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// });

function logout() {
    localStorage.removeItem("user");
    window.location.href = "login.html";
}