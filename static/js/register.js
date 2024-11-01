$(document).ready(function () {
    let csrf_token = $('meta[name="csrf-token"]').attr('content');
    $("#submit").click(function (e) {
        e.preventDefault();

        // Gather form data
        let data = {
            name: $('#name').val(),
            email: $('#email').val(),
            password: $('#password').val()
        };

        console.log(data);

        // AJAX request to send data to the server
        $.ajax({
            url: '/register',        // Replace with your actual endpoint
            type: 'POST',
            data: JSON.stringify(data),  // Send the data as JSON
            contentType: 'application/json',  // Specify the content type as JSON

            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            },

            success: function (response) {
                console.log('response', response);  // Handle the response from the server
                if (response.status == 200) {
                    window.location.href = "/";
                }
            },
            error: function (xhr, status, error) {
                console.error('Error occurred:', error);  // Handle errors
            }
        });
    });
});
