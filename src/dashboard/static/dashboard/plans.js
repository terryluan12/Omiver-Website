// Plans Dashboard JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Day tab switching functionality
    const dayTabs = document.querySelectorAll('.day-tab');
    const dayTrainings = document.querySelectorAll('.day-training');
    
    dayTabs.forEach((tab, index) => {
        tab.addEventListener('click', function() {
            // Remove active class from all tabs and trainings
            dayTabs.forEach(t => t.classList.remove('active'));
            dayTrainings.forEach(t => t.classList.remove('active'));
            
            // Add active class to clicked tab
            tab.classList.add('active');
            
            // Show corresponding training content
            if (dayTrainings[index]) {
                dayTrainings[index].classList.add('active');
            }
        });
    });
    
    // Feedback button functionality
    const feedbackBtns = document.querySelectorAll('.feedback-btn');
    feedbackBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Add your feedback functionality here
            alert('Feedback functionality would be implemented here');
        });
    });
});
