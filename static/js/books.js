document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('submitted-status');
    const value= form.getAttribute('value')

    if (value==="true") {
        showConfirmationModal();
    } else {
        console.error('Submission failed');
    }
});

function showConfirmationModal() {
    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();

    setTimeout(() => {
        confirmationModal.hide();
    }, 5000);
};