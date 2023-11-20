document.addEventListener('DOMContentLoaded', function () {
    // Initial form count
    var formCount = parseInt("{{ formset.total_form_count }}");

    // Formset container
    var formsetContainer = document.getElementById('ingredients-formset-container');

    // Button to add more forms
    var addFormButton = document.getElementById('add-form');

    // Add form when button is clicked
    addFormButton.addEventListener('click', function () {
        // Clone the last form in the formset
        var lastForm = formsetContainer.lastElementChild;
        var newForm = lastForm.cloneNode(true);

        // Update the form's input names to avoid conflicts
        updateFormInputNames(newForm, formCount);

        // Increment the form count
        formCount++;

        // Append the new form to the formset container
        formsetContainer.appendChild(newForm);
    });
});

function updateFormInputNames(form, formCount) {
    var inputs = form.querySelectorAll(':input');
    inputs.forEach(function (input) {
        var name = input.getAttribute('name').replace(/-\d+-/g, '-' + formCount + '-');
        input.setAttribute('name', name);
    });
}