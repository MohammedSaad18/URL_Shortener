const alertBox = document.getElementById("alert-box");
const form = document.getElementById("p-form");
const long_url = document.getElementById("id_url");
const short_code = document.getElementById("id_shortcode");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const url = "";

const display_short_url = (short_url) => {
  console.log(short_url);
  alertBox.innerHTML = `<div class="alert alert-success" role="alert">${short_url}</div>`;
};

const display_error = (msg) => {
  alertBox.innerHTML = `<div class="alert alert-danger" role="alert">${msg}</div>`;
};

console.log(form.elements)

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const fd = new FormData();
  fd.append("csrfmiddlewaretoken", csrf[0].value);
  fd.append("url", long_url.value);
  fd.append("shortcode", short_code.value)
  $.ajax({
    type: "POST",
    url: url,
    data: fd,
    success: function (response) {
      display_short_url(response.shorturl);
    },
    error: function (error) {
      display_error(error.responseText);
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});
