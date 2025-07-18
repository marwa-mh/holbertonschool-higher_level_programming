fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data =>{
      const ul=  document.getElementById('list_movies');
      data.results.forEach(element => {
        let li = document.createElement('li');
        li.textContent= element.title;
        ul.appendChild(li);
      });
        
    })
    .catch(error =>{
        console.error('Error fetching character:', error);
    });