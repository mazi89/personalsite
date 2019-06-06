// form submission handling
document.addEventListener('DOMContentLoaded', () => {
	var form = document.getElementById("contactForm");

	form.addEventListener('submit', function(event){
					event.preventDefault();
					var request = new XMLHttpRequest();
					request.open("POST", 'https://abdinasirnoor.com/contacted', true);
						request.onload = function() {
							if ((this.status === 200)) {
							 $("#contactModal").modal('hide'); // remove contactModal
							 var node = document.createElement("div");
							 node.classList.add("alert");
							 node.classList.add("alert-success");
							 node.textContent = "Message sent successfully!";
							 $(node).alert();
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
