// Logic used to add dynamically more forms/lines to the ingredients formset on frontend, to allow users
// to add as much ingredients to their recipe as they want.

document.addEventListener('DOMContentLoaded', function () {
    // Formset container
    var formsetContainer = document.getElementById('ingredients-formset-container');

    // Button to add more forms
    var addFormButton = document.getElementById('add-form');

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
// to add as much allergens to their recipe as they want.

document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('allergens-formset-container');

    var addFormButton = document.getElementById('allergen-form');

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
// to allow users to add as much cooking instructions to their recipe as they want.

document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('cooking-instructions-formset-container');

    var addFormButton = document.getElementById('cooking-instructions-form');

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

function updateFormInputNames(form, formCount) {
    var inputs = form.querySelectorAll('[name]');
    inputs.forEach(function (input) {
        var name = input.getAttribute('name').replace(/-\d+-/g, '-' + formCount + '-');
        input.setAttribute('name', name);
        input.value = '';
    });
}

function updateFormsetManagementForm(formsetContainer, formCount) {
    var totalFormsInput = formsetContainer.querySelector('input[name$="TOTAL_FORMS"]');
    
    if (totalFormsInput) {
        totalFormsInput.value = formCount;
    }
}