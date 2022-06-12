window.onload = function () {
    weather()
};


function diaDaSemana(dia, mes, ano) {
    const semana = [
        "Domingo",
        "Segunda",
        "Terça",
        "Quarta",
        "Quinta",
        "Sexta",
        "Sábado"
    ];
    return semana[new Date(`${ano}/${mes}/${dia}`).getDay()]
};

function weather(){

    var nameOut = document.querySelector('.name')
    var dateOut = document.querySelector('.date')
    var iconOut = document.querySelector('.icon')
    var tempOut = document.querySelector('.temp')
    var conditionOut = document.querySelector('.condition')

    fetch('https://api.weatherapi.com/v1/current.json?key=6453194fd1b3454e97e184604221106&q=Lisboa&aqi=no&lang=pt')
    .then(response => response.json())
    .then(data => {
        console.log(data);

        tempOut.innerHTML = data.current.temp_c + "&#176;";
        conditionOut.innerHTML = data.current.condition.text;

        nameOut.innerHTML = data.location.name;
        const date = data.location.localtime;

        const y = parseInt(date.substr(0,4));
        const m = parseInt(date.substr(5,2));
        const d = parseInt(date.substr(8,2));

        dateOut.innerHTML = `${diaDaSemana(d,m,y)} ${d}, ${m} ${y}`;

        iconOut.src = data.current.condition.icon;


    });
}
