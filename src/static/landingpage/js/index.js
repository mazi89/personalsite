// form submission handling
document.addEventListener('DOMContentLoaded', () => {
	var form = document.getElementById("contactForm");

	form.addEventListener('submit', function(event){
					event.preventDefault();
					var request = new XMLHttpRequest();
					request.open("POST", 'https://abdinasirnoor.com/contacted', true);
						request.onload = function() {
							if ((this.status === 200)) {
								console.log(this.response);
							}
							else {
								console.log(this.response);
							};
						};
					request.send(new FormData(this));
	      });
});
