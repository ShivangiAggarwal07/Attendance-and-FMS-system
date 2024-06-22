document.addEventListener("DOMContentLoaded", function() {
    
    function updateDateTime() {
        document.getElementById('dateTime').innerText = new Date().toLocaleString();
    }
    updateDateTime();
    setInterval(updateDateTime, 1000);

    const attendanceData = {
        timeIn: "09:00 AM",
        timeOut: "05:00 PM",
        totalHours: "8 hours",
        daysPresent: 20,
        daysAbsent: 2,
        leaveTaken: 3
    };
    const leaveData = {
        leaveBalance: 5,
        holidays: ["Independence Day - 4th July", "Labor Day - 2nd September"],
        leaveRequests: {
            pending: ["Vacation - 5th June", "Medical - 12th June"],
            approved: ["Sick Leave - 1st June"],
            rejected: ["Vacation - 3rd June"]
        }
    };

    const taskData = {
        tasks: [
            {name: "Make Homepage UI", assignedDate: "2024-05-28", dueDate: "2024-06-02", status: "In Progress"},
            {name: "Connect it with <br>backend", assignedDate: "2024-05-29", dueDate: "2024-06-03", status: "Pending"},
            {name: "Apply an AI functionality <br>in the project", assignedDate: "2024-05-30", dueDate: "2024-06-04", status: "Completed"}
        ],
        plannedTime: "40 hours",
        actualTime: "38 hours"
    };

    document.getElementById('timeIn').innerText = attendanceData.timeIn;
    document.getElementById('timeOut').innerText = attendanceData.timeOut;
    document.getElementById('totalHours').innerText = attendanceData.totalHours;
    document.getElementById('daysPresent').innerText = attendanceData.daysPresent;
    document.getElementById('daysAbsent').innerText = attendanceData.daysAbsent;
    document.getElementById('leaveTaken').innerText = attendanceData.leaveTaken;

    document.getElementById('leaveBalance').innerText = leaveData.leaveBalance;
    const holidaysList = document.getElementById('holidaysList');
    leaveData.holidays.forEach(holiday => {
        let li = document.createElement('li');
        li.innerText = holiday;
        holidaysList.appendChild(li);
    });

    const leaveRequestsList = document.getElementById('leaveRequestsList');
    const pendingRequests = document.createElement('li');
    pendingRequests.innerText = `Pending Requests: ${leaveData.leaveRequests.pending.join(", ")}`;
    leaveRequestsList.appendChild(pendingRequests);
    const approvedRequests = document.createElement('li');
    approvedRequests.innerText = `Approved Requests: ${leaveData.leaveRequests.approved.join(", ")}`;
    leaveRequestsList.appendChild(approvedRequests);
    const rejectedRequests = document.createElement('li');
    rejectedRequests.innerText = `Rejected Requests: ${leaveData.leaveRequests.rejected.join(", ")}`;
    leaveRequestsList.appendChild(rejectedRequests);

    
    const taskOverview = document.querySelector('.tasks-section');
    taskData.tasks.forEach(task => {
        const taskElement = document.createElement('div');
        taskElement.className = 'task';
        taskElement.innerHTML = `
            <div>${task.name}</div>
            <div>${task.assignedDate}</div>
            <div>${task.dueDate}</div>
            <div>${task.status}</div>
            <div class="task-buttons">
                <button class="accept-btn">Accept</button>
                <button class="report-btn" data-index="${index}">Report Progress</button>
                <div class="dropdown-content" id="reportDropdown-${index}">
                    <a href="#" data-status="Not Started">Not Started</a>
                    <a href="#" data-status="In Progress">In Progress</a>
                    <a href="#" data-status="Completed">Completed</a>
                </div>
                <button class="finish-btn">Finish</button>
            </div>
        `;
        taskOverview.appendChild(taskElement);
    });

    document.getElementById('plannedTime').innerText = taskData.plannedTime;
    document.getElementById('actualTime').innerText = taskData.actualTime;

    //Future: Functions for handling facial recognition, leave approvals, etc. can be added here
    
    document.querySelectorAll('.report-btn').forEach(button => {
        button.addEventListener('click', function() {
            const index = this.getAttribute('data-index');
            const dropdown = document.getElementById(`reportDropdown-${index}`);
            dropdown.classList.toggle('show');
        });
    });

    document.querySelectorAll('.dropdown-content a').forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const newStatus = this.getAttribute('data-status');
            const taskIndex = this.closest('.dropdown-content').id.split('-')[1];
            taskData.tasks[taskIndex].status = newStatus;
            document.querySelectorAll('.task-status')[taskIndex].innerText = newStatus;
            this.closest('.dropdown-content').classList.remove('show');
        });
    });

    // Close the dropdown if the user clicks outside of it
    window.addEventListener('click', function(event) {
        if (!event.target.matches('.report-btn')) {
            document.querySelectorAll('.dropdown-content').forEach(dropdown => {
                if (dropdown.classList.contains('show')) {
                    dropdown.classList.remove('show');
                }
            });
        }
    });
    
    document.querySelector('.attendance-widget').addEventListener('click', function() {
        alert('Facial recognition attendance recorded!');
    });
});
