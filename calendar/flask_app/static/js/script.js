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

function getStats(seasonId){
    // console.log(id)
    // event.preventDefault()
    fetch(`http://localhost:5000/get_stats/${seasonId}`)
        .then( response => response.json() )
        .then( data => {
            console.log(data)
            let statsBody = document.getElementById('stats-body')
            statsBody.innerHTML = ''
            playersArray = data[0]
            teamStatsObj = data[1]


            document.getElementById('team-ppg').innerHTML = Number(teamStatsObj['points']).toFixed(1)
            document.getElementById('team-rpg').innerHTML = Number(teamStatsObj['rebounds']).toFixed(1)
            document.getElementById('team-apg').innerHTML = Number(teamStatsObj['assists']).toFixed(1)
            document.getElementById('team-spg').innerHTML = Number(teamStatsObj['steals']).toFixed(1)
            document.getElementById('team-bpg').innerHTML = Number(teamStatsObj['blocks']).toFixed(1)
            document.getElementById('team-tpg').innerHTML = Number(teamStatsObj['turnovers']).toFixed(1)
            document.getElementById('team-fg').innerHTML = `${(Number(teamStatsObj['made_shots'])/Number(teamStatsObj['attempted_shots']) * 100).toFixed(1)}%`
            document.getElementById('team-ft').innerHTML = '50%'

            for (i=0; i < playersArray.length; i++){
                res = `
                    <tr>
                        <td>${playersArray[i].number}</td>
                        <td>${playersArray[i].first_name} ${playersArray[i].last_name}</td>
                        <td></td>
                        <td></td>
                        <td>${ Number(playersArray[i].points).toFixed(1)}</td>
                        <td>${ Number(playersArray[i].assists).toFixed(1) }</td>
                        <td>${ Number(playersArray[i].rebounds).toFixed(1) }</td>
                        <td>${ Number(playersArray[i].steals).toFixed(1) }</td>
                        <td>${ Number(playersArray[i].blocks).toFixed(1) }</td>
                        <td>${ Number(playersArray[i].turnovers).toFixed(1) }</td>
                        <td>${ Number(playersArray[i].made_shots/playersArray[i].attempted_shots * 100).toFixed(1) }%</td>
                        <td></td>
                    </tr>
                `
                statsBody.innerHTML = statsBody.innerHTML + res
            }
        })
        
}


//SAVE FORM TO DATABASE AJAX

// let myForm = document.getElementById('form')

// document.getElementById('submit').addEventListener("click", function(event){
//     event.preventDefault()
//     let form = new FormData(myForm)
//     fetch("/save/note", { method :'POST', body : form})
//             .then( response => response.json() )
//             .then( data => console.log(data) )
//     submit()
// })