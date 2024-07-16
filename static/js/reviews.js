const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_insight");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewtId}` endpoint.
*/

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      console.log(reviewId)
      let reviewContent = document.getElementById(`review${reviewId}`).innerText;
      console.log(`${reviewContent}`)
      reviewText.value = reviewContent;
      submitButton.innerText = "Update";
      reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
  }