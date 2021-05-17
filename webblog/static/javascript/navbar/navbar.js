window.onclick = function (event) {
	// alert(event.target.id);
	event.stopPropagation();
	var signup_form = document.getElementById("signup-dialog");
	var login_form = document.getElementById("login-dialog");
	var account_form = document.getElementById("my_account");
	var sort_form = document.getElementById("my_sort");
	var go_home = document.getElementById("gohome");

	if (event.target.id == "gohome") {
		location.replace("/");
	}

	if (
		event.target.id == "signup-btn" ||
		event.target.id == "dropdown-signup"
	) {
		signup_form.style.display = "block";
		login_form.style.display = "none";
		account_form.style.display = "none";
	} else if (
		event.target.id == "signin-btn" ||
		event.target.id == "dropdown-signin"
	) {
		login_form.style.display = "block";
		signup_form.style.display = "none";
		account_form.style.display = "none";
	} else if (
		event.target.id == "login-dialog" ||
		event.target.id == "signup-dialog"
	) {
		signup_form.style.display = "none";
		login_form.style.display = "none";
		account_form.style.display = "none";
	} else if (event.target.id == "to-signup") {
		signup_form.style.display = "block";
		login_form.style.display = "none";
		account_form.style.display = "none";
	} else if (event.target.id == "to-login") {
		signup_form.style.display = "none";
		login_form.style.display = "block";
		account_form.style.display = "none";
	} else if (event.target.id == "btn-account-id") {
		account_form.style.display = "block";
	} else if (event.target.id == "sort-btn-id") {
		sort_form.style.display = "block";
	} else {
		account_form.style.display = "none";
		sort_form.style.display = "none";
	}
};

