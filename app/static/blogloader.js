$.ajax({
  url      : document.location.protocol + '//ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=10&callback=?&q=' + encodeURIComponent('http://andrewmellor.co.uk/blog/feeds/all.atom.xml'),
  dataType : 'json',
  success  : function (data) {
    if (data.responseData.feed && data.responseData.feed.entries) {
      html = '';
      $.each(data.responseData.feed.entries, function (i, e) {
        if (i === 5) { return false; };
        html = html + "<p><a href="+ e.link + "> " + e.title + "</a></p>";
      });
      document.getElementById("blog").innerHTML = html;
    }
  }
});