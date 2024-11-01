$(document).ready(function() {
    $.ajax({
        url: '/get_news',
        type: 'GET',
        contentType: 'application/json',
        success: function(data) {
            data.news_data.articles.forEach(article => {
                const imageUrl = article.urlToImage;
                
                // Only create and append the card if the imageUrl exists
                if (imageUrl) {
                    $('#news-container').append(`
                        <div class="col-md-6 col-lg-4 mb-4">
                            <div class="card">
                                <img src="${imageUrl}" class="card-img-top" alt="Article Image">
                                <div class="card-body">
                                    <h5 class="card-title">${article.title}</h5>
                                    <p class="card-text">${article.description || "No description available"}</p>
                                    <p class="author"><b>Author:</b> ${article.author || "Unknown"}</p>
                                    <p class="date"><b>Date:</b> ${new Date(article.publishedAt).toLocaleDateString() || "Not available"}</p>
                                    <a href="${article.url}" target="_blank" class="btn btn-primary">Read More</a>
                                </div>
                            </div>
                        </div>
                    `);
                }
            });
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
});
