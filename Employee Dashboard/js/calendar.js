    //get the current date
    const currentDate = new Date();

    //get the month and year
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();

    //get the calendar container
    const calendar = document.querySelector('.calendar');

    //get the month and year elements
    const monthYear = document.getElementById('monthYear');

    //get the previous and next month buttons
    const prevMonthBtn = document.getElementById('prevMonthBtn');
    const nextMonthBtn = document.getElementById('nextMonthBtn');

    //initialize the calendar
    function initCalendar() {
        //set the month and year
        monthYear.textContent = getMonthName(currentMonth) + ' ' + currentYear;

        //clear the days container
        const daysContainer = document.querySelector('.days');
        daysContainer.innerHTML = '';

        //get the first day of the month
        const firstDay = new Date(currentYear, currentMonth, 1).getDay();

        //get the number of days in the month
        const numDays = new Date(currentYear, currentMonth + 1, 0).getDate();

        //add empty cells for previous month
        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement('div');
            emptyCell.classList.add('empty-cell');
            daysContainer.appendChild(emptyCell);
        }

        //add days of the month
        for (let i = 1; i <= numDays; i++) {
            const dayCell = document.createElement('div');
            dayCell.textContent = i;
            dayCell.classList.add('day-cell');

            // Mark attendance
            const date = new Date(currentYear, currentMonth, i);
            const attendanceStatus = getAttendanceStatus(date);
            if (attendanceStatus === 'present') {
                dayCell.classList.add('present');
            } else if (attendanceStatus === 'absent') {
                dayCell.classList.add('absent');
            }

            daysContainer.appendChild(dayCell);
        }
    }

    //name of the month
    function getMonthName(month) {
        const months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ];
        return months[month];
    }
    function getAttendanceStatus(date) {
    const attendanceDates = {
    '2023-06-01': 'present',
    '2023-06-03': 'absent',
    '2023-06-05': 'present',
    '2023-06-08': 'absent',
    '2023-06-10': 'present',
    };

    const dateStr = date.toISOString().slice(0, 10);
    return attendanceDates[dateStr] || '';
    }
    prevMonthBtn.addEventListener('click', () => {
        currentMonth--;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        }
        initCalendar();
    });

    nextMonthBtn.addEventListener('click', () => {
        currentMonth++;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        initCalendar();
    });

    
    // Initialize the calendar
    initCalendar();
    const dayCells = document.querySelectorAll('.day-cell');
    dayCells.forEach(cell => {
        cell.addEventListener('click', () => {
            const date = new Date(currentYear, currentMonth, cell.textContent);
            const attendanceStatus = getAttendanceStatus(date);
            showAttendancePopup(date, attendanceStatus);
        });
    });
    function showAttendancePopup(date, attendanceStatus) {
        const popup = document.createElement('div');
        popup.classList.add('attendance-popup');
    
        const popupContent = document.createElement('div');
        popupContent.classList.add('popup-content');
    
        const dateStr = date.toDateString();
        const attendanceText = attendanceStatus === 'present' ? 'Present' : attendanceStatus === 'absent' ? 'Absent' : 'No data';
        const timeIn = '9:00 AM'; // Dummy time in
        const timeOut = '6:00 PM'; // Dummy time out
    
        popupContent.innerHTML = `
            <h3>${dateStr}</h3>
            <p>Attendance: ${attendanceText}</p>
            <p>Time In: ${timeIn}</p>
            <p>Time Out: ${timeOut}</p>
        `;
    
        popup.appendChild(popupContent);
        document.body.appendChild(popup);
    
        // Close the popup when clicked outside
        window.addEventListener('click', (e) => {
            if (e.target === popup) {
                popup.remove();
            }
        });
    }