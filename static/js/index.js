$(document).ready(function() {
    $.ajax({
        url: '/get_breaking_news',
        type: 'GET',
        contentType: 'application/json',
        success: function(data) {
            console.log(data);
            data.top_news.forEach((article) => {
                // <img src="https://via.placeholder.com/350x200" class="card-img-top" alt="Trending 1"></img>
                const imageUrl = article.urlToImage;
                $('#trending').append(` <div class="col-md-4 mb-4">
                <div class="card">
                    
                    <img src="${imageUrl}" class="card-img-top" alt="Trending 1">
                    <div class="card-body">
                        <h5 class="card-title">${article.title}</h5>
                        <p class="card-text">${article.description}</p>
                        <a href="${article.url}" class="btn btn-primary">Read more</a>
                    </div>
                </div>
            </div>`)

            })
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    })
    $.ajax({
        url: '/get_articals',
        type: 'GET',
        contentType: 'application/json',
        success: function(data) {
            console.log(data);
            data.top_news.forEach((article) => {
                // <img src="https://via.placeholder.com/350x200" class="card-img-top" alt="Trending 1"></img>
                const imageUrl = article.urlToImage;
                $('#latest').append(` <div class="col-md-4 mb-4">
                <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="${imageUrl}" class="card-img-top" alt="Trending 1">
                    <div class="card-body">
                        <h5 class="card-title">${article.title}</h5>
                        <p class="card-text">${article.description}</p>
                        <a href="${article.url}" class="btn btn-primary">Read more</a>
                    </div>
                </div>
            </div>
            `)

            })
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    })
})