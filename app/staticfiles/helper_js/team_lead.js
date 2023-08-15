window.onload = function() {
    team_lead();
  };

function team_lead() {
    
    fetch(`http://127.0.0.1:8000/api/projects/load_users/`)
        .then(response => response.json())
        .then(users => {

        let options = '<option value="">Select a user </option>';
        for (const user of users) {
            if (user.name != '') {
                options += `<option value="${user.id}">${user.name}</option>`;
            }
        }

        userDropdown.innerHTML = options;

        })
        .catch(error => console.error('Error fetching users:', error));
};