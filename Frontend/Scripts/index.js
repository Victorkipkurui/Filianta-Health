function openLoginSignupPage() {
  window.open("login.html", "_blank");
}
function handleLogin() {
  openLoginSignupPage();
}
document.addEventListener("DOMContentLoaded", function() {
  const loginButton = document.getElementById("js-button");
  if (loginButton) {
      loginButton.addEventListener("click", handleLogin);
  }
});
