// Logic used to add dynamically more forms/lines to the ingredients formset on frontend, to allow users
// to add as much ingredients to their recipe as they want when CREATING private recipes.

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
// to add as much allergens to their recipe as they want when CREATING private recipes.

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
// to allow users to add as much cooking instructions to their recipe as they want when CREATING private recipes.

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
// to allow users to add as much cooking instructions to their recipe as they want when CREATING private recipes.

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


// Logic used to fill the update form with the data from the recipe that the user wants to update.
function fillUpdateForm(recipeName, description, specialNote, cookingTime, numberOfPortions, estimatedCost, originCountry, recipeCategory, recipePic) {
    document.getElementById('id_recipe_name_update').value = recipeName;
    document.getElementById('id_description_update').value = description;
    document.getElementById('id_special_note_update').value = specialNote;
    document.getElementById('id_cooking_time_update').value = cookingTime;
    document.getElementById('id_number_of_portions_update').value = numberOfPortions;
    document.getElementById('id_recipe_estimated_cost_update').value = estimatedCost;
    document.getElementById('id_pic_update').value = recipePic;

    var originCountryDropdown = document.getElementById('id_origin_country_update');
    for (var i = 0; i < originCountryDropdown.options.length; i++) {
        console.log('Option:', originCountryDropdown.options[i].value);
        if (originCountryDropdown.options[i].value === originCountry) {
            console.log('Match found for originCountry:', originCountry);
            originCountryDropdown.options[i].selected = true;
            break;
        }
    }
    console.log('Setting value for originCountry: ', originCountry);

    var recipeCategoryDropdown = document.getElementById('id_recipe_category_update');
    for (var i = 0; i < recipeCategoryDropdown.options.length; i++) {
        console.log('Option:', recipeCategoryDropdown.options[i].value);
        if (recipeCategoryDropdown.options[i].value === recipeCategory) {
            console.log('Match found for recipeCategory:', recipeCategory);
            recipeCategoryDropdown.options[i].selected = true;
            break;
        }
    }
    console.log('Setting value for recipeCategory: ', recipeCategory);
}
