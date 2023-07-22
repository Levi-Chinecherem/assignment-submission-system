$(document).ready(function() {
    // AJAX for posting a new comment
    $('#comment-form').on('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(this);
  
      $.ajax({
        url: $(this).data('discussion-id'),
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          $('#comment-list').append(response.comment_html);
          $('#comment-form')[0].reset();
        }
      });
    });
  
    // AJAX for posting a new reply
    $(document).on('submit', '.reply-form', function(event) {
      event.preventDefault();
      const formData = new FormData(this);
      const commentId = $(this).data('comment-id');
  
      $.ajax({
        url: '/post_reply/' + commentId + '/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          $('.reply-list[data-comment-id="' + commentId + '"]').append(response.reply_html);
          $('.reply-form[data-comment-id="' + commentId + '"]')[0].reset();
        }
      });
    });
  });
  