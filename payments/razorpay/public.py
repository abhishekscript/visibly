import razorpay

from django.http import HttpResponse

client = razorpay.Client(auth=('rzp_test_wtk3FJewnChgYm', '5X4PxzZefqJ4150GuvVkwHwg'))
client.set_app_details({'title': 'cluster_app', 'version': 'v1.0'})

checkout_page = '''
    <button id="rzp-button1">Pay</button>
    <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
    <script>
    var options = {
        "key": "rzp_test_wtk3FJewnChgYm","amount": "{{amount}}",
        "currency": "{{currency}}",
        "name": "cluster_app",
        "description": "Premium Membership",
        "image": "https://example.com/your_logo",
        "order_id": "order_IluGWxBm9U8zJ8",
        "handler": function (response){
            alert(response.razorpay_payment_id);
            alert(response.razorpay_order_id);
            alert(response.razorpay_signature)
        },
        "prefill": {
            "name": "Gaurav Kumar",
            "email": "gaurav.kumar@example.com",
            "contact": "9999999999"
        },
        "notes": {
            "address": "Razorpay Corporate Office"
        },
        "theme": {
            "color": "#3399cc"
        }
    };
    var rzp1 = new Razorpay(options);
    rzp1.on('payment.failed', function (response){
            alert(response.error.code);
            alert(response.error.description);
            alert(response.error.source);
            alert(response.error.step);
            alert(response.error.reason);
            alert(response.error.metadata.order_id);
            alert(response.error.metadata.payment_id);
    });
    document.getElementById('rzp-button1').onclick = function(e){
        rzp1.open();
        e.preventDefault();
    }
    </script>
'''.replace('\n','')

def create_order(amount, currency, receipt_id):
    data = {'amount': amount, 'currency': currency, 'receipt': receipt_id}
    return client.order.create(data=data)

def get_rendered_data():
    return checkout_page
