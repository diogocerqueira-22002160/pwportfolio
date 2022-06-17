

https://api.nasa.gov/planetary/apod?api_key=0BUCItLduVvPd63YbBaAlZbej19RhjBmyp2Wsm43

function nasa(){

    let image = document.querySelector('.nasa-img')
    let title = document.querySelector('.title')
     fetch('https://api.nasa.gov/planetary/apod?api_key=0BUCItLduVvPd63YbBaAlZbej19RhjBmyp2Wsm43')
    .then(response => response.json())
    .then(data => {
        console.log(data);

        image.src = data.url
        title.innerHTML = data.title
    });
}


nasa().onload;