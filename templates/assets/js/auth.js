'use strict';


const loginBtn = document.getElementById('login_btn_id');
const loginErrorBlock = document.getElementById('login_error_block_id');

loginBtn.onclick = (event) => {
  event.preventDefault();

  const email = document.getElementById('id_email').value;
  const password = document.getElementById('id_password').value;

  const data = {
    email: email,
    password: password,
  }

  fetch(loginUrl, {
    method: 'POST',
    headers: {
      'Accept': 'application/json, text/plain, */*',
      'Content-type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify(data)
  })
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  })
  .then(responseJSON => {
    document.location.href = responseJSON['success_url'];
  })
  .catch(error => {
    loginErrorBlock.style.display = 'block';
  })
}
