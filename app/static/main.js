window.onload = function () {
    let parse_data = function(new_data, dataset) {
        let date = new_data[0];
        if (date === dataset.time[dataset.time.length - 1]) {
            console.log('No han llegado nuevos datos...')
        } else {
            if (dataset.time.length > 5) {
                dataset.time.shift();
                dataset.cookie1.shift();
                dataset.cookie2.shift();
                dataset.tea.shift();
                dataset.coffee.shift();
            }
            dataset.time.push(new_data[0]);
            dataset.cookie1.push(new_data[1]);
            dataset.cookie2.push(new_data[2]);
            dataset.tea.push(new_data[3]);
            dataset.coffee.push(new_data[4]);
        }
    };


    let dataset = {
        time: [],
        cookie1: [],
        cookie2: [],
        tea: [],
        coffee: []
    };


    let ctx = document.getElementById("myChart").getContext('2d');
    let ctx_2 = document.getElementById('liquids_chart').getContext('2d');
    let liquidChart = new Chart(ctx_2, {
       type: 'line',
        data: {
            labels: dataset.time,
            datasets: [
                {
                    label: "Te",
                    data: dataset.tea,
                    backgroundColor: 'green',
                    borderColor: 'green',
                    borderWidth: 1,
                    fill: false
                },
                {
                    label: "Cafe",
                    data: dataset.coffee,
                    backgroundColor: 'blue',
                    borderColor: 'blue',
                    borderWidth: 1,
                    fill: false
                }
                ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: "Liquidos"
            },
            tooltips: {
                mode: 'index',
                intersect: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        displayFormats: {
                            second: 'h:mm:ss a'
                        }
                    },
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: "Peso"
                    }
                }]
            }
        }
    });
    let myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dataset.time,
            datasets: [
                {
                    label: "Galleta 1",
                    data: dataset.cookie1,
                    backgroundColor: 'red',
                    borderColor: 'red',
                    borderWidth: 1,
                    fill: false
                },
                {
                    label: "Galleta 2",
                    data: dataset.cookie2,
                    backgroundColor: 'orange',
                    borderColor: 'orange',
                    borderWidth: 1,
                    fill: false
                }
                ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: "Galletas"
            },
            tooltips: {
                mode: 'index',
                intersect: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        displayFormats: {
                            second: 'h:mm:ss a'
                        }
                    },
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: "Peso"
                    }
                }]
            }
        }
    });

    function get_data() {
        let request = new XMLHttpRequest();
        request.open('GET', 'api/datos', true);
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                let data = JSON.parse(this.response);
                parse_data(data, dataset);
                myChart.update();
                liquidChart.update();
            } else {
                alert('server error')
            }
        };

        request.onerror = function() {
            alert('connection error')
        };
        request.send();
    }
    get_data();
    let query = setInterval(get_data, 1000);

};
