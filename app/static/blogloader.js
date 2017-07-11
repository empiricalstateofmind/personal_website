$.get('https://andrewmellor.co.uk/blog/feeds/all.atom.xml', function (data) {
    html = '';
    $(data).find("entry").each(function (i) { // or "item" or whatever suits your feed
        if (i === 5) { return false; };
        var el = $(this);
        html = html + "<p><a href="+ el.find("link").attr("href") + "> " + el.find("title").text() + "</a></p>";
        console.log("------------------------");
        console.log("title      : " + el.find("title").text());
    });
    document.getElementById("blog").innerHTML = html;
});

// GOOGLE API DEPRECIATED
// $.ajax({
//   url      : document.location.protocol + '//ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=10&callback=?&q=' + encodeURIComponent('http://andrewmellor.co.uk/blog/feeds/all.atom.xml'),
//   dataType : 'json',
//   success  : function (data) {
//     if (data.responseData.feed && data.responseData.feed.entries) {
//       html = '';
//       $.each(data.responseData.feed.entries, function (i, e) {
//         if (i === 5) { return false; };
//         html = html + "<p><a href="+ e.link + "> " + e.title + "</a></p>";
//       });
//       document.getElementById("blog").innerHTML = html;
//     }
//   }
// });
