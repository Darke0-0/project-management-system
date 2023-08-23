window.onload = function() {
    task_fetch();
  };

function task_fetch() {
    var taskset = document.getElementById("mytask").getAttribute("data-context");
    // taskset[0]
    var tasks_set = JSON.parse(JSON.parse(taskset));
    console.log(tasks_set[0]['fields'])
    
    var todo = '';
    var ongoing = '';
    var complete = '';
    var verified = '';
    for (const task_dict of tasks_set) {
        if (task_dict['fields']['state'] == 'T') {
            todo += `<div class="panel"> 
                            <div class="kanban-box item-box"> 
                                <div class="dropdown edit"> 
                                    <a href="#" class="btn-link" data-bs-toggle="dropdown" aria-expanded="false"> 
                                        <i class="fas fa-pencil-alt"></i> 
                                    </a> 
                                    <div class="dropdown-menu dropdown-menu-right"> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#delete_project"><i class="bx bx-trash"></i> Delete</a> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#edit_card_modal"><i class="bx bx-edit mr-5"></i>Edit</a> 
                                    </div> 
                                </div>
                                <div class="content-box">
                                    <h6 class="title fs-16">${task_dict['fields']['heading']}</h6> 
                                    <div class="progress skill-progress mt-15 mb-15" style="height:7px;"> 
                                        <div class="progress-bar progress-animated" style="width: 78%; height:7px;" role="progressbar"> 
                                            <span class="sr-only">78% Complete</span> 
                                        </div> 
                                    </div> 
                                    <div class="d-flex justify-content-between"> 
                                        <div class="link"><a href="#"><i class="fas fa-paperclip"></i></a></div> 
                                        <div class="time"> 
                                            <p class="font-main mb-0"><i class="far fa-clock"></i>Due in 5 days</p> 
                                        </div> 
                                    </div> 
                                </div>
                            </div>
                        </div> `
        };
        if (task_dict['fields']['state'] == 'O') {
            ongoing += `<div class="panel"> 
                            <div class="kanban-box item-box"> 
                                <div class="dropdown edit"> 
                                    <a href="#" class="btn-link" data-bs-toggle="dropdown" aria-expanded="false"> 
                                        <i class="fas fa-pencil-alt"></i> 
                                    </a> 
                                    <div class="dropdown-menu dropdown-menu-right"> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#delete_project"><i class="bx bx-trash"></i> Delete</a> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#edit_card_modal"><i class="bx bx-edit mr-5"></i>Edit</a> 
                                    </div> 
                                </div>
                                <div class="content-box">
                                    <h6 class="title fs-16">${task_dict['fields']['heading']}</h6> 
                                    <div class="progress skill-progress mt-15 mb-15" style="height:7px;"> 
                                        <div class="progress-bar progress-animated" style="width: 78%; height:7px;" role="progressbar"> 
                                            <span class="sr-only">78% Complete</span> 
                                        </div> 
                                    </div> 
                                    <div class="d-flex justify-content-between"> 
                                        <div class="link"><a href="#"><i class="fas fa-paperclip"></i></a></div> 
                                        <div class="time"> 
                                            <p class="font-main mb-0"><i class="far fa-clock"></i>Due in 5 days</p> 
                                        </div> 
                                    </div> 
                                </div>
                            </div>
                        </div> `
        };
        if (task_dict['fields']['state'] == 'C') {
            complete += `<div class="panel"> 
                            <div class="kanban-box item-box"> 
                                <div class="dropdown edit"> 
                                    <a href="#" class="btn-link" data-bs-toggle="dropdown" aria-expanded="false"> 
                                        <i class="fas fa-pencil-alt"></i> 
                                    </a> 
                                    <div class="dropdown-menu dropdown-menu-right"> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#delete_project"><i class="bx bx-trash"></i> Delete</a> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#edit_card_modal"><i class="bx bx-edit mr-5"></i>Edit</a> 
                                    </div> 
                                </div>
                                <div class="content-box">
                                    <h6 class="title fs-16">${task_dict['fields']['heading']}</h6> 
                                    <div class="progress skill-progress mt-15 mb-15" style="height:7px;"> 
                                        <div class="progress-bar progress-animated" style="width: 78%; height:7px;" role="progressbar"> 
                                            <span class="sr-only">78% Complete</span> 
                                        </div> 
                                    </div> 
                                    <div class="d-flex justify-content-between"> 
                                        <div class="link"><a href="#"><i class="fas fa-paperclip"></i></a></div> 
                                        <div class="time"> 
                                            <p class="font-main mb-0"><i class="far fa-clock"></i>Due in 5 days</p> 
                                        </div> 
                                    </div> 
                                </div>
                            </div>
                        </div> `
        };
        if (task_dict['fields']['state'] == 'V') {
            verified += `<div class="panel"> 
                            <div class="kanban-box item-box"> 
                                <div class="dropdown edit"> 
                                    <a href="#" class="btn-link" data-bs-toggle="dropdown" aria-expanded="false"> 
                                        <i class="fas fa-pencil-alt"></i> 
                                    </a> 
                                    <div class="dropdown-menu dropdown-menu-right"> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#delete_project"><i class="bx bx-trash"></i> Delete</a> 
                                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#edit_card_modal"><i class="bx bx-edit mr-5"></i>Edit</a> 
                                    </div> 
                                </div>
                                <div class="content-box">
                                    <h6 class="title fs-16">${task_dict['fields']['heading']}</h6> 
                                    <div class="progress skill-progress mt-15 mb-15" style="height:7px;"> 
                                        <div class="progress-bar progress-animated" style="width: 78%; height:7px;" role="progressbar"> 
                                            <span class="sr-only">78% Complete</span> 
                                        </div> 
                                    </div> 
                                    <div class="d-flex justify-content-between"> 
                                        <div class="link"><a href="#"><i class="fas fa-paperclip"></i></a></div> 
                                        <div class="time"> 
                                            <p class="font-main mb-0"><i class="far fa-clock"></i>Due in 5 days</p> 
                                        </div> 
                                    </div> 
                                </div>
                            </div>
                        </div> `
        };
    };

    todolist.innerHTML = todo;
    ongoinglist.innerHTML = ongoing;
    completelist.innerHTML = complete;
    verifiedlist.innerHTML = verified;
};