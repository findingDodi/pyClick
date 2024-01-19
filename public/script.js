const CLICK_BUTTON = document.getElementById('click-button');
const CLICKS = document.getElementById('clicks')
const INCREMENT_CLICKS_URL = '/api/increment-clicks';
const GET_CLICKS_URL = '/api/get-clicks';

function incrementClicks() {
    fetch(INCREMENT_CLICKS_URL)
        .then((response) => {
            //getClicks();
            return response.json();
        })
        .then((data) => {
            updateClicks(data);
        })
}
/*
async function getClicks() {
    const response = await fetch(GET_CLICKS_URL);
    const clicks = await response.json();
    updateClicks(clicks);
}
*/

function getClicks() {
    fetch(GET_CLICKS_URL).then(response => updateClicks(response.json()));
}

function updateClicks(updatesClicks) {
    CLICKS.innerText = updatesClicks;
}

CLICK_BUTTON.addEventListener('click', incrementClicks)