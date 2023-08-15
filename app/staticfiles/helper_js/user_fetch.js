window.onload = function() {
    user_fetch();
    team_lead();
  };

function user_fetch() {
        
    fetch(`../load_users/`)
        
        .then(response => response.json())
        .then(users => {

        let options = '';
        for (const user of users) {
            if (user.name != '') {
                // options += `<option value="${user.id}">${user.name}</option>`;
                options += `<li draggable="true" value="${user.id}">${user.name}</li>`;
            }
        }

        userList.innerHTML = options;

        })
        .catch(error => console.error('Error fetching users:', error));
      
    const lists = document.querySelectorAll('.list');
    lists.forEach(list => {
    list.addEventListener('dragstart', handleDragStart);
    list.addEventListener('dragover', handleDragOver);
    list.addEventListener('drop', handleDrop);
    });

    let draggedItem;

    function handleDragStart(event) {
    draggedItem = event.target;
    }

    function handleDragOver(event) {
    event.preventDefault();
    }

    function handleDrop(event) {
    event.preventDefault();
    const targetList = event.currentTarget;
    targetList.appendChild(draggedItem);
    }
    
};
