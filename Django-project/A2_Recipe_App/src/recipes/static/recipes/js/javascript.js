//***Logic below to handle the main recipe search bar functionality (search by name)
document.getElementById('search-recipe-by-name-button').addEventListener('click', function () {
    performMainSearch();
});

function performMainSearch() {
    var searchQuery = document.getElementById('recipe-search-by-name-input').value;

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
    performSearchByFilters();
});

function performSearchByFilters() {
    var searchFilter1 = document.getElementById('filter-option-selected1').value;
    var searchFilter2 = document.getElementById('filter-option-selected2').value;
    var searchFilter3 = document.getElementById('filter-option-selected3').value;
    var searchFilter4 = document.getElementById('filter-option-selected4').value;

    if (!searchFilter1 && !searchFilter2 && !searchFilter3 && !searchFilter4) {
        console.log('Search query is empty');
        return;
    }

    //***Used to build a URL dynamically based on how many and which filters are selected 
    //***by users
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
document.getElementById('search-recipe-by-ingredient-button').addEventListener('click', function () {
    performIngredientsSearch();
});

function performIngredientsSearch() {
    var searchQuery = document.getElementById('recipe-search-by-ingredients-input').value;

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



//***Function below used to change dynamically the recipes list UI to display the searched 
//***results, whether it is a search by name, by filters or by ingredients.
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
                <span>If you still can't find your recipe, it's a sign! <a href="/recipes-submit/"> Submit your recipe to us</a> so that we can display it for all users to enjoy. It's simple and it takes 2 minutes.</span>
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
            <img src="../../../media/difficulty-icon.png" alt="level-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>Difficulty</span>
            <span class="vertical-line">|</span>
            <img src="../../../media/category-icon.png" alt="category-icon" style="width: 20px; height: 20px; margin-right: 5px;"><span>Category</span>
        </div> 
        <br>
        <br>
        <div class="search-result-not-found">
            <button type="button" class="btn btn-danger" onclick="clearSearch()">Clear search</button>
            <br>
        </div>
        `;

        searchResultsContainer.appendChild(headingContainer);

        var recipeRow = document.createElement('div');
        recipeRow.className = 'row card-general-padding';

        recipes.forEach(function (recipe) {
            var recipeCard = document.createElement('div');
            recipeCard.className = 'col-xl-4 col-lg-6 col-sm-12 card-bottom-padding';

            var currentPath = window.location.pathname;

            var recipeUrl;
            if (currentPath === '/recipes-list-signed-users/') {
                recipeUrl = recipe.recipe_url_signed_users;
            } else if (currentPath === '/recipes-list-unsigned-users/') {
                recipeUrl = recipe.recipe_url;
            }

            recipeCard.innerHTML = `
            <div class="card text-bg-dark">
                <a href="${recipeUrl}">
                    <img src="${recipe.pic}" class="img-fluid" alt="recipe-image">
                </a>                                
                <div class="card-text">
                    <div>
                        <a href="${recipeUrl}">
                            <h5 class="card-title-custom">${recipe.recipe_name}</h5>
                        </a>
                    </div>
                    <div class="recipe-card-quick-info">
                        <img src="../../../media/flag-icon.png" class="card-icons" alt="flag-icon"><span>${recipe.origin_country}</span>
                    </div>
                    <br>
                    <div class="recipe-card-quick-info">
                        <img src="../../../media/difficulty-icon.png" class="card-icons" alt="difficulty-icon"><span>${recipe.difficulty}</span>
                    </div>
                    <br>
                    <div class="recipe-card-quick-info">
                        <img src="../../../media/category-icon.png" class="card-icons" alt="category-icon"><span>${recipe.recipe_category}</span>
                    </div>
                </div>
            </div>
        `;

            recipeRow.appendChild(recipeCard);
        });
        searchResultsContainer.appendChild(recipeRow);
    }
}



//***Function below used to hide the default recipes list UI and display the search results
//***UI dynamically when users are doing researches. 
function showSearchResultsSection() {
    var defaultContentSections = document.getElementsByClassName('default-content');

    for (var i = 0; i < defaultContentSections.length; i++) {
        defaultContentSections[i].style.display = 'none';
    }

    var searchResultsSection = document.getElementById('search-results');
    searchResultsSection.style.display = 'block';
}



//***Function below used to return to main recipes list UI when users click on the clear 
//***search button.
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



// Logic for the 'show more' and 'reduce' buttons on the north america recipes section
document.addEventListener("DOMContentLoaded", function () {

    var visibleCardCount = 7;
    var cards = document.querySelectorAll('.north-america-recipes');

    function showMoreCards() {
        var hiddenCards = document.querySelectorAll('.north-america-recipes-hidden');
        for (var i = 0; i < hiddenCards.length && i < 6; i++) {
            hiddenCards[i].classList.remove('north-america-recipes-hidden');
            visibleCardCount++;
        }

        if (visibleCardCount >= cards.length) {
            document.getElementById('showMoreButtonNorthAmerica').style.display = 'none';
            document.getElementById('hideExtraCardButtonNorthAmerica').style.display = 'block';
        }
    }

    function hideExtraCards() {
        for (var i = visibleCardCount - 1; i >= 7; i--) {
            cards[i].classList.add('north-america-recipes-hidden');
        }
    
        visibleCardCount = 7;
    
        document.getElementById('hideExtraCardButtonNorthAmerica').style.display = 'none';
        document.getElementById('showMoreButtonNorthAmerica').style.display = 'block';
    }

    if (cards.length > visibleCardCount) {
        for (var i = visibleCardCount; i < cards.length; i++) {
            cards[i].classList.add('north-america-recipes-hidden');
        }
        document.getElementById('showMoreButtonNorthAmerica').style.display = 'block';
    } else {
        document.getElementById('showMoreButtonNorthAmerica').style.display = 'none';
    }

    document.getElementById('showMoreButtonNorthAmerica').addEventListener('click', showMoreCards);
    document.getElementById('hideExtraCardButtonNorthAmerica').addEventListener('click', hideExtraCards);
});



// Logic for the 'show more' and 'reduce' buttons on the central america recipes section
document.addEventListener("DOMContentLoaded", function () {

    var visibleCardCount = 7;
    var cards = document.querySelectorAll('.central-america-recipes');

    function showMoreCards() {
        var hiddenCards = document.querySelectorAll('.central-america-recipes-hidden');
        for (var i = 0; i < hiddenCards.length && i < 6; i++) {
            hiddenCards[i].classList.remove('central-america-recipes-hidden');
            visibleCardCount++;
        }

        if (visibleCardCount >= cards.length) {
            document.getElementById('showMoreButtonCentralAmerica').style.display = 'none';
            document.getElementById('hideExtraCardButtonCentralAmerica').style.display = 'block';
        }
    }

    function hideExtraCards() {
        for (var i = visibleCardCount - 1; i >= 7; i--) {
            cards[i].classList.add('central-america-recipes-hidden');
        }
    
        visibleCardCount = 7;
    
        document.getElementById('hideExtraCardButtonCentralAmerica').style.display = 'none';
        document.getElementById('showMoreButtonCentralAmerica').style.display = 'block';
    }

    if (cards.length > visibleCardCount) {
        for (var i = visibleCardCount; i < cards.length; i++) {
            cards[i].classList.add('central-america-recipes-hidden');
        }
        document.getElementById('showMoreButtonCentralAmerica').style.display = 'block';
    } else {
        document.getElementById('showMoreButtonCentralAmerica').style.display = 'none';
    }

    document.getElementById('showMoreButtonCentralAmerica').addEventListener('click', showMoreCards);
    document.getElementById('hideExtraCardButtonCentralAmerica').addEventListener('click', hideExtraCards);
});



// Logic for the 'show more' and 'reduce' buttons on the south america recipes section
document.addEventListener("DOMContentLoaded", function () {

    var visibleCardCount = 7;
    var cards = document.querySelectorAll('.south-america-recipes');

    function showMoreCards() {
        var hiddenCards = document.querySelectorAll('.south-america-recipes-hidden');
        for (var i = 0; i < hiddenCards.length && i < 6; i++) {
            hiddenCards[i].classList.remove('south-america-recipes-hidden');
            visibleCardCount++;
        }

        if (visibleCardCount >= cards.length) {
            document.getElementById('showMoreButtonSouthAmerica').style.display = 'none';
            document.getElementById('hideExtraCardButtonSouthAmerica').style.display = 'block';
        }
    }

    function hideExtraCards() {
        for (var i = visibleCardCount - 1; i >= 7; i--) {
            cards[i].classList.add('south-america-recipes-hidden');
        }
    
        visibleCardCount = 7;
    
        document.getElementById('hideExtraCardButtonSouthAmerica').style.display = 'none';
        document.getElementById('showMoreButtonSouthAmerica').style.display = 'block';
    }

    if (cards.length > visibleCardCount) {
        for (var i = visibleCardCount; i < cards.length; i++) {
            cards[i].classList.add('south-america-recipes-hidden');
        }
        document.getElementById('showMoreButtonSouthAmerica').style.display = 'block';
    } else {
        document.getElementById('showMoreButtonSouthAmerica').style.display = 'none';
    }

    document.getElementById('showMoreButtonSouthAmerica').addEventListener('click', showMoreCards);
    document.getElementById('hideExtraCardButtonSouthAmerica').addEventListener('click', hideExtraCards);
});



// Function for the 'show more' and 'reduce' buttons on the europe recipes section
document.addEventListener("DOMContentLoaded", function () {

    var visibleCardCount = 7;
    var cards = document.querySelectorAll('.europe-recipes');

    function showMoreCards() {
        var hiddenCards = document.querySelectorAll('.europe-recipes-hidden');
        for (var i = 0; i < hiddenCards.length && i < 6; i++) {
            hiddenCards[i].classList.remove('europe-recipes-hidden');
            visibleCardCount++;
        }

        if (visibleCardCount >= cards.length) {
            document.getElementById('showMoreButtonEurope').style.display = 'none';
            document.getElementById('hideExtraCardButtonEurope').style.display = 'block';
        }
    }

    function hideExtraCards() {
        for (var i = visibleCardCount - 1; i >= 7; i--) {
            cards[i].classList.add('europe-recipes-hidden');
        }
    
        visibleCardCount = 7;
    
        document.getElementById('hideExtraCardButtonEurope').style.display = 'none';
        document.getElementById('showMoreButtonEurope').style.display = 'block';
    }

    if (cards.length > visibleCardCount) {
        for (var i = visibleCardCount; i < cards.length; i++) {
            cards[i].classList.add('europe-recipes-hidden');
        }
        document.getElementById('showMoreButtonEurope').style.display = 'block';
    } else {
        document.getElementById('showMoreButtonEurope').style.display = 'none';
    }

    document.getElementById('showMoreButtonEurope').addEventListener('click', showMoreCards);
    document.getElementById('hideExtraCardButtonEurope').addEventListener('click', hideExtraCards);
});



//***Code to ensure smooth transition in the pages when users click on the 'back to top'
//***link at the bottom of the pages.
function scrollToSection(event, targetSectionId) {
    event.preventDefault();
    var targetSection = document.querySelector(targetSectionId);
    var offset = targetSection.getBoundingClientRect().top + window.scrollY;
    window.scrollTo({
        top: offset,
        behavior: 'smooth'
    });
}

var backToTopLink1 = document.querySelector('.back-to-top-link');
backToTopLink1.addEventListener('click', function (event) {
    scrollToSection(event, '#topsection');
});

var backToNorthAmericaRecipes = document.querySelector('#hideExtraCardButtonNorthAmerica');
backToNorthAmericaRecipes.addEventListener('click', function (event) {
    scrollToSection(event, '#northAmericaRecipes');
});

var backToCentralAmericaRecipes = document.querySelector('#hideExtraCardButtonCentralAmerica');
backToCentralAmericaRecipes.addEventListener('click', function (event) {
    scrollToSection(event, '#centralAmericaRecipes');
});

var backToSouthAmericaRecipes = document.querySelector('#hideExtraCardButtonSouthAmerica');
backToSouthAmericaRecipes.addEventListener('click', function (event) {
    scrollToSection(event, '#southAmericaRecipes');
});

var backToEuropeRecipes = document.querySelector('#hideExtraCardButtonEurope');
backToEuropeRecipes.addEventListener('click', function (event) {
    scrollToSection(event, '#europeRecipes');
});
