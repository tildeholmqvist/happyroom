$(document).ready(function(){
    $('.delete-btn').click(function(e){
        e.preventDefault();
        var productId = $(this).data('product-id');
        var serviceId = $(this).data('service-id');

        if (productId) {
            var deleteUrl = '/delete/' + productId + '/';
        } else if (serviceId) {
            var deleteUrl = '/delete/' + serviceId + '/';
        }

        $('#deleteModal #deleteConfirm').attr('href', deleteUrl);
        $('#deleteModal').modal('show');
    });
});