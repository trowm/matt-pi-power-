document.addEventListener(
  "DOMContentLoaded",
  function () {

    getStatus();

    switch1.addEventListener(
      "click",
      function () {
        switchClicked("1");
      },
      false
    );
  },
  false
);

function switchClicked(button) {
  fetch(`/switch?socket=${button}`)
    .then(function (response) {
      return response.text();
    })
    .then(function (data) {
      getStatus();
    })
    .catch((error) => {
      // Handle error
    });
}

function getStatus() {
  fetch(`/status`)
    .then(function (response) {
      return response.text();
    })
    .then(function (data) {
      var switch1 = document.getElementById("switch1");
      switch1.setAttribute("data-id", data);
    })
    .catch((error) => {
      console.log(error, "error");
    });
}