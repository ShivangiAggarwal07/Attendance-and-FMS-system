const picker = document.getElementById('date_form');
picker.addEventListener('input', function(e){
var day = new Date(this.value).getUTCDay();
if([6,0].includes(day)){
    e.preventDefault();
    this.value = '';
    alert('Weekends not allowed');
} else {
    calc();
}
});

const pickers = document.getElementById('date_to');
pickers.addEventListener('input', function(e){
var day = new Date(this.value).getUTCDay();
if([6,0].includes(day)){
    e.preventDefault();
    this.value = '';
    alert('Weekends not allowed');
} else {
    calc();
}
});

function calc() {
    const date_to = document.getElementById('date_to');
    const date_from = document.getElementById('date_form');
    result = getBusinessDateCount(new Date(date_from.value), new Date(date_to.value));
    var work = document.getElementById("requested_days");
    work.value = result;
}

function getBusinessDateCount(startDate, endDate) {
    var elapsed, daysBeforeFirstSaturday, daysAfterLastSunday;
    var ifThen = function(a, b, c) {
        return a == b ? c : a;
    };

    elapsed = endDate - startDate;
    elapsed /= 86400000;

    daysBeforeFirstSunday = (7 - startDate.getDay()) % 7;
    daysAfterLastSunday = endDate.getDay();

    elapsed -= (daysBeforeFirstSunday + daysAfterLastSunday);
    elapsed = (elapsed / 7) * 5;
    elapsed += ifThen(daysBeforeFirstSunday - 1, -1, 0) + ifThen(daysAfterLastSunday, 6, 5);

    return Math.ceil(elapsed);
}