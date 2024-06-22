const toggleSidebar = document.getElementById('toggle-sidebar');
const sidebarContainer = document.querySelector('.sidebar-container');

toggleSidebar.addEventListener('click', () => {
    sidebarContainer.classList.toggle('show');
});

var sidebar = document.querySelector('.sidebar');
var mainContent = document.querySelector('.main-content');

sidebar.addEventListener('mouseover', function() {
    mainContent.classList.add('move-right');
});

sidebar.addEventListener('mouseout', function() {
    mainContent.classList.remove('move-right');
});

const reportPopup = document.getElementById('reportPopup');
const closeBtn = reportPopup.querySelector('.close-btn');
const reportBtns = document.querySelectorAll('.report-btn');
const submitReportBtn = document.getElementById('submitReport');

reportBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        reportPopup.style.display = 'block';
    });
});

closeBtn.addEventListener('click', () => {
    reportPopup.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === reportPopup) {
        reportPopup.style.display = 'none';
    }
});

submitReportBtn.addEventListener('click', () => {
    const summary = document.getElementById('reportSummary').value;
    const progressStatus = document.querySelector('input[name="progressStatus"]:checked').value;
    console.log('Progress Summary:', summary);
    console.log('Progress Status:', progressStatus);
    reportPopup.style.display = 'none';
});

const taskOverview = document.getElementById('taskOverview');

taskOverview.addEventListener('click', (event) => {
    const target = event.target;

    if (target.classList.contains('accept-btn')) {
        const taskStatus = target.closest('.task').querySelector('.task > div:nth-child(4)');
        taskStatus.textContent = 'Accepted';
        taskStatus.style.color = 'green';
        target.disabled = true;
    } else if (target.classList.contains('report-btn')) {
        reportPopup.style.display = 'block';
    } else if (target.classList.contains('finish-btn')) {
        const taskStatus = target.closest('.task').querySelector('.task > div:nth-child(4)');
        taskStatus.textContent = 'Finished ✓';
        taskStatus.style.color = 'green';
        target.disabled = true;
        const acceptBtn = target.closest('.task-buttons').querySelector('.accept-btn');
        acceptBtn.disabled = true;
        const reportBtn = target.closest('.task-buttons').querySelector('.report-btn');
        reportBtn.disabled = true;
    }
});