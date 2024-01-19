const CLICK_BUTTON = document.getElementById('click-button');
const CLICKS = document.getElementById('clicks')
const INCREMENT_CLICKS_URL = '/api/increment-clicks';
const GET_CLICKS_URL = '/api/get-clicks';

function incrementClicks() {
    fetch(INCREMENT_CLICKS_URL)
        .then(() => {
            getClicks();
        });
}

function getClicks() {
    fetch(GET_CLICKS_URL)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            updateClicks(data);
        });
}

function updateClicks(updatesClicks) {
    CLICKS.innerText = updatesClicks;
}

CLICK_BUTTON.addEventListener('click', incrementClicks);
setInterval(getClicks, 1000);