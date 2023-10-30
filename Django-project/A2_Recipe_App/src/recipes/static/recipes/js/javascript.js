//***Logic to handle the main search functionality

document.getElementById('button-addon2').addEventListener('click', function () {
    console.log('Button clicked');
    performSearch();
});


function performSearch() {
    var searchQuery = document.getElementById('recipe-search-input').value;
    console.log(searchQuery)

    if (!searchQuery) {
        console.log('Search query is empty');
        return;
    }

    fetch(`/search-recipe-name/?query=${searchQuery}`)
        .then(response => response.json())
        .then(data => {
            displaySearchResults(data);
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function displaySearchResults(data) {
    var recipes = data.recipes;
    var searchResultsContainer = document.getElementById('search-results');
    showSearchResultsSection();

    searchResultsContainer.innerHTML = '';

    if (recipes.length === 0) {
        searchResultsContainer.innerHTML = 'No recipes found.';
    } else {
        recipes.forEach(function (recipe) {
            var recipeCard = document.createElement('div');
            recipeCard.className = 'col-xl-4 col-lg-6 col-sm-12 card-padding';

            var headingContainer = document.createElement('div');
            headingContainer.style.textAlign = 'center';
            headingContainer.innerHTML = `
            <br>
            <br>
            <h1 class="recipes-continent-title-section">Search results</h1> 
            <div class="icon-legend">
                <img src="../../../media/flag-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>Country</span>
                <span class="vertical-line">|</span>
                <img src="../../../media/difficulty-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>Difficulty</span>
                <span class="vertical-line">|</span>
                <img src="../../../media/category-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>Category</span>
            </div> 
            <br>
            <br>`;

            recipeCard.innerHTML = `
                <br>
                <div class="card text-bg-dark">
                    <img src="${recipe.pic}" class="img-fluid" alt="recipe-image">
                    <div class="card-img-overlay">
                        <div class="card-text">
                            <h5 class="card-title">${recipe.recipe_name}</h5>
                            <div class="line-background">
                                <img src="../../../media/flag-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>${ recipe.recipe_origin_country }</span>
                            </div>
                            <br>
                            <div class="line-background">
                                <img src="../../../media/difficulty-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>${ recipe.recipe_difficulty }</span>
                            </div>
                            <br>
                            <div class="line-background">
                                <img src="../../../media/category-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>${ recipe.recipe_category }</span>
                            </div>                        
                        </div>
                    </div>
                </div>
            `;
            searchResultsContainer.appendChild(headingContainer);
            searchResultsContainer.appendChild(recipeCard);
        });
    }
}

function showSearchResultsSection() {
    var defaultContentSections = document.getElementsByClassName('default-content');

    for (var i = 0; i < defaultContentSections.length; i++) {
        defaultContentSections[i].style.display = 'none';
    }

    var searchResultsSection = document.getElementById('search-results');
    searchResultsSection.style.display = 'block';
}

//***Logic to handle the search by ingredients functionality

//***In progress

//***Logic to handle the main search by filters functionality

//***In progress
