/** DOMContentLoaded */
bookForm=document.addEventListener('DOMContentLoaded', function() {
    /** Books */
    const bookSubmission = document.getElementById('book-submitted');
    if (bookSubmission != null){
        const bookSubmissionValue= bookSubmission.getAttribute('value');
        console.log("book submission ",bookSubmissionValue)
        /** for book submission */
        if (bookSubmissionValue==="true") {
            showBookConfirmationModal();
        } else {
            console.error('Submission failed');
        }
    }    
});

categoryForm=document.addEventListener('DOMContentLoaded', function() {
    /** Category */
    const categorySubmission = document.getElementById('category-submitted');
    if(categorySubmission != null){
        const categorySubmissionValue= categorySubmission.getAttribute('value');
        /** for category submission */
        if (categorySubmissionValue==="true") {
            showCategoryConfirmationModal();
        } else {
            console.error('Submission failed');
        }
    }
});

authorForm=document.addEventListener('DOMContentLoaded', function() {
    /** Author */
    const authorSubmission = document.getElementById('author-submitted');
    if (authorSubmission != null){
        const authorSubmissionValue= authorSubmission.getAttribute('value');
        /** for author submission */
        if (authorSubmissionValue==="true") {
            showAuthorConfirmationModal();
        } else {
            console.error('Submission failed');
        }
    }
    
});

const time_in_second=2500;
/** Show books submission modal */
function showBookConfirmationModal() {
    const confirmationModal = new bootstrap.Modal(document.getElementById('bookConfirmationModal'));
    confirmationModal.show();
    setTimeout(() => {
        confirmationModal.hide();
    }, time_in_second);
};


/** Show category submission modal */
function showCategoryConfirmationModal() {
    const confirmationModal = new bootstrap.Modal(document.getElementById('categoryConfirmationModal'));
    confirmationModal.show();
    setTimeout(() => {
        confirmationModal.hide();
    }, time_in_second);
};

/** Show author submission modal */
function showAuthorConfirmationModal() {
    const confirmationModal = new bootstrap.Modal(document.getElementById('authorConfirmationModal'));
    confirmationModal.show();
    setTimeout(() => {
        confirmationModal.hide();
    }, time_in_second);
};