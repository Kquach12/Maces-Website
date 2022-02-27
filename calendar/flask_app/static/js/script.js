function getGames(event){
    // console.log(event.target.value)
    // event.preventDefault()
    fetch(`http://localhost:5000/get_games/${event.target.value}`)
        .then( response => response.json() )
        .then( data => {
            console.log(data) 
            // TODO: change below to correct div later on
            let testDiv = document.getElementById('testDiv')

            for (let i = 0; i < data.length; i++){
                
                let locationClass = 'schedule-game-home'
                let level = 'Varsity'
                let outComeDiv = `${data[i]['date']} <br> ${data[i]['time']}`

                if (data[i]['location'] == 'away'){
                    locationClass = 'schedule-game-away'
                }

                if (data[i]['level'] == 1){
                    level = 'JV'
                }

                if (data[i]['outcome'] == 0){
                    outComeDiv = `Loss, ${data[i]['maces_score']} - ${data[i]['opponent_score']}`
                }
                else if (data[i]['outcome'] == 1){
                    outComeDiv = `Win, ${data[i]['maces_score']} - ${data[i]['opponent_score']}`
                }

                res = `
                    <div class="${locationClass} d-flex justify-content-between align-items-center mb-3">
                        <span class="d-flex justify-content-center align-items-center">
                            <img src="../static/images/logo2.PNG" alt="" style="width: 100px;">
                            <div class="ml-5">
                                <h3>${data[i]['opponent']}</h3>
                                <h5>${level}</h5>
                            </div>
                        </span>
                        <div>${outComeDiv}</div>
                    </div>
                `
                testDiv.innerHTML = testDiv.innerHTML + res

            }
        })
        
}



// {%if games%}
//             {% for game in games %}
//             {% if game.location == 'home'%}
//                 <div class="schedule-game-home d-flex justify-content-between align-items-center mb-3">
//             {% else %}
//                 <div class="schedule-game-away d-flex justify-content-between align-items-center mb-3">
//             {% endif %}
//                     <span class="d-flex justify-content-center align-items-center">
//                         <img src="../static/images/logo2.PNG" alt="" style="width: 100px;">
//                         <div class="ml-5">
//                             <h3>{{game.opponent}}</h3>
//                             {% if game.level ==0%}
//                                 <h5>Varsity</h5>
//                             {% else %}
//                                 <h5>JV</h5>
//                             {% endif %}
//                         </div>
//                     </span>
//                     {% if game.outcome == 0 %}
//                         <div>
//                             <h5>Loss, {{game.maces_score}}-{{game.opponent_score}}</h5>
//                         </div>
//                     {% elif game.outcome == 1 %}
//                         <div>
//                             <h5>Win, {{game.maces_score}}-{{game.opponent_score}}</h5>
//                         </div>
//                     {% else %}
//                         <div>
//                             <h5>{{game.date}}</h5>
//                             <h5>{{game.time}}</h5>
//                         </div>
//                     {% endif %}

//                 </div>
//             {% endfor %}
//         {% endif %}