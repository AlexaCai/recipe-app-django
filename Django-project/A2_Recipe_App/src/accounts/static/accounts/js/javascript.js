// Logic used to add dynamically more forms/lines to the ingredients formset on frontend, to allow users
// to add as much ingredients to their recipe as they want when CREATING private recipes.
document.addEventListener('DOMContentLoaded', function () {
    console.log('DOMContentLoaded fired'); 

    var formsetContainer = document.getElementById('ingredients-formset-container');
    var addFormButton = document.getElementById('ingredient-form');
    var removeFormButton = document.getElementById('remove-ingredient-form');

    // Initially, hide the "Remove Ingredient" button if there's only one formset
    updateRemoveIngredientButton();

    // Add form when "ingredient-form" button is clicked
    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('ingredients_formset');
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);
    
        // Clear the input fields in the new formset
        var inputs = newFormset.querySelectorAll('input[type="text"], input[type="number"]');
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].value = '';
        }

        // Clear the textarea fields in the new formset
        var textarea = newFormset.querySelector('textarea');
            textarea.value = '';

        // Update the names of the input fields in the new formset
        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);
    
        // Append the new formset container after the last formset container
        formsetContainer.appendChild(newFormset);
    
        // Update the visibility of the "Remove Ingredient" button
        updateRemoveIngredientButton();
        
        // Update formset management form
        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);
    });

    // Remove form when the "Remove Ingredient" button is clicked
    removeFormButton.addEventListener('click', function () {
        var formsets = Array.from(formsetContainer.getElementsByClassName('ingredients_formset'));
        if (formsets.length > 1) {
            var lastFormset = formsets[formsets.length - 1];
            formsetContainer.removeChild(lastFormset);
    
            // Update the names of the input fields in the remaining formsets
            for (var i = 0; i < formsets.length - 1; i++) {
                updateFormInputNames(formsets[i], i);
            }
    
            // Update the visibility of the "Remove Ingredient" button
            updateRemoveIngredientButton();
            
            // Update formset management form
            updateFormsetManagementForm(formsetContainer, formsets.length - 1);
        }
    });
});

function updateRemoveIngredientButton() {
    var formsetContainer = document.getElementById('ingredients-formset-container');
    var removeFormButton = document.getElementById('remove-ingredient-form');

    var formsets = formsetContainer.getElementsByClassName('ingredients_formset');
    console.log('Number of formsets:', formsets.length);

    if (formsets.length > 1) {
        removeFormButton.style.display = 'inline-block';
    } else {
        removeFormButton.style.display = 'none';
    }
}


// Logic used to add dynamically more forms/lines to the allergens formset on frontend, to allow users
// to add as much allergens to their recipe as they want when CREATING private recipes.
document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('allergens-formset-container');
    var addFormButton = document.getElementById('allergen-form');
    var removeFormButton = document.getElementById('remove-allergen-form');

    updateRemoveAllergensButton();

    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('allergen_formset');
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);
    
        var inputs = newFormset.querySelectorAll('input[type="text"]');
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].value = '';
        }
    
        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);
    
        formsetContainer.appendChild(newFormset);
    
        updateRemoveAllergensButton();
        
        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);
    });

    removeFormButton.addEventListener('click', function () {
        var formsets = Array.from(formsetContainer.getElementsByClassName('allergen_formset'));
        if (formsets.length > 1) {
            var lastFormset = formsets[formsets.length - 1];
            formsetContainer.removeChild(lastFormset);
    
            for (var i = 0; i < formsets.length - 1; i++) {
                updateFormInputNames(formsets[i], i);
            }
    
            updateRemoveAllergensButton();
            
            updateFormsetManagementForm(formsetContainer, formsets.length - 1);
        }
    });
});

function updateRemoveAllergensButton() {
    var formsetContainer = document.getElementById('allergens-formset-container');
    var removeFormButton = document.getElementById('remove-allergen-form');

    var formsets = formsetContainer.getElementsByClassName('allergen_formset');
    console.log('Number of formsets:', formsets.length);

    if (formsets.length > 1) {
        removeFormButton.style.display = 'inline-block';
    } else {
        removeFormButton.style.display = 'none';
    }
}

// Logic used to add dynamically more forms/lines to the cooking instructions formset on frontend, 
// to allow users to add as much cooking instructions to their recipe as they want when CREATING private recipes.
document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('cooking-instructions-formset-container');
    var addFormButton = document.getElementById('cooking-instructions-form');
    var removeFormButton = document.getElementById('remove-instructions-form');

    updateRemoveInstructionsButton();

    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('cooking_instructions_formset');
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);
    
        var inputs = newFormset.querySelectorAll('input[type="text"]');
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].value = '';
        }
    
        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);
    
        formsetContainer.appendChild(newFormset);
    
        updateRemoveInstructionsButton();
        
        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);
    });

    removeFormButton.addEventListener('click', function () {
        var formsets = Array.from(formsetContainer.getElementsByClassName('cooking_instructions_formset'));
        if (formsets.length > 1) {
            var lastFormset = formsets[formsets.length - 1];
            formsetContainer.removeChild(lastFormset);
    
            for (var i = 0; i < formsets.length - 1; i++) {
                updateFormInputNames(formsets[i], i);
            }
    
            updateRemoveInstructionsButton();
            
            updateFormsetManagementForm(formsetContainer, formsets.length - 1);
        }
    });
});

function updateRemoveInstructionsButton() {
    var formsetContainer = document.getElementById('cooking-instructions-formset-container');
    var removeFormButton = document.getElementById('remove-instructions-form');

    var formsets = formsetContainer.getElementsByClassName('cooking_instructions_formset');
    console.log('Number of formsets:', formsets.length);

    if (formsets.length > 1) {
        removeFormButton.style.display = 'inline-block';
    } else {
        removeFormButton.style.display = 'none';
    }
}


// Logic used to add dynamically more forms/lines to the ingredients formset on frontend, to allow users
// to add as much ingredients to their recipe as they want when UPDATING private recipes.

document.addEventListener('DOMContentLoaded', function () {
    // Formset container
    var formsetContainer = document.getElementById('ingredients-formset-update-container');

    // Button to add more forms
    var addFormButton = document.getElementById('add-ingredient-update-form');

    // Add form when button is clicked
    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('formset');
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);

        // Update the formsetContainer ID to avoid duplicate IDs
        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);

        // Append the new formset container after the last formset container
        formsetContainer.appendChild(newFormset);

        // Update formset management form
        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);
    });
});


// Logic used to add dynamically more forms/lines to the allergens formset on frontend, to allow users
// to add as much allergens to their recipe as they want when UPDATING private recipes.

document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('allergens-formset-update-container');

    var addFormButton = document.getElementById('allergen-update-form');

    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('allergen_formset');
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);

        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);

        formsetContainer.appendChild(newFormset);

        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);
    });
});


// Logic used to add dynamically more forms/lines to the cooking instructions formset on frontend, 
// to allow users to add as much cooking instructions to their recipe as they want when UPDATING private recipes.

document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('cooking-instructions-formset-update-container');

    var addFormButton = document.getElementById('cooking-instructions-update-form');

    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('cooking_instructions_formset');
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);

        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);

        formsetContainer.appendChild(newFormset);

        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);
    });
});


function updateFormInputNames(form, formIndex) {
    var inputs = form.querySelectorAll('[name]');
    inputs.forEach(function (input) {
        var name = input.getAttribute('name').replace(/-\d+-/g, '-' + formIndex + '-');
        input.setAttribute('name', name);
    });
}

function updateFormsetManagementForm(formsetContainer, formCount) {
    var totalFormsInput = formsetContainer.querySelector('input[name$="TOTAL_FORMS"]');
    
    if (totalFormsInput) {
        totalFormsInput.value = formCount;
    }
}