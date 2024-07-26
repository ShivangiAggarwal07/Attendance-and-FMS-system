const video = document.getElementById('video');

// Get access to the camera
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.srcObject = stream;
        video.play();
    });
}

document.getElementById('scanButton').addEventListener('click', function() {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = 'Processing...';

    // Here you would capture the image from the video and send it to your backend for processing.
    // For this example, we'll simulate a response.

    setTimeout(function() {
        // Simulated response
        const recognized = Math.random() > 0.5; // Randomly simulate recognition for demo purposes
        if (recognized) {
            resultDiv.innerHTML = 'Attendance approved: John Doe';
        } else {
            resultDiv.innerHTML = 'Face not recognized. Registering new face...';
        }
    }, 2000);
});
