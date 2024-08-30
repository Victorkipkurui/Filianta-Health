document.querySelector('.js-appointment').addEventListener('submit', function(event) {
  event.preventDefault();

  let formData = new FormData(this);
  let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  fetch('/bookings/book/', {
      method: 'POST',
      body: formData,
      headers: {
          'X-CSRFToken': csrfToken
      }
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          // Handle success (e.g., show a success message, update the appointment list)
      } else {
          // Handle errors
      }
  });
});
