// form submission handling
document.addEventListener('DOMContentLoaded', () => {
	var form = document.getElementById("contactForm");

	form.addEventListener('submit', function(event){
					event.preventDefault();
					var request = new XMLHttpRequest();
					request.open("POST", 'https://abdinasirnoor.com/contacted/', true);
						request.onload = function() {
							if ((this.status === 200)) {
							 $("#contactModal").modal('hide'); // remove contactModal
							 $("#successModal").modal('show'); //success message
							 $(".btn-default").replaceWith('<p class="h2">Message has been sent <div class="far fa-thumbs-up"></p>');

							}
							else {
							 $("#contactModal").modal('hide'); // remove contactModal
							$("#successModal").removeClass('alert-success');
							$("#successModal").addClass('alert-danger');
							$(".bodyMessage").replaceWith('<p class="h1 bodyMessage"><strong>Message Was not sent!</strong> bot detected. If you\re human please try again later!</p>');
							$(".btn-default").replaceWith('<p class="h2">Message has was not sent!<i class="far fa-thumbs-down fa-3x"></i></p>');
							};
						};
					request.send(new FormData(this));
	      });
});
