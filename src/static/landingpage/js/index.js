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
							 $('body').append(` <div class="alert alert-success alert-dismissible fade" role="alert" id="buttonAlert">
											          <strong>Success!</strong> Message was sent successfully.
											          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
											            <span aria-hidden="true">&times;</span>
											          </button>
											   				</div>`);
							 $('alert-success').alert();
							}
							else {
							 $("#contactModal").modal('hide'); // remove contactModal
 							 var node = document.createElement("div");
 							 node.classList.add("alert");
 							 node.classList.add("alert-danger");
 							 node.textContent = "Message sent unsuccessfully! Bot detected. If you're human, please try again later.";
 							 $(node).alert();
							};
						};
					request.send(new FormData(this));
	      });
});
