document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('book-form');

    form.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(form);
        console.log("about to enter the try")
        if (response.ok) {
            showConfirmationModal();
        } else {
            console.error('Submission failed');
        }
        /*try {
            const response = await fetch('/submit-url', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                showConfirmationModal();
            } else {
                console.error('Submission failed');
            }
        } catch (error) {
            console.error('Error:', error);
        }*/
    });

    function showConfirmationModal() {
        const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        confirmationModal.show();

        setTimeout(() => {
            confirmationModal.hide();
        }, 2000);
    }
});