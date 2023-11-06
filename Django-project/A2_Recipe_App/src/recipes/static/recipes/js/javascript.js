//***Logic below to handle the main search functionality

document.getElementById('button-addon2').addEventListener('click', function () {
    console.log('Button clicked');
    performMainSearch();
});

function performMainSearch() {
    var searchQuery = document.getElementById('recipe-search-by-name-input').value;
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



//***Logic below to handle the advanced search functionality - with filters

document.getElementById('advanced-search-filters-modal-button').addEventListener('click', function () {
    console.log('Button clicked');
    performSearchByFilters();
});

function performSearchByFilters() {
    var searchFilter1 = document.getElementById('filter-option-selected1').value;
    console.log(searchFilter1)
    var searchFilter2 = document.getElementById('filter-option-selected2').value;
    console.log(searchFilter2)
    var searchFilter3 = document.getElementById('filter-option-selected3').value;
    console.log(searchFilter3)
    var searchFilter4 = document.getElementById('filter-option-selected4').value;
    console.log(searchFilter4)

    if (!searchFilter1 && !searchFilter2 && !searchFilter3 && !searchFilter4) {
        console.log('Search query is empty');
        return;
    }

    //***Used to build a URL dynamically based on how many and which filters are selected by users
    var url = '/search-recipe-filters/?';

    if (searchFilter1) {
        url += 'query1=' + searchFilter1;
    }

    if (searchFilter2) {
        if (searchFilter1) {
            url += '&';
        }
        url += 'query2=' + searchFilter2;
    }

    if (searchFilter3) {
        if (searchFilter1) {
            url += '&';
        }
        if (searchFilter2) {
            url += '&';
        }
        url += 'query3=' + searchFilter3;
    }

    if (searchFilter4) {
        if (searchFilter1) {
            url += '&';
        }
        if (searchFilter2) {
            url += '&';
        }
        if (searchFilter3) {
            url += '&';
        }
        url += 'query4=' + searchFilter4;
    }

    fetch(url)
        .then(response => response.json())
        .then(data => {
            displaySearchResults(data);
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}



//***Logic below to handle the advanced search functionality - by ingredients

document.getElementById('button-addon3').addEventListener('click', function () {
    console.log('Button clicked');
    performIngredientsSearch();
});

function performIngredientsSearch() {
    var searchQuery = document.getElementById('recipe-search-by-ingredients-input').value;
    console.log(searchQuery)

    if (!searchQuery) {
        console.log('Search query is empty');
        return;
    }

    fetch(`/search-recipe-ingredients/?query=${searchQuery}`)
        .then(response => response.json())
        .then(data => {
            displaySearchResults(data);
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}



//***Function below used to change dynamically the recipes UI to display the searched results, whether it \
//***is a search by name, by filters or by ingredients.

function displaySearchResults(data) {
    var recipes = data.recipes;
    var searchResultsContainer = document.getElementById('search-results');
    showSearchResultsSection();

    searchResultsContainer.innerHTML = '';

    if (recipes.length === 0) {
        var searchResultsRow = document.createElement('div');
        searchResultsRow.className = 'row';

        var leftColumn = document.createElement('div');
        leftColumn.className = 'col-sm-1 col-md-2';

        var middleColumn = document.createElement('div');
        middleColumn.className = 'col-sm-10 col-md-8 text-center';

        var mainSearchNotFound = document.createElement('div');
        mainSearchNotFound.className = 'card-general-padding';

        mainSearchNotFound.innerHTML = `
            <br>
            <br>
            <h1 class="recipes-continent-title-section">Recipe(s) not found</h1> 
            <br>
            <br>
            <div class="search-result-not-found">
                <span>For recipes searched by name or ingredient name, make sure there's are not spelling mistake in your text.</span>
                <br>
                <br>
                <span>***</span>
                <br>
                <br>
                <span>For recipes searched by filters (advanced search), consider reducing the number of filters applied for potentially more results.</span>
                <br>
                <br>
                <span>***</span>
                <br>
                <br>
                <span>If you still can't find your recipe, it's a sign! <a href="placeholder">Submit your recipe to us</a> so that we can display it for all users to enjoy. It's simple and it takes 2 minutes.</span>
                <br>
                <br>
                <span>***</span>
                <br>
                <br>
                <button type="button" class="btn btn-danger" onclick="clearSearch()">Clear search</button>
            </div>
            `;

        var rightColumn = document.createElement('div');
        rightColumn.className = 'col-sm-1 col-md-2';

        middleColumn.appendChild(mainSearchNotFound);

        searchResultsRow.appendChild(leftColumn);
        searchResultsRow.appendChild(middleColumn);
        searchResultsRow.appendChild(rightColumn);

        searchResultsContainer.appendChild(searchResultsRow);

    } else {
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
        <br>
        <div class="search-result-not-found">
            <button type="button" class="btn btn-danger" onclick="clearSearch()">Clear search</button>
            <br>
            <br>
        </div>
        `;

        searchResultsContainer.appendChild(headingContainer);

        var recipeRow = document.createElement('div');
        recipeRow.className = 'row card-general-padding';

        recipes.forEach(function (recipe) {
            var recipeCard = document.createElement('div');
            recipeCard.className = 'col-xl-4 col-lg-6 col-sm-12 card-bottom-padding';

            recipeCard.innerHTML = `
                <br>
                <div class="card text-bg-dark">
                    <img src="${recipe.pic}" class="img-fluid" alt="recipe-image">
                    <div class="card-img-overlay">
                        <div class="card-text">
                            <a href="${recipe.recipe_url}"><h5 class="card-title">${recipe.recipe_name}</h5></a>
                            <div class="line-background">
                                <img src="../../../media/flag-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>${recipe.recipe_origin_country}</span>
                            </div>
                            <br>
                            <div class="line-background">
                                <img src="../../../media/difficulty-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>${recipe.recipe_difficulty}</span>
                            </div>
                            <br>
                            <div class="line-background">
                                <img src="../../../media/category-icon.png" alt="flag-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>${recipe.recipe_category}</span>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            var currentPath = window.location.pathname;
            if (currentPath.includes('/recipes-list-signed-users/')) {
                var buttonContainer = document.createElement('div');
                buttonContainer.className = 'd-flex justify-content-center';
                buttonContainer.innerHTML = '<button type="button" class="btn btn-dark recipes-list-page-add-to-favorite-button">Add to favorite</button>';
                recipeCard.appendChild(buttonContainer);
            }
            recipeRow.appendChild(recipeCard);
        });
        searchResultsContainer.appendChild(recipeRow);
    }
}



//***Function below used to hide the default content sections and display the search results section
//***dynamically when users are doing researches. 

function showSearchResultsSection() {
    var defaultContentSections = document.getElementsByClassName('default-content');

    for (var i = 0; i < defaultContentSections.length; i++) {
        defaultContentSections[i].style.display = 'none';
    }

    var searchResultsSection = document.getElementById('search-results');
    searchResultsSection.style.display = 'block';
}



//***Function below used to return to main recipes list page when users click on the clear search button

function clearSearch() {
    var searchInput = document.getElementById('recipe-search-by-name-input');
    searchInput.value = '';

    var currentPath = window.location.pathname; 

    if (currentPath.includes('/recipes-list-signed-users/')) {
        window.location.href = '/recipes-list-signed-users';
    }
    else if (currentPath.includes('/recipes-list-unsigned-users/')) {
        window.location.href = '/recipes-list-unsigned-users';
    }
}



//***Code to ensure smooth transition in the page when user click on the back to top link at the \
//***bottom of the detailed page.

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

backToTopLink1.addEventListener('click', function (event) {
    scrollToSection(event, '#topsection');
});
