async function onFavoriteClick(event) {
    event.preventDefault()
    let url = event.target.dataset.itemFavoriteUrl
    const settings = {
        method: 'POST',
        headers: {"X-CSRFToken": getCookie("csrftoken")},
    }
    let response = await fetch(url, settings)
    let favoriteInfo = await response.json()
    event.target.innerText = favoriteInfo.value
}

function onLoad() {
    const favoriteButtons = document.querySelectorAll('.item-favorite')
    favoriteButtons.forEach(function (curBtn) {
        curBtn.addEventListener('click', onFavoriteClick)
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = onLoad