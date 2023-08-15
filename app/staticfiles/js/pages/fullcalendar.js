document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    fetch('http://127.0.0.1:8000/api/projects/calendar_set/')
    .then(response => response.json())
    .then(project_set => {
        let project_list = []
        for (let i = 0; i < project_set.length; i++) {
            var randomColor = Math.floor(Math.random()*16777215).toString(16);
            project_list.push({"title" : project_set[i].title,
                                "start" : project_set[i].start_date,
                                "end" : project_set[i].end_date,
                                "color": '#' + String(randomColor) });
            }
        console.log(project_list)
        var calendar = new FullCalendar.Calendar(calendarEl, {
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
            },
            navLinks: true, // can click day/week names to navigate views
            businessHours: true, // display business hours
            editable: true,
            selectable: true,
            events: project_list
            });

            calendar.render();
        })
});