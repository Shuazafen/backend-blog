const init = () => {
    fetch('blogs.json')
    .then(response => response.json())
    .then(data => {
        items = data;
        console.log(items)
        addDataToHTML();
    })
}

init();

let items = [];
let carts = [];
let listProductHTML = document.querySelector('.items')


const addDataToHTML = () => {
    listProductHTML.innerHTML = '';
    if(items.length > 0){
      items.forEach(product => {
  
        let newProduct = document.createElement('li');
        newProduct.classList.add('item__wrap');
        newProduct.dataset.id = product.id;
        newProduct.innerHTML = `
        <div class="items">
        <img src="${product.image}" alt="food image" class="img_holder">
        <button class='li-btn'>${product.category}</button>
      </div>
    
      <div class="pt-5">
        <div class="mb-2">
          <h4>${product.time}</h4>
          <h2 class="card__title">${product.title}</h2>
          <p class="paragraph">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
      </div>
      `;
      listProductHTML.appendChild(newProduct);
      })
     
    }
  }

  