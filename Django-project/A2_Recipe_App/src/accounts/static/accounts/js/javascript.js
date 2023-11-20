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

function updateFormInputNames(form, formCount) {
    var inputs = form.querySelectorAll('[name]');
    inputs.forEach(function (input) {
        var name = input.getAttribute('name').replace(/-\d+-/g, '-' + formCount + '-');
        input.setAttribute('name', name);
        // Clear input values to avoid conflicts
        input.value = '';
    });
}

function updateFormsetManagementForm(formsetContainer, formCount) {
    var totalFormsInput = formsetContainer.querySelector('input[name$="TOTAL_FORMS"]');
    
    if (totalFormsInput) {
        totalFormsInput.value = formCount;
    }
}