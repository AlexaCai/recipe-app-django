// Logic used to add dynamically more forms/lines to the ingredients formset on frontend, to allow users
// to add as much ingredients to their recipe as they want when SUBMITTING recipes.

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    var formsetContainer = document.getElementById('ingredients-formset-container');
    var addFormButton = document.getElementById('add-form');
    console.log(addFormButton);  // This should log the button element

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
// to add as much allergens to their recipe as they want when SUBMITTING recipes.

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
// to allow users to add as much cooking instructions to their recipe as they want when SUBMITTING recipes.

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

// Logic used to add dynamically more forms/lines to the cooking tools formset on frontend, 
// to allow users to add as much cooking instructions to their recipe as they want when SUBMITTING recipes.

document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('recipe-tools-formset-container');

    var addFormButton = document.getElementById('recipe-tools-form');

    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('recipe_tools_formset');
        var lastFormset = formsets[formsets.length - 1];
        var newFormset = lastFormset.cloneNode(true);

        var formsetContainerCount = formsets.length;
        updateFormInputNames(newFormset, formsetContainerCount);

        formsetContainer.appendChild(newFormset);

        updateFormsetManagementForm(formsetContainer, formsetContainerCount + 1);
    });
});

// Logic used to add dynamically more forms/lines to the similar recipes formset on frontend, 
// to allow users to add as much cooking instructions to their recipe as they want when SUBMITTING recipes.

document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('recipe-similar-complementary-formset-container');

    var addFormButton = document.getElementById('recipe-similar-complementary-form');

    addFormButton.addEventListener('click', function () {
        console.log('Button Clicked');
        var formsets = formsetContainer.getElementsByClassName('recipe_similar_complementary_formset');
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