window.onload = function() {
    user_chat();

  };

function user_chat() {
    let user_list = [];
    fetch(`http://127.0.0.1:8000/api/projects/load_users/`)
        .then(response => response.json())
        .then(users => {
        users.sort()
        filterDropDown(
            document.getElementById('dropdown'),
            document.getElementById('input'),
            users
            )})

    function filterDropDown(dropdown, input, items) {
        //create dropdown items from list of items
        for (let i=0; i<items.length; i++) {
            let dropdown_item = document.createElement('a');
            dropdown_item.setAttribute('href', '#'+items[i].id);
            dropdown_item.setAttribute('class', 'dropdown-item');
            dropdown_item.addEventListener('click', () => {
                fetchMessage(items[i].id)
            })
            dropdown_item.innerHTML = items[i].name;
            dropdown.appendChild(dropdown_item);
        }
        // fetchMessage(dropdown):
    
        input.addEventListener('input', function () {
            let dropdown_items = dropdown.querySelectorAll('.dropdown-item');
            console.log("click")
            if (!dropdown_items)
                return false;
            for (let i=0; i<dropdown_items.length; i++) {
                if (dropdown_items[i].innerHTML.toUpperCase().includes(input.value.toUpperCase()))
                    dropdown_items[i].style.display = 'block';
                else
                    dropdown_items[i].style.display = 'none';
            }
        });
        function fetchMessage(id){
            fetch(`../joinroom/${id}`)
            .then(response => response.json())
            .then(message => {
                console.log(message)
                const socket = new WebSocket(
                    'ws://'
                    + window.location.host
                    + 'ws/api/chat/chatroom/'
                    + id
                    + '/'
                );

                socket.onopen = function(e){
                    console.log("CONNECTION ESTABLISHED");
                }
                
                socket.onclose = function(e){
                    console.log("CONNECTION LOST");
                }
                
                socket.onerror = function(e){
                    console.log("ERROR OCCURED");
                }
            const user_id = document.getElementById('user_id').textContent;
            })
        }
    }
};

function chatroom(value) {
    window.location.assign(`${value}.html`);
};
