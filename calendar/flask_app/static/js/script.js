function getGames(seasonId){
    // console.log(id)
    // event.preventDefault()
    fetch(`http://localhost:5000/get_games/${seasonId}`)
        .then( response => response.json() )
        .then( data => {
            console.log(data)
            let gamesDiv = document.getElementById('gamesDiv')
            let winPctId = document.getElementById('winPctId')
            let recordId = document.getElementById('recordId')
            gamesDiv.innerHTML = ''

            gamesArray = data[0]
            winPct = data[1]
            record = data[2]

            winPctId.innerHTML = `${winPct}%`
            recordId.innerHTML = `${record['wins']} - ${record['losses']}`

            for (let i = 0; i < gamesArray.length; i++){
                
                let locationClass = 'schedule-game-home'
                let level = 'Varsity'
                let outComeDiv = `${gamesArray[i]['date']} <br> ${gamesArray[i]['time']}`

                if (gamesArray[i]['location'] == 'away'){
                    locationClass = 'schedule-game-away'
                }

                if (gamesArray[i]['level'] == 1){
                    level = 'JV'
                }

                if (gamesArray[i]['outcome'] == 0){
                    outComeDiv = `Loss, ${gamesArray[i]['maces_score']} - ${gamesArray[i]['opponent_score']}`
                }
                else if (gamesArray[i]['outcome'] == 1){
                    outComeDiv = `Win, ${gamesArray[i]['maces_score']} - ${gamesArray[i]['opponent_score']}`
                }

                res = `
                    <div class="${locationClass} d-flex justify-content-between align-items-center mb-3">
                        <span class="d-flex justify-content-center align-items-center">
                            <img src="../static/images/logo2.PNG" alt="" style="width: 100px;">
                            <div class="ml-5">
                                <h3>${gamesArray[i]['opponent']}</h3>
                                <h5>${level}</h5>
                            </div>
                        </span>
                        <div><h5>${outComeDiv}</h5></div>
                    </div>
                `
                gamesDiv.innerHTML = gamesDiv.innerHTML + res

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