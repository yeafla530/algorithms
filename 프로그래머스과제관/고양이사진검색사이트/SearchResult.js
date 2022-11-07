export default function SearchResult({$app, initialState}) {
    this.state = initialState;
    this.$target = document.createElement("div")
    this.$target.className = "SearchResult"
    $app.appendChild(this.$target);
  
    this.data = initialData;
    this.onClick = onClick;
  
    
  
    this.setState = (nextData) => {
      this.state = nextData;
      this.render();
    }
  
    this.render = () => {
      if (this.state.data) {
        this.$target.innerHTML = this.state.data
          .map(
            (cat, idx) => `
              <div class="item" data-index="${idx}">
                <img src=${cat.url} alt=${cat.name} />
              </div>
            `
          )
          .join("");
  
      }
    }
    
  
    this.onClick = onClick;
  
    this.$target.addEventListener("click", (e) => {
      const $searchItem = e.target.closet(".item")
      const { index } = $searchItem.dataset;
      this.onClick(this.state[index])
    });
  
    this.render()
    
  }
  