/** DOMContentLoaded */
document.addEventListener('DOMContentLoaded', function() {
    /** Books */
    const bookSubmission = document.getElementById('book-submitted');
    if (bookSubmission != null){
        const bookSubmissionValue= bookSubmission.getAttribute('value');
        /** for book submission */
        if (bookSubmissionValue==="true") {
            showBookConfirmationModal();
        } 
    }
    
     /** Category */
     const categorySubmission = document.getElementById('category-submitted');
     if(categorySubmission != null){
         const categorySubmissionValue= categorySubmission.getAttribute('value');
         /** for category submission */
         if (categorySubmissionValue==="true") {
             showCategoryConfirmationModal();
         }
     }

     /** Author */
    const authorSubmission = document.getElementById('author-submitted');
    if (authorSubmission != null){
        const authorSubmissionValue= authorSubmission.getAttribute('value');
        /** for author submission */
        if (authorSubmissionValue==="true") {
            showAuthorConfirmationModal();
        } 
    }

    /** Notification Messages auto-hide */
    const notificationMsg=document.getElementById('msg');
    if(notificationMsg!=null){
        setTimeout(()=>{
            notificationMsg.classList.remove('show');
        },time_in_second)
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
