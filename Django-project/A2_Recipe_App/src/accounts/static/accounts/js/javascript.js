// When the document is fully loaded, it calls the handleFormsets function for three different formsets
document.addEventListener('DOMContentLoaded', function () {
    handleFormsets('ingredients-formset-container', 'add-ingredient-form', 'remove-ingredient-form', 'ingredients_formset');
    handleFormsets('allergens-formset-container', 'add-allergen-form', 'remove-allergen-form', 'allergen_formset');
    handleFormsets('cooking-instructions-formset-container', 'add-cooking-instruction-form', 'remove-cooking-instruction-form', 'cooking_instructions_formset');
});

// handleFormsets function takes four arguments: the IDs of the formset container, the add button, etc... 
// It gets these elements from the DOM and sets up event listeners for the add and remove buttons.
function handleFormsets(containerId, addBtnId, removeBtnId, formsetClass) {
    var formsetContainer = document.getElementById(containerId);
    var addFormButton = document.getElementById(addBtnId);
    var removeFormButton = document.getElementById(removeBtnId);

        // Hide the remove button if there's only one formset (default when modal open)
        var formsets = formsetContainer.getElementsByClassName(formsetClass);
        if (formsets.length <= 1) {
            removeFormButton.style.display = 'none';
        }

        // Adds a new formset to the formset container when the add button is clicked, 
        // and updates the formset management form to reflect the new total forms count. 
        // also makes the remove button visible.
    addFormButton.addEventListener('click', function () {
        var formsets = formsetContainer.getElementsByClassName(formsetClass);
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);

        // Clear the values of the inputs in the new formset
        var inputs = newFormset.querySelectorAll('input[type="text"], input[type="number"]');
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].value = '';
        }

        // Clear the value of the textarea in the new formset
        var textarea = newFormset.querySelector('textarea');
        if (textarea) {
            textarea.value = '';
        }

        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);

        formsetContainer.appendChild(newFormset);

        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);

        // Show the remove button when a new formset is added
        removeFormButton.style.display = 'block';
    });

    // Removes the last formset from the formset container when the remove button is clicked, 
    // updates the names of the input fields in the remaining formsets, updates the formset management 
    // form to reflect the new total forms count, and hides the remove button if there's only one 
    // formset left.
    removeFormButton.addEventListener('click', function () {
        var formsets = Array.from(formsetContainer.getElementsByClassName(formsetClass));
        if (formsets.length > 1) {
            var lastFormset = formsets[formsets.length - 1];
            formsetContainer.removeChild(lastFormset);
    
            for (var i = 0; i < formsets.length - 1; i++) {
                updateFormInputNames(formsets[i], i);
            }
    
            updateFormsetManagementForm(formsetContainer, formsets.length - 1);
    
            // Get the updated list of formsets
            formsets = Array.from(formsetContainer.getElementsByClassName(formsetClass));
    
            // Hide the remove button if there's only one formset left
            if (formsets.length <= 1) {
                removeFormButton.style.display = 'none';
            }
        }
    });
}

// Selects all elements in the form that have a name attribute, and for each input, it replaces
// the index in the name with the new index. This is done using a regular expression that matches 
// -<number>- and replaces it with -<newIndex>-
function updateFormInputNames(form, formIndex) {
    var inputs = form.querySelectorAll('[name]');
    inputs.forEach(function (input) {
        var name = input.getAttribute('name').replace(/-\d+-/g, '-' + formIndex + '-');
        input.setAttribute('name', name);
    });
}

// Used to let the code know how many forms there are / are submitted
function updateFormsetManagementForm(formsetContainer, formCount) {
    var totalFormsInput = formsetContainer.querySelector('input[name$="TOTAL_FORMS"]');
    
    if (totalFormsInput) {
        totalFormsInput.value = formCount;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    // Initialize visible card count
    var visibleCardCount = 6;

    // Function to show additional cards
    function showMoreCards() {
        // Initialize hidden cards here
        var hiddenCards = document.querySelectorAll('.recipe-card-hidden');
        for (var i = 0; i < hiddenCards.length && i < 6; i++) {
            hiddenCards[i].classList.remove('recipe-card-hidden');
            visibleCardCount++;
        }

        // Hide the "Show More" button if the number of cards shown is not 6
        if (i < 6) {
            document.getElementById('showMoreButton').style.display = 'none';
            document.getElementById('hideExtraCardButton').style.display = 'block';
        }

        // Append a new "Show More" button after the newly revealed cards
        appendShowMoreButton();
    }

    // Function to hide extra cards
    function hideExtraCards() {
        // Select all cards
        var cards = document.querySelectorAll('.recipe-card-padding');
        for (var i = 7; i < cards.length; i++) {
            cards[i].classList.add('recipe-card-hidden');
        }

        // Update the visible card count
        visibleCardCount = 6;

        // Hide the "Hide" button and show the "Show More" button
        document.getElementById('hideExtraCardButton').style.display = 'none';
        document.getElementById('showMoreButton').style.display = 'block';
    }

    // Attach click event to the initial "Show More" button
    document.getElementById('showMoreButton').addEventListener('click', showMoreCards);

    // Attach click event to the "Hide" button
    document.getElementById('hideExtraCardButton').addEventListener('click', hideExtraCards);
});


function scrollToSection(event, targetSectionId) {
    event.preventDefault();
    var targetSection = document.querySelector(targetSectionId);
    var offset = targetSection.getBoundingClientRect().top + window.scrollY;
    window.scrollTo({
        top: offset,
        behavior: 'smooth'
    });
}

var backToTopLink1 = document.querySelector('.back-to-top a');
var backToCreatedRecipes = document.querySelector('#hideExtraCardButton');

backToTopLink1.addEventListener('click', function (event) {
    scrollToSection(event, '#topsection');
});

backToCreatedRecipes.addEventListener('click', function (event) {
    scrollToSection(event, '#createdRecipes');
});
