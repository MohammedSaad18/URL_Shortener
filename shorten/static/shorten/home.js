const alertBox = document.getElementById("alert-box");
const form = document.getElementById("p-form");
const long_url = document.getElementById("id_url");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const url = "";

const display_short_url = (short_url) => {
  console.log(short_url);
  alertBox.innerHTML = `<div class="alert alert-success" role="alert">${short_url}</div>`;
};

console.log(form.elements)

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const fd = new FormData();
  fd.append("csrfmiddlewaretoken", csrf[0].value);
  fd.append("url", long_url.value);

  $.ajax({
    type: "POST",
    url: url,
    data: fd,
    success: function (response) {
      console.log(response);
      display_short_url(response.shorturl);
    },
    error: function (error) {
      console.log(error);
      display_short_url(error);
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});
